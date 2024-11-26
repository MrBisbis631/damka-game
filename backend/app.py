from flask import Flask, request, jsonify
import uuid
from game_logic import create_room, join_room, get_game_state, make_move

app = Flask(__name__)

# In-memory storage for simplicity
games = {}

@app.route('/create_room', methods=['POST'])
def create_room_endpoint():
    data = request.json
    response = create_room(data, games)
    return jsonify(response), 200 if "gameUuid" in response else 400

@app.route('/join_room', methods=['POST'])
def join_room_endpoint():
    data = request.json
    response = join_room(data, games)
    return jsonify(response), 200 if "gameUuid" in response else 400

@app.route('/game_state/<game_uuid>', methods=['GET'])
def game_state_endpoint(game_uuid):
    response = get_game_state(game_uuid, games)
    return jsonify(response), 200 if "gameUuid" in response else 404

@app.route('/move', methods=['POST'])
def move_endpoint():
    data = request.json
    response = make_move(data, games)
    return jsonify(response), 200 if "error" not in response else 400

if __name__ == '__main__':
    app.run(debug=True)
