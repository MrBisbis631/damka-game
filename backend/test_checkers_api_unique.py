import unittest
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

class TestCheckersAPI(unittest.TestCase):

    def setUp(self):
        """
        This method runs before every test.
        """
        self.game_uuid = None

    def test_create_room_valid(self):
        """
        Test creating a valid game room.
        """
        payload = {"playerName": "Player 1", "playerImage": "https://example.com/player1.png"}
        response = requests.post(f"{BASE_URL}/create_room", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("gameUuid", data)
        self.game_uuid = data["gameUuid"]

    def test_create_room_invalid(self):
        """
        Test creating a game room with missing payload.
        """
        payload = {}  # Missing playerName
        response = requests.post(f"{BASE_URL}/create_room", json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn("error", data)

    def test_join_room_valid(self):
        """
        Test joining a valid game room.
        """
        self.test_create_room_valid()  # Create a valid room first
        payload = {"gameUuid": self.game_uuid, "playerName": "Player 2",
                   "playerImage": "https://example.com/player2.png"}
        response = requests.post(f"{BASE_URL}/join_room", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("gameUuid", data)

    def test_join_room_invalid(self):
        """
        Test joining a game room with an invalid UUID.
        """
        payload = {"gameUuid": "invalid-uuid", "playerName": "Player 2",
                   "playerImage": "https://example.com/player2.png"}
        response = requests.post(f"{BASE_URL}/join_room", json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn("error", data)


    def test_game_state_valid(self):
        """
        Test fetching the game state for a valid game.
        """
        self.test_create_room_valid()  # Create a valid room first
        response = requests.get(f"{BASE_URL}/game_state/{self.game_uuid}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("gameUuid", data)
        self.assertIn("board", data)

    def test_game_state_invalid(self):
        """
        Test fetching the game state with an invalid UUID.
        """
        response = requests.get(f"{BASE_URL}/game_state/invalid-uuid")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("error", data)

if __name__ == "__main__":
    unittest.main()
