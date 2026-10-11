# Spotify clients for Crawlora

Official Crawlora client packages for the hosted Spotify API. Access 38 API endpoints covering search, tracks, albums, artists, playlists, profiles, audiobooks, charts, and podcast shows and episodes from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape Spotify locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Spotify or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/spotify`](javascript/README.md)
- Python: [`crawlora-spotify`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-spotify`](go.mod)
- Ruby: [`crawlora-spotify`](ruby/README.md)
- Java: [`net.crawlora:crawlora-spotify:0.1.1`](java/README.md)
- PHP: [`crawlora/spotify`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=spotify-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 38 selected public Spotify API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
