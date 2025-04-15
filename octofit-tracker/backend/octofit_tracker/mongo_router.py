from pymongo import MongoClient
from django.conf import settings

class MongoRouter:
    """
    A router to control all database operations on models in the MongoDB database.
    """

    def db_for_read(self, model, **hints):
        return 'mongo'

    def db_for_write(self, model, **hints):
        return 'mongo'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return False

# Initialize MongoDB client
mongo_client = MongoClient(**settings.MONGO_CLIENT_SETTINGS)

def get_mongo_db():
    return mongo_client[settings.MONGO_CLIENT_SETTINGS['authSource']]
