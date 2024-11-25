import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

const ROBOHASH_URL = "https://robohash.org";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function generateRobohashUrl(hash?: string) {
  hash = hash || Math.random().toString(36).substring(3);
  return `${ROBOHASH_URL}/${hash}.svg`;
}
