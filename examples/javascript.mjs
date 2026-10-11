import { SpotifyClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new SpotifyClient({ apiKey });

  const search = await client.search({ q: "daft punk" });
  console.log("search", search);
  const track = await client.track({ id: "4cOdK2wGLETKBW3PvgPWqT" });
  console.log("track", track);
