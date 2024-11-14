from flask import request, jsonify, Flask
import os
from app.kafka_settings.producer import produce
from dotenv import load_dotenv
from app.service.send_to_consumer_service import send_to_consumer_service
import logging
from app.routes.receiving_content_route import receiving_content_bp

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


app.register_blueprint(receiving_content_bp, url_prefix="/receiving_content")

if __name__ == '__main__':
    app.run()
