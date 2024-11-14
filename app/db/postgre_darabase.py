from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

engine = create_engine(os.environ['DB_POSTGRESQL_URL'])
session_maker = sessionmaker(bind=engine)


def check_postgresql_connection():
    try:
        with session_maker() as session:
            result = session.execute(text("SELECT version();"))
            version = result.fetchone()
            print(f"Connected successfully: PostgreSQL version: {version[0]}")
            return True
    except Exception as e:
        print(f"Failed to connect: {e}")
        return False
