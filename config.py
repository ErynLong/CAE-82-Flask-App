## Config
import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    REGISTERED_USERS = {
        'kevinb@codingtemple.com':{"name":"Kevin", "password":"123abc"},
        'alext@codingtemple.com':{"name":"Alex", "password":"Colt45"},
        'joelc@codingtemple.com':{"name":"Joel", "password":"MorphinTime"}
    }
