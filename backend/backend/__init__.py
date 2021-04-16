# -*- coding: utf-8 -*-

import os
import flask
import requests
import json

import google.oauth2.credentials
import google_auth_oauthlib.flow

CLIENT_SECRETS_FILE = "./secrets/client_secret.json" # oauth client id & client secret
SCOPES = ['openid']
FLASK_SECRET_KEY_FILE = "./secrets/secret_key.txt" # flask session secret key

app = flask.Flask(__name__, template_folder="dist", static_folder="dist/assets/")
app.secret_key = open(FLASK_SECRET_KEY_FILE, 'br').read()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  # redirect to dev vite server if we're running dev flask server
  if app.debug:
      return flask.redirect('http://localhost:3333')
  return flask.render_template('index.html')

@app.route('/')
def index():
  return '''<a href="/test">Do OAuth</a>
  <a href="/revoke">Revoke Credentials</a>
  <a href="/clear">Clear session</a>'''


@app.route('/test')
def show_id_token():
  if 'credentials' not in flask.session:
    return flask.redirect('authorize')

  credentials = google.oauth2.credentials.Credentials(
      **flask.session['credentials'])

  # TODO: put in db
  flask.session['credentials'] = credentials_to_dict(credentials)
  return flask.jsonify(credentials_to_dict(credentials))


@app.route('/authorize')
def authorize():
  # Start OAuth 2.0 Authorization Grant Flow
  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=SCOPES)

  flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

  authorization_url, state = flow.authorization_url(
      access_type='offline') #,
      # include_granted_scopes='true')

  flask.session['state'] = state

  return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
  # state from original /authorize call
  state = flask.session['state']

  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
  flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

  authorization_response = flask.request.url
  flow.fetch_token(authorization_response=authorization_response)

  # TODO: put in db
  credentials = flow.credentials
  flask.session['credentials'] = credentials_to_dict(credentials)

  return flask.redirect(flask.url_for('show_id_token'))


@app.route('/revoke')
def revoke():
  if 'credentials' not in flask.session:
    return ('You need to <a href="/authorize">authorize</a> before revoking')

  credentials = google.oauth2.credentials.Credentials(
    **flask.session['credentials'])

  revoke = requests.post('https://oauth2.googleapis.com/revoke',
      params={'token': credentials.token},
      headers = {'content-type': 'application/x-www-form-urlencoded'})

  clear_credentials()
  status_code = getattr(revoke, 'status_code')
  if status_code == 200:
    return('Credentials successfully revoked.' + index())
  else:
    return('An error occurred.' + index())


@app.route('/clear')
def clear_credentials():
  if 'credentials' in flask.session:
    del flask.session['credentials']
  return ('Credentials have been cleared.<br><br>' +
          index())


def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'id_token': credentials.id_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes,
          'quota_project_id': credentials.quota_project_id}

def run_dev(secure):
  if not secure:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  app.run('localhost', 8080, debug=True)
