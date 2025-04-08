from pymongo import MongoClient
from django.conf import settings

# Establish a connection to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

# Collections
users_collection = db['users']
teams_collection = db['teams']
activities_collection = db['activity']
leaderboard_collection = db['leaderboard']
workouts_collection = db['workouts']
