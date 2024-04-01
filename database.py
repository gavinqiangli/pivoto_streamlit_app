import json
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")


def connect_2_db():
    # connect to mongo
    password = quote_plus(MONGODB_PASSWORD)
    url = f"mongodb+srv://{MONGODB_USERNAME}:{password}@cluster0.hm3ugvt.mongodb.net/{MONGODB_DB_NAME}?retryWrites=true&w=majority"

    client = MongoClient(url)
    db = client[MONGODB_DB_NAME]
    api_keys = db["api_keys"]
    feedbacks = db["feedbacks"]
    newsletter_users = db["newsletter_users"]

    return api_keys, feedbacks, newsletter_users


def find_api_key(api_key):
    api_keys, _, _ = connect_2_db()
    find_api_key = api_keys.find_one({"api_key": api_key})
    return find_api_key

def save_feedback_to_db(feedback):
    _, feedbacks, _ = connect_2_db()
    feedbacks.insert_one({"feedback": feedback})

def find_newsletter_user(email):
    _, _, newsletter_users = connect_2_db()
    find_user = newsletter_users.find_one({"email": email})
    return find_user

def save_newsletter_user_to_db(email):
    _, _, newsletter_users = connect_2_db()
    newsletter_users.insert_one({"email": email})




# if __name__ == '__main__':
#   _,_ = connect_2_db()
