# @crawlora-org/spotify — Spotify API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Spotify API.
It exposes 38 API endpoints for search, tracks, albums, artists, playlists, profiles, audiobooks, charts, and podcast shows and episodes through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-javascript-homepage). It does not run a browser or scrape Spotify locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Spotify or its owners.

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

## Supported Spotify API endpoints

This package exposes each route below as a direct method and through the `spotify` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-spotify/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/spotify-podcasts/categories` | `spotify-podcasts-categories` | Retrieve Spotify Podcasts categories |
| `GET` | `/spotify-podcasts/charts` | `spotify-podcasts-charts` | Retrieve Spotify podcast charts |
| `GET` | `/spotify-podcasts/episode` | `spotify-podcasts-episode` | Retrieve Spotify podcast episode details |
| `GET` | `/spotify-podcasts/home` | `spotify-podcasts-home` | Retrieve Spotify Podcasts home |
| `GET` | `/spotify-podcasts/search` | `spotify-podcasts-search` | Search Spotify Podcasts |
| `GET` | `/spotify-podcasts/show` | `spotify-podcasts-show` | Retrieve Spotify podcast show metadata |
| `GET` | `/spotify-podcasts/show/episodes` | `spotify-podcasts-show-episodes` | Retrieve Spotify podcast show episodes |
| `GET` | `/spotify-podcasts/show/recommendations` | `spotify-podcasts-show-recommendations` | Retrieve Spotify podcast recommendations |
| `GET` | `/spotify/album` | `spotify-album` | Retrieve Spotify album details |
| `GET` | `/spotify/album/tracks` | `spotify-album-tracks` | Retrieve Spotify album tracks |
| `GET` | `/spotify/albums/search` | `spotify-albums-search` | Search Spotify albums |
| `GET` | `/spotify/artist` | `spotify-artist` | Retrieve Spotify artist details |
| `GET` | `/spotify/artist/albums` | `spotify-artist-albums` | Retrieve Spotify artist albums |
| `GET` | `/spotify/artist/playlists` | `spotify-artist-playlists` | Retrieve Spotify artist playlists |
| `GET` | `/spotify/artist/related` | `spotify-artist-related` | Retrieve Spotify related artists |
| `GET` | `/spotify/artists/search` | `spotify-artists-search` | Search Spotify artists |
| `GET` | `/spotify/audiobook` | `spotify-audiobook` | Retrieve Spotify audiobook details |
| `GET` | `/spotify/audiobook/chapters` | `spotify-audiobook-chapters` | Retrieve Spotify audiobook chapters |
| `GET` | `/spotify/audiobooks/search` | `spotify-audiobooks-search` | Search Spotify audiobooks |
| `GET` | `/spotify/chapter` | `spotify-chapter` | Retrieve Spotify audiobook chapter details |
| `GET` | `/spotify/episodes/search` | `spotify-episodes-search` | Search Spotify episodes |
| `GET` | `/spotify/featured-charts-by-country` | `spotify-featured-charts-by-country` | Retrieve Spotify featured charts by country |
| `GET` | `/spotify/genre` | `spotify-genre` | Retrieve Spotify genre page |
| `GET` | `/spotify/home` | `spotify-home` | Retrieve Spotify home sections |
| `GET` | `/spotify/playlist` | `spotify-playlist` | Retrieve Spotify playlist details |
| `GET` | `/spotify/playlists/search` | `spotify-playlists-search` | Search Spotify playlists |
| `GET` | `/spotify/popular-by-country` | `spotify-popular-by-country` | Retrieve Spotify popular by country |
| `GET` | `/spotify/profile` | `spotify-profile` | Retrieve Spotify public profile |
| `GET` | `/spotify/profile/followers` | `spotify-profile-followers` | Retrieve Spotify public profile followers |
| `GET` | `/spotify/profile/playlists` | `spotify-profile-playlists` | Retrieve Spotify public profile playlists |
| `GET` | `/spotify/profiles/search` | `spotify-profiles-search` | Search Spotify profiles |
| `GET` | `/spotify/search` | `spotify-search` | Search Spotify catalog |
| `GET` | `/spotify/section` | `spotify-section` | Retrieve Spotify browse section |
| `GET` | `/spotify/shows/search` | `spotify-shows-search` | Search Spotify shows |
| `GET` | `/spotify/track` | `spotify-track` | Retrieve Spotify track details |
| `GET` | `/spotify/track/recommended` | `spotify-track-recommended` | Retrieve Spotify recommended tracks |
| `GET` | `/spotify/track/similar-albums` | `spotify-track-similar-albums` | Retrieve Spotify track similar albums |
| `GET` | `/spotify/tracks/search` | `spotify-tracks-search` | Search Spotify tracks |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
