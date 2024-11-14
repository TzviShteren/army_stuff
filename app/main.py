from flask import request, jsonify, Flask
import os
from app.kafka_settings.producer import produce
from dotenv import load_dotenv
from app.service.send_to_consumer_service import send_to_consumer_service
import logging

load_dotenv(verbose=True)
app = Flask(__name__)

logging.basicConfig(filename='db_logs.log', level=logging.INFO)

NEW_MEMBER_TOPIC = os.environ['GET_DATA_TOPIC']


# get the data from enosh
@app.route('/api/email/', methods=['POST'])
def all_messages():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        send_to_consumer_service(data['sentences'])

        produce(
            topic=NEW_MEMBER_TOPIC,
            key=data['email'],
            value=data
        )

        # data.produce_member(data)
        return jsonify({"message": "Data inserted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
