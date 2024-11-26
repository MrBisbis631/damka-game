import uuid

def create_room(data, games):
    try:
        player_name = data["playerName"]
        player_image = data.get("playerImage")
        game_uuid = str(uuid.uuid4())
        
        starting_board = [
            ["w", "e", "w", "e", "w", "e", "w", "e"],
            ["e", "w", "e", "w", "e", "w", "e", "w"],
            ["w", "e", "w", "e", "w", "e", "w", "e"],
            ["e", "e", "e", "e", "e", "e", "e", "e"],
            ["e", "e", "e", "e", "e", "e", "e", "e"],
            ["e", "b", "e", "b", "e", "b", "e", "b"],
            ["b", "e", "b", "e", "b", "e", "b", "e"],
            ["e", "b", "e", "b", "e", "b", "e", "b"]
        ]

        games[game_uuid] = {
            "state": "waiting",
            "board": starting_board,
            "player1": {"id": str(uuid.uuid4()), "name": player_name, "image": player_image},
            "player2": None,
        }
        return {"gameUuid": game_uuid}
    except KeyError:
        return {"error": "Missing required field 'playerName'."}


def join_room(data, games):
    try:
        game_uuid = data["gameUuid"]
        player_name = data["playerName"]
        player_image = data.get("playerImage")

        if game_uuid not in games:
            return {"error": "Game not found."}
        if games[game_uuid]["player2"] is not None:
            return {"error": "Game is already full."}

        games[game_uuid]["player2"] = {"id": str(uuid.uuid4()), "name": player_name, "image": player_image}
        games[game_uuid]["state"] = "player1_turn"
        return {"gameUuid": game_uuid}
    except KeyError:
        return {"error": "Missing required fields."}


def get_game_state(game_uuid, games):
    if game_uuid not in games:
        return {"error": "Game not found."}
    game = games[game_uuid]
    return {
        "gameUuid": game_uuid,
        "state": game["state"],
        "board": game["board"],
        "player1": game["player1"],
        "player2": game["player2"],
    }


def make_move(data, games):
    try:
        game_uuid = data["gameUuid"]
        from_pos = data["from"]
        to_pos = data["to"]

        if game_uuid not in games:
            return {"error": "Game not found."}

        # Validate and update board logic (simplified here)
        game = games[game_uuid]
        board = game["board"]

        # Check if it's a valid move (dummy logic for example)
        if board[from_pos[0]][from_pos[1]] not in ["w", "b"]:
            return {"error": "Invalid move. No piece at 'from' position."}

        # Update board (for simplicity)
        board[to_pos[0]][to_pos[1]] = board[from_pos[0]][from_pos[1]]
        board[from_pos[0]][from_pos[1]] = "e"

        # Update turn state
        game["state"] = "player2_turn" if game["state"] == "player1_turn" else "player1_turn"
        return {"message": "Move successful."}
    except KeyError:
        return {"error": "Invalid request payload."}

