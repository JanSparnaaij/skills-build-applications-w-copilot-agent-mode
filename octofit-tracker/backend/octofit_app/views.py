from django.http import JsonResponse
from django.views import View
from .models import User, Team, Activity, Leaderboard, Workout

class UserListView(View):
    def get(self, request):
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)

class TeamListView(View):
    def get(self, request):
        teams = list(Team.objects.values())
        return JsonResponse(teams, safe=False)

class ActivityListView(View):
    def get(self, request):
        activities = list(Activity.objects.values())
        return JsonResponse(activities, safe=False)

class LeaderboardListView(View):
    def get(self, request):
        leaderboards = list(Leaderboard.objects.values())
        return JsonResponse(leaderboards, safe=False)

class WorkoutListView(View):
    def get(self, request):
        workouts = list(Workout.objects.values())
        return JsonResponse(workouts, safe=False)

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboards': '/api/leaderboards/',
        'workouts': '/api/workouts/',
    })
