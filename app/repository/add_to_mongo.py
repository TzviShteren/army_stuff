from app.db.mongo_database import all_messages_collection


def add_to_mongo(data):
    try:
        all_messages_collection.insert_one(data)
        print("Database initialized with sample data.")
    except Exception as e:
        print(f"An error occurred: {e}")
