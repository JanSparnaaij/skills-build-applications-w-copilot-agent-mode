import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.core.management.base import BaseCommand
from octofit_tracker.mongo_router import mongo_router

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        db = mongo_router.db

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboards.delete_many({})
        db.workouts.delete_many({})

        # Create test users
        db.users.insert_many([
            {'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123'},
            {'username': 'jane_doe', 'email': 'jane@example.com', 'password': 'password123'},
        ])

        # Create test teams
        db.teams.insert_one({
            'name': 'Team Alpha',
            'description': 'Alpha team description',
            'members': ['john_doe', 'jane_doe'],
        })

        # Create test activities
        db.activities.insert_many([
            {'user': 'john_doe', 'activity_type': 'Running', 'duration': 30, 'date': '2025-04-10'},
            {'user': 'jane_doe', 'activity_type': 'Cycling', 'duration': 45, 'date': '2025-04-11'},
        ])

        # Create test leaderboard
        db.leaderboards.insert_one({
            'team': 'Team Alpha',
            'points': 150,
        })

        # Create test workouts
        db.workouts.insert_many([
            {'name': 'Morning Yoga', 'description': 'A relaxing yoga session', 'duration': 60, 'difficulty': 'Easy'},
            {'name': 'HIIT', 'description': 'High-intensity interval training', 'duration': 30, 'difficulty': 'Hard'},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))