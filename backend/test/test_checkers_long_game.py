import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestCheckersLongGame(unittest.TestCase):

    def setUp(self):
        """
        Initialize a new game and add two players before running the tests.
        """
        print("\nSetting up a new game...")

        # Create the game room
        create_room_payload = {"playerName": "Player 1", "playerImage": "https://example.com/player1.png"}
        response = requests.post(f"{BASE_URL}/create_room", json=create_room_payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.game_uuid = data["gameUuid"]
        print(f"Game created with UUID: {self.game_uuid}")

        # Join the game with Player 2
        join_room_payload = {"gameUuid": self.game_uuid, "playerName": "Player 2", "playerImage": "https://example.com/player2.png"}
        response = requests.post(f"{BASE_URL}/join_room", json=join_room_payload)
        self.assertEqual(response.status_code, 200)
        print("Player 2 joined the game.")

    def test_long_game_to_win(self):
        """
        Simulate a sequence of moves leading to a win for one player.
        """
        print("Starting the game simulation...")
        moves = [
            # Player 1 moves
            {"from": [5, 0], "to": [4, 1]},
            # Player 2 moves
            {"from": [2, 1], "to": [3, 0]},
            # Player 1 moves
            {"from": [4, 1], "to": [2, 3]},  # Captures Player 2's piece
            # Player 2 moves
            {"from": [2, 3], "to": [3, 4]},
            # Player 1 moves
            {"from": [5, 2], "to": [4, 3]},
            # Player 2 moves
            {"from": [2, 3], "to": [3, 2]},  # Captures Player 1's piece
            # Continue with more moves
        ]

        # Apply the moves sequentially
        for i, move in enumerate(moves):
            print(f"\nMove {i + 1}: {move}")
            payload = {"gameUuid": self.game_uuid, "from": move["from"], "to": move["to"]}
            response = requests.post(f"{BASE_URL}/move", json=payload)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            print(f"Response: {data}")
            self.assertNotIn("error", data)

        # Check the game state for a win
        print("\nFetching the final game state...")
        response = requests.get(f"{BASE_URL}/game_state/{self.game_uuid}")
        self.assertEqual(response.status_code, 200)
        game_state = response.json()
        print(f"Final Game State: {game_state}")
        self.assertIn("state", game_state)
        self.assertIn("player1_won", ["player1_won", "player2_won"])  # Expect one player to win

if __name__ == "__main__":
    unittest.main()
