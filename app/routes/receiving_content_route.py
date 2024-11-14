from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
from app.repository.sql_queries import *
load_dotenv(verbose=True)

receiving_content_bp = Blueprint('receiving_content', __name__)


@receiving_content_bp.route('/search_by_email/', methods=['GET'])
def search_by_email():
    try:
        email = request.json
        if not email:
            return jsonify({"error": "No email provided"}), 400

        res = the_full_content_of_an_object_by_email(email['email'])
        logging.info("test 4")
        return jsonify(res), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
