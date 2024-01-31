from os import environ

#TG Credentials
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

#Website Credentials
API_KEY = environ.get('API_KEY', '')
API_URL = environ.get('API_URL', 'https://linksmoney.in/api')
WEB_NAME = environ.get('WEB_NAME', 'linksmoney.in')

#Optional
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '')
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', '')
