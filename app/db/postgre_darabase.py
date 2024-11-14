from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ['DB_POSTGRESQL_URL'])
session_maker = sessionmaker(bind=engine)
