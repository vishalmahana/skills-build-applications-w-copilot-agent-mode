from django.core.management.base import BaseCommand
from octofit_tracker.models import users_collection, teams_collection, activities_collection, leaderboard_collection, workouts_collection
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Drop existing collections
        users_collection.drop()
        teams_collection.drop()
        activities_collection.drop()
        leaderboard_collection.drop()
        workouts_collection.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        users_collection.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        teams_collection.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": timedelta(hours=1).total_seconds()},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": timedelta(hours=2).total_seconds()},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": timedelta(hours=1, minutes=30).total_seconds()},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": timedelta(minutes=30).total_seconds()},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15).total_seconds()},
        ]
        activities_collection.insert_many(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        leaderboard_collection.insert_many(leaderboard_entries)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        workouts_collection.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
