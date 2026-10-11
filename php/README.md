# Crawlora Spotify API client for PHP (`crawlora/spotify`)

This PHP package calls Crawlora's hosted Spotify API at `https://api.crawlora.net/api/v1`. It exposes 38 endpoints covering search, tracks, albums, artists, playlists, profiles, audiobooks, charts, and podcast shows and episodes. It does not call or scrape Spotify directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/spotify
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Spotify\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("spotify-search", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 38 API operations.

## Supported Spotify API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-spotify/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-spotify). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-spotify/blob/main/docs/usage.md).
