from flask import Blueprint, request, jsonify
import os
from app.kafka_settings.producer import produce
from dotenv import load_dotenv

load_dotenv(verbose=True)

email_blueprint = Blueprint('api/email', __name__)

new_member_topic = os.environ['GET_ALL_DATA_TO_MONGO_TOPIC']


# get the data from enosh
@email_blueprint.route('/', methods=['POST'])
def all_messages():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        produce(
            topic=new_member_topic,
            key=data['email'].encode('utf-8'),
            value=data
        )

        data.produce_member(data)
        return jsonify({"message": "Data inserted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
