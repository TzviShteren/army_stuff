import flask
from faker.proxy import Faker
from app.kafka_settings.consumer import consume
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

fake = Faker()
app = flask.Flask(__name__)


def test(data):
    print(data)


if __name__ == '__main__':
    consume(
        topic=os.environ['GET_DATA_TOPIC'],
        function=test
    )
