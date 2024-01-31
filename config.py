from os import environ

#TG Credentials
API_ID = int(environ.get('API_ID', '24003416'))
API_HASH = environ.get('API_HASH', '013d9b3fe388308ff1272d33d1e40e2b')
BOT_TOKEN = environ.get('BOT_TOKEN', '6858627899:AAEtsmzG_9kRpwXqkULMXn56Bn5K5fTp4fU')

#Website Credentials
API_KEY = environ.get('API_KEY', 'c7951680b0ff1e52743c10eae2f4de6a6e1175b1')
API_URL = environ.get('API_URL', 'https://linksmoney.in/api')
WEB_NAME = environ.get('WEB_NAME', 'linksmoney.in')

#Optional
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', 'https://t.me/linksmoneysupport')
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', 'https://t.me/linksmoneyofficial')
