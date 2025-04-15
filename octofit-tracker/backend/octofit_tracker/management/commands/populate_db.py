from django.core.management.base import BaseCommand
from octofit_tracker.mongo_router import get_mongo_db

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Connect to the database
        db = get_mongo_db()

        # Define test data for users, teams, activities, leaderboard, and workouts
        users = [
            {"email": "user1@example.com", "name": "User One", "age": 25},
            {"email": "user2@example.com", "name": "User Two", "age": 30}
        ]
        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]}
        ]
        activities = [
            {"user": "user1@example.com", "type": "running", "duration": 30},
            {"user": "user2@example.com", "type": "cycling", "duration": 45}
        ]
        leaderboard = [
            {"user": "user1@example.com", "score": 100},
            {"user": "user2@example.com", "score": 90}
        ]
        workouts = [
            {"name": "Morning Run", "duration": 30},
            {"name": "Evening Yoga", "duration": 60}
        ]

        # Insert test data into collections
        db.users.create_index("email", unique=True)
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))