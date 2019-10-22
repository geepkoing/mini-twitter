from flask import Flask, request, jsonify

app = Flask(__name__)
app.users = {}
app.id_count = 1

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@app.route('/sign-up', methods=['POST'])
def sign_up():
    user = request.json
    user['id'] = app.id_count
    app.users[app.id_count] = user
    app.id_count = app.id_count + 1

    return jsonify(user)