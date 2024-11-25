import { createLazyFileRoute } from "@tanstack/react-router";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { useEffect, useState } from "react";
import { type CarouselApi } from "@/components/ui/carousel";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { generateRobohashUrl } from "@/lib/utils";
import { CreateRoomRequest, JoinRoomRequest } from "@/types";

export const Route = createLazyFileRoute("/")({
  component: Index,
});

function Index() {
  return (
    <div className="min-h-screen flex flex-col justify-between">
      <div className="mb-5">
        <h1 className="text-center text-3xl font-semibold my-5">
          Welcome to Damka game
        </h1>
        <p className="text-muted-foreground text-sm text-center max-w-md mx-auto mb-5">
          Damka is played on an 8x8 board with 12 pieces per player. The player
          with the light pieces moves first. A player wins when the opponent has
          no legal moves left.
        </p>
        <ActionTabs />
      </div>
      <div className="chess-board-bg p-28 text-center"></div>
    </div>
  );
}

function ActionTabs() {
  const [actionData, setActionData] = useState<
    JoinRoomRequest & CreateRoomRequest
  >({
    playerName: "",
    playerImage: "",
    gameUuid: "",
  });

  const [images] = useState<string[]>(() =>
    Array.from({ length: 10 }).map(() => generateRobohashUrl())
  );

  useEffect(() => {
    setActionData((prev) => ({
      ...prev,
      playerImage: images[0],
    }));
  }, [images]);

  const onChooseAvatar = (avatarUrl: string) => {
    setActionData((prev) => ({ ...prev, playerImage: avatarUrl }));
  };

  const setActionDataField =
    (field: keyof typeof actionData) =>
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setActionData((prev) => ({ ...prev, [field]: e.target.value }));
    };

  return (
    <Tabs defaultValue="create-room" className="w-[400px] mx-auto">
      <TabsList className="grid w-full grid-cols-2">
        <TabsTrigger value="create-room">Create room</TabsTrigger>
        <TabsTrigger value="join-room">Join room</TabsTrigger>
      </TabsList>
      <TabsContent value="create-room">
        <Card>
          <CardHeader>
            <CardTitle>Create a Room</CardTitle>
            <CardDescription>
              Fill in the details below to create a new game room. Once created,
              you can share the room code with your friends to join.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-2">
            <div className="space-y-1">
              <Label htmlFor="username">Photo</Label>
              <ChooseAvatar images={images} onChoose={onChooseAvatar} />
            </div>
            <div className="space-y-1">
              <Label htmlFor="name">Name</Label>
              <Input
                id="name"
                onChange={setActionDataField("playerName")}
                value={actionData.playerName}
              />
            </div>
          </CardContent>
          <CardFooter>
            <Button>Create room</Button>
          </CardFooter>
        </Card>
      </TabsContent>
      <TabsContent value="join-room">
        <Card>
          <CardHeader>
            <CardTitle>Join room</CardTitle>
            <CardDescription>
              Enter the room code shared by your friend to join the game.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-2">
            <div className="space-y-1">
              <Label htmlFor="username">Photo</Label>
              <ChooseAvatar images={images} onChoose={onChooseAvatar} />
            </div>
            <div className="space-y-1">
              <Label htmlFor="name">Name</Label>
              <Input id="name" onChange={setActionDataField("playerName")} />
            </div>
            <div className="space-y-1">
              <Label htmlFor="roomId">Room ID</Label>
              <Input id="roomId" onChange={setActionDataField("gameUuid")} />
            </div>
          </CardContent>
          <CardFooter>
            <Button>Join room</Button>
          </CardFooter>
        </Card>
      </TabsContent>
    </Tabs>
  );
}

type ChooseAvatarProps = {
  onChoose: (avatarUrl: string) => void;
  images: string[];
};

function ChooseAvatar({ onChoose, images }: ChooseAvatarProps) {
  const [api, setApi] = useState<CarouselApi>();

  useEffect(() => {
    if (!api) return;

    api.on("select", (e) => {
      const index = e.slidesInView()[0];
      onChoose(images[index]);
    });
  }, [api, images, onChoose]);

  return (
    <Carousel className="size-24 mx-auto" setApi={setApi}>
      <CarouselContent className="aaaaaa">
        {images.map((url, index) => (
          <CarouselItem key={index}>
            <Avatar className="size-24">
              <AvatarImage src={url} />
              <AvatarFallback>BT</AvatarFallback>
            </Avatar>
          </CarouselItem>
        ))}
      </CarouselContent>
      <CarouselPrevious />
      <CarouselNext />
    </Carousel>
  );
}
