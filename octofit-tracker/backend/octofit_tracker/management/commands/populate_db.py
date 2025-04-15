import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.core.management.base import BaseCommand
from octofit_app.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', description='Alpha team description')
        team1.members.add(user1, user2)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-10')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-11')

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, points=150)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60, difficulty='Easy')
        Workout.objects.create(name='HIIT', description='High-intensity interval training', duration=30, difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))