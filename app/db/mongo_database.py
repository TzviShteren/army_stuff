from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

client = MongoClient(os.environ['DB_MONGO_URL'])
db = client['army_stuff']
all_messages_collection = db['all_messages']
