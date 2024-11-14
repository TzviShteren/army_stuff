from flask import request, jsonify, Flask
from app.db.mongo_database import init_to_mongo_db
app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def all_messages():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        init_to_mongo_db(data)
        return jsonify({"message": "Data inserted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
