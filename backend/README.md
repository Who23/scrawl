# backend for scrawl.
## setup
- install python3
- install (poetry)[https://python-poetry.org]
- Run `make init`
- setup google console oauth client id & client secret into specified json file. Set up the client using [this](https://support.google.com/cloud/answer/6158849) and downlaod the client_secret.json

## usage
`make dev` - dev server
`make prod` - prod server