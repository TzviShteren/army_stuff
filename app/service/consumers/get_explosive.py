import flask
from faker.proxy import Faker
from app.kafka_settings.consumer import consume
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

fake = Faker()


def test(data):
    print(data)


app = flask.Flask(__name__)

if __name__ == '__main__':
    consume(
        topic=os.environ['MESSAGES_EXPLOSIVE_TOPIC'],
        function=test
    )
    app.run()
