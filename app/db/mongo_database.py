
from flask.cli import load_dotenv
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

client = MongoClient(os.environ['DB_MONGO_URL'])
db = client['army_stuff']
all_messages_collection = db['all_messages']


def init_to_mongo_db(data):
    all_messages_collection.drop()

    all_messages_collection.insert_many(data)

    print("Database initialized with sample data.")
