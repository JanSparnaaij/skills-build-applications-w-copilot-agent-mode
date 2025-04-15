from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='teams')

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    points = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.IntegerField()  # in minutes
    difficulty = models.CharField(max_length=50)
