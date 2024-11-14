import flask
from app.kafka_settings.consumer import consume
import os
from dotenv import load_dotenv
from app.service.consumers.Inserting_to_postgres.repository.insert_data import insert_data
load_dotenv(verbose=True)

app = flask.Flask(__name__)


if __name__ == '__main__':
    consume(
        topic=os.environ['GET_DATA_TOPIC'],
        function=insert_data
    )
    app.run()
