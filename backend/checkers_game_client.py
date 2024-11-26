import requests

BASE_URL = "http://127.0.0.1:5000"  # URL of your Flask server

class CheckersGameClient:
    def __init__(self):
        self.game_uuid = None

    def create_room(self, player_name, player_image=None):
        """
        Creates a new game room for the first player.
        """
        payload = {"playerName": player_name, "playerImage": player_image}
        response = requests.post(f"{BASE_URL}/create_room", json=payload)
        if response.status_code == 200:
            data = response.json()
            self.game_uuid = data["gameUuid"]
            print(f"Game created successfully! Game UUID: {self.game_uuid}")
        else:
            print("Error creating room")
            return None

    def join_room(self, game_uuid, player_name, player_image=None):
        """
        Allows a second player to join an existing room.
        """
        payload = {"gameUuid": game_uuid, "playerName": player_name, "playerImage": player_image}
        response = requests.post(f"{BASE_URL}/join_room", json=payload)
        if response.status_code == 200:
            print(f"Player {player_name} joined the game successfully!")
        else:
            print("Error joining room")
            return None

    def get_game_state(self):
        """
        Retrieves and prints the current state of the game.
        """
        if not self.game_uuid:
            print("No game in progress.")
            return

        response = requests.get(f"{BASE_URL}/game_state/{self.game_uuid}")
        if response.status_code == 200:
            data = response.json()
            print(f"Game state: {data['state']}")
            print(f"Current Turn: {'Player 1' if data['state'] == 'player1_turn' else 'Player 2'}")
            print("Board:")
            self.print_board(data["board"])
        else:
            print("Error retrieving game state")

    def make_move(self, from_pos, to_pos):
        """
        Make a move on the board.
        """
        if not self.game_uuid:
            print("No game in progress.")
            return

        move_payload = {
            "gameUuid": self.game_uuid,
            "from": from_pos,
            "to": to_pos
        }

        response = requests.post(f"{BASE_URL}/move", json=move_payload)
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                print(f"Error: {data['error']}")
            else:
                print(f"Move from {from_pos} to {to_pos} was successful!")
        else:
            print("Error making move")

    def print_board(self, board):
        """
        Prints the board with row and column numbers on all sides.
        """
        # Print top column numbers (a to h)
        print("   " + "  ".join(chr(i) for i in range(ord('a'), ord('h') + 1)))

        # Print the board with row numbers (1 to 8)
        for idx, row in enumerate(board):
            print(f"{8 - idx}  " + "  ".join(row))

        # Print bottom column numbers again (a to h)
        print("   " + "  ".join(chr(i) for i in range(ord('a'), ord('h') + 1)))
        print()

    def play_game(self, player_name, player_image=None):
        """
        Start and play the game with two players.
        """
        # Player 1 creates the game
        if not self.game_uuid:
            self.create_room(player_name, player_image)

        while True:
            self.get_game_state()

            # Ask the current player for a move
            from_pos_str = input("Enter the 'from' position (e.g., a1): ").lower()
            to_pos_str = input("Enter the 'to' position (e.g., a2): ").lower()

            # Convert the input into board indices
            from_pos = self.convert_position(from_pos_str)
            to_pos = self.convert_position(to_pos_str)

            if from_pos and to_pos:
                self.make_move(from_pos, to_pos)

                # Check if game state indicates a win
                self.get_game_state()
                continue_or_quit = input("Do you want to continue? (y/n): ").lower()
                if continue_or_quit != 'y':
                    break
            else:
                print("Invalid input, please try again.")

    def convert_position(self, pos_str):
        """
        Converts a position string (e.g., 'a1') to board indices (e.g., (7, 0)).
        """
        if len(pos_str) != 2:
            print("Invalid position format!")
            return None

        column, row = pos_str
        if column not in 'abcdefgh' or row not in '12345678':
            print("Invalid position input!")
            return None

        col_idx = ord(column) - ord('a')  # Convert 'a' to 0, 'b' to 1, etc.
        row_idx = 8 - int(row)  # Convert row 1-8 to 7-0

        return (row_idx, col_idx)

if __name__ == "__main__":
    client = CheckersGameClient()

    # Example: Player 1 starts the game
    player_name_1 = "Player 1"
    player_name_2 = "Player 2"
    player_image_1 = "https://example.com/player1.png"
    player_image_2 = "https://example.com/player2.png"

    # Start and play the game
    client.play_game(player_name_1, player_image_1)
    client.play_game(player_name_2, player_image_2)
