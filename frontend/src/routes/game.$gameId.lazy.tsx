import { createLazyFileRoute } from "@tanstack/react-router";

export const Route = createLazyFileRoute("/game/$gameId")({
  component: Game,
});

function Game() {
  const { gameId } = Route.useParams();
  return <div className="p-2">Game {gameId}</div>;
}
