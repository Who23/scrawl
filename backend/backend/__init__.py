# -*- coding: utf-8 -*-
# TODO: only store openID token in cookie rather than everything.

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

@app.route('/api/logged_in')
def isLoggedIn():
  logged_in = False
  if 'credentials' in flask.session:
    logged_in = True

  return flask.jsonify({ 'response' : logged_in })


@app.route('/api/login')
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


@app.route('/api/oauth2callback')
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

  del flask.session['state']

  return flask.redirect(flask.url_for('index'))

@app.route('/api/logout')
def revoke():
  if 'credentials' not in flask.session:
    return flask.redirect(flask.url_for('index'))

  credentials = google.oauth2.credentials.Credentials(
    **flask.session['credentials'])

  revoke = requests.post('https://oauth2.googleapis.com/revoke',
      params={'token': credentials.token},
      headers = {'content-type': 'application/x-www-form-urlencoded'})

  clear_credentials()
  status_code = getattr(revoke, 'status_code')
  if status_code == 200:
    return flask.redirect(flask.url_for('index'))
  else:
    return { 'response': f"Revoke failed with status {status_code}"}, 500

def clear_credentials():
  if 'credentials' in flask.session:
    del flask.session['credentials']

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
