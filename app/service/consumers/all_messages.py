import flask
from faker.proxy import Faker
from app.repository.add_to_mongo import add_to_mongo
from app.kafka_settings.consumer import consume
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

fake = Faker()

app = flask.Flask(__name__)

if __name__ == '__main__':
    consume(
        topic=os.environ['GET_ALL_DATA_TO_MONGO_TOPIC'],
        function=add_to_mongo
    )
    app.run()
