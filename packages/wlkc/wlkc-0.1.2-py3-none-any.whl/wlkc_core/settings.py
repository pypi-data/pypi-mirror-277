import os
from logging.config import dictConfig

from sqlalchemy import QueuePool

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

# DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'flask-website.db')

DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/admin?charset=utf8mb4'

DATABASE_CONNECT_OPTIONS = {"echo": True, "echo_pool": True, "pool_size": 20, "pool_timeout": 30, "pool_pre_ping": True, "pool_recycle": 3600, "poolclass": QueuePool}

# WHOOSH_INDEX = os.path.join(BASE_DIR, 'flask-website.whoosh')
SCHEDULER_API_ENABLED = True
STATIC_PATH = [
    "/favicon.ico",
    "/login",
    "/captchaImage"
]
REDIS_URL = "redis://redis:redis123@redis:6379/3"

JWT_SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz'
AUTH_CHECK = True

CAPTCHA_IMAGE_PREFIX = "login:img:"
TOKEN = "token"
TOKEN_PREFIX = "Bearer "
LOGIN_USER_KEY = "login_user_key"
LOGIN_TOKEN_PREFIX = 'login_tokens:'

LOG_PATH = os.path.join(os.getcwd(), './logs/')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            # 'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            'class': "wlkc_core.utils.loggingHandler.CustomFormatter",
            'format': '[%(asctime)s] [%(process)s] - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        "file": {
            'class': 'wlkc_core.utils.loggingHandler.TimeLoggerRolloverHandler',
            'level': 'DEBUG',
            'filename': LOG_PATH + "wlkc.log",
            'formatter': 'default'
        }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi', 'file']
    }
}
dictConfig(LOGGING_CONFIG)
