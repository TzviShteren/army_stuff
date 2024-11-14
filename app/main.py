from flask import request, jsonify, Flask

app = Flask(__name__)


@app.route('/new_member', methods=['POST'])
def new_member():
    print(request.json)


if __name__ == '__main__':
    app.run()
