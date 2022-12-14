import os
from dotenv import load_dotenv

load_dotenv(".env")
# LOADS ENVIRONMENTS FILE (.env) IF EXISTS ELSE USE DEFAULTS VALUE

AMAZON_ACCESS_KEY = os.getenv('AMAZON_ACCESS_KEY', 'YOUR_ACCESS_KEY')
AMAZON_SECRET_KEY = os.getenv('AMAZON_SECRET_KEY', 'YOUR_SECRET_KEY')
AMAZON_PARTNER_ID = os.getenv('AMAZON_PARTNER_ID', 'YOUR_PARTNER_ID')
AMAZON_COUNTRY = os.getenv('AMAZON_COUNTRY', 'YOUR_COUNTRY_ID')
REDIS_DATABASE_HOST = os.getenv('REDIS_DATABASE_HOST', '127.0.0.1')
REDIS_DATABASE_PORT = os.getenv('REDIS_DATABASE_PORT', 6379)
REDIS_DATABASE_USERNAME = os.getenv('REDIS_DATABASE_USERNAME', None)
REDIS_DATABASE_PASSWORD = os.getenv('REDIS_DATABASE_PASSWORD', None)
CATEGORY_REFRESH_TIMEOUT_SECONDS = os.getenv('CATEGORY_REFRESH_TIMEOUT_SECONDS', 3600)
CATEGORY_NUMBER_DOWNLOAD_ITEMS = os.getenv('CATEGORY_NUMBER_DOWNLOAD_ITEMS', 100)
MAX_ITEM_COUNT_OFFER = os.getenv('MAX_ITEM_COUNT_OFFER', 10)
MAX_ITEM_PAGE_OFFER = os.getenv('MAX_ITEM_PAGE_OFFER', 10)
THROTTLING_SECONDS = os.getenv('THROTTLING_SECONDS', 2)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/1')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/1')
DEBUG = os.getenv('DEBUG', True)
