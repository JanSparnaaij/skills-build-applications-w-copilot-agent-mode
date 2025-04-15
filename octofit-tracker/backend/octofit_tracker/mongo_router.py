from pymongo import MongoClient
from django.conf import settings

class MongoRouter:
    def __init__(self):
        self.client = MongoClient(
            host=settings.MONGO_CLIENT_SETTINGS['host'],
            port=settings.MONGO_CLIENT_SETTINGS['port'],
            username=settings.MONGO_CLIENT_SETTINGS['username'],
            password=settings.MONGO_CLIENT_SETTINGS['password'],
            authSource=settings.MONGO_CLIENT_SETTINGS['authSource'],
        )
        self.db = self.client[settings.DATABASES['default']['NAME']]

    def get_collection(self, collection_name):
        return self.db[collection_name]

mongo_router = MongoRouter()
