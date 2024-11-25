type Color = "w" | "b" | "e";

export type ErrorResponse = {
  error: string;
};

export type GameStateResponse =
  | {
      gameUuid: string;
      state:
        | "waiting"
        | "player1_turn"
        | "player2_turn"
        | "player1_won"
        | "player2_won";

      board: Color[][];
      player1: {
        id: string;
        name: string;
        image?: string;
      };
      player2?: {
        id: string;
        name: string;
        image?: string;
      };
    }
  | ErrorResponse;

export type MoveRequest = {
  gameUuid: string;
  from: [number, number];
  to: [number, number];
};

export type CreateRoomRequest = {
  playerName: string;
  playerImage?: string;
};

export type CreateRoomResponse =
  | {
      gameUuid: string;
    }
  | ErrorResponse;

export type JoinRoomRequest = {
  gameUuid: string;
  playerName: string;
  playerImage?: string;
};

export type JoinRoomResponse =
  | {
      gameUuid: string;
    }
  | ErrorResponse;
