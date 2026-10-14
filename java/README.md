# Crawlora Spotify API client for Java

The official Java client for Crawlora's hosted Spotify API. It exposes 38 endpoints covering search, tracks, albums, artists, playlists, profiles, audiobooks, charts, and podcast shows and episodes. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-spotify</artifactId>
  <version>0.2.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-java-console) to get an API key.

```java
import net.crawlora.spotify.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("q", "daft punk")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Spotify API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-spotify/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-spotify)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-java-api-docs)
