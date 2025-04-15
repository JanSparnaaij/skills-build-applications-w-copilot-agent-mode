from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # MongoDB connection settings
        client = MongoClient(
            host='localhost',
            port=27017,
            username='',
            password='',
            authSource='admin'
        )

        # Connect to the database
        db = client['octofit_db']

        # Define test data
        test_data = [
            {"name": "John Doe", "email": "john.doe@example.com", "age": 30, "active": True},
            {"name": "Jane Smith", "email": "jane.smith@example.com", "age": 25, "active": True},
            {"name": "Alice Johnson", "email": "alice.johnson@example.com", "age": 35, "active": False},
        ]

        # Insert test data into a collection (e.g., "users")
        users_collection = db['users']
        users_collection.insert_many(test_data)

        self.stdout.write(self.style.SUCCESS('Test data has been successfully inserted into the database.'))