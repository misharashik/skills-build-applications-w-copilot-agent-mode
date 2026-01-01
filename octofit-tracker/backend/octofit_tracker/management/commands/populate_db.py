from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

# Sample data
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "dc"},
    {"name": "Batman", "email": "batman@dc.com", "team": "dc"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "marvel"},
]
TEAMS = [
    {"name": "marvel"},
    {"name": "dc"},
]
ACTIVITIES = [
    {"user": "superman@dc.com", "activity": "fly", "duration": 60},
    {"user": "ironman@marvel.com", "activity": "run", "duration": 30},
]
LEADERBOARD = [
    {"team": "marvel", "points": 100},
    {"team": "dc", "points": 90},
]
WORKOUTS = [
    {"name": "Pushups", "difficulty": "easy"},
    {"name": "Squats", "difficulty": "medium"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient(host='localhost', port=27017)
        db = client["octofit_db"]
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        db.users.create_index("email", unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
