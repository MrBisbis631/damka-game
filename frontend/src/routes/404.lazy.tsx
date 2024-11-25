import { createLazyFileRoute } from "@tanstack/react-router";

export const Route = createLazyFileRoute("/404")({
  component: RouteComponent,
});

function RouteComponent() {
  return "Hello /404!";
}
