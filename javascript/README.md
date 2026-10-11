# @crawlora-org/spotify

JavaScript and TypeScript client for Crawlora's hosted Spotify API.
It calls [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-javascript-homepage); it does not run a browser or scrape Spotify locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Spotify or its owners.

## Install

```sh
npm install @crawlora-org/spotify
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { SpotifyClient } from "@crawlora-org/spotify";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new SpotifyClient({ apiKey });
const result1 = await client.search({ q: "daft punk" });
console.log(result1);
const result2 = await client.track({ id: "4cOdK2wGLETKBW3PvgPWqT" });
console.log(result2);
```

The client also exports `Client` as an alias for `SpotifyClient`. Operation
methods are available directly in camelCase and through the `spotify`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-spotify/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-spotify/blob/main/examples/javascript.mjs) for a complete usage example.


## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
