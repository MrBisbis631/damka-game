import uuid

def create_room(data, games):
    try:
        player_name = data["playerName"]
        player_image = data.get("playerImage")
        game_uuid = str(uuid.uuid4())
        
        # Define the starting board configuration
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

def get_game_state(game_uuid, games):

def make_move(data, games):


