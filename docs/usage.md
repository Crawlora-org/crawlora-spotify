# Spotify client usage

The `@crawlora-org/spotify` and `crawlora-spotify` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Spotify locally; Crawlora is independent from and not endorsed by Spotify or its owners.

The package tracks the public API contract revision `sha256:f451f5340517c087f7a6f601dab3c1eef266bade0631f9b5d1b4455dd90c24c0` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 38 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `spotify` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `album` / `album` | `GET /spotify/album` | `uri` (query, optional), `id` (query, optional), `offset` (query, optional), `limit` (query, optional) | Retrieve Spotify album details |
| `albumsSearch` / `albums_search` | `GET /spotify/albums/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional), `number_of_top_results` (query, optional), `include_audiobooks` (query, optional), `include_pre_releases` (query, optional), `include_album_pre_releases` (query, optional), `include_authors` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Search Spotify albums |
| `albumTracks` / `album_tracks` | `GET /spotify/album/tracks` | `uri` (query, optional), `id` (query, optional), `offset` (query, optional), `limit` (query, optional) | Retrieve Spotify album tracks |
| `artist` / `artist` | `GET /spotify/artist` | `uri` (query, optional), `id` (query, optional) | Retrieve Spotify artist details |
| `artistAlbums` / `artist_albums` | `GET /spotify/artist/albums` | `uri` (query, optional), `id` (query, optional), `type` (query, optional; values: `album`, `single`, `compilation`, `appears_on`, `all`), `order` (query, optional; values: `date_desc`, `date_asc`, `name_asc`, `name_desc`), `offset` (query, optional), `limit` (query, optional) | Retrieve Spotify artist albums |
| `artistPlaylists` / `artist_playlists` | `GET /spotify/artist/playlists` | `uri` (query, optional), `id` (query, optional) | Retrieve Spotify artist playlists |
| `artistRelated` / `artist_related` | `GET /spotify/artist/related` | `uri` (query, optional), `id` (query, optional) | Retrieve Spotify related artists |
| `artistsSearch` / `artists_search` | `GET /spotify/artists/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional) | Search Spotify artists |
| `audiobook` / `audiobook` | `GET /spotify/audiobook` | `uri` (query, optional), `id` (query, optional) | Retrieve Spotify audiobook details |
| `audiobookChapters` / `audiobook_chapters` | `GET /spotify/audiobook/chapters` | `uri` (query, optional), `id` (query, optional), `offset` (query, optional), `limit` (query, optional) | Retrieve Spotify audiobook chapters |
| `audiobooksSearch` / `audiobooks_search` | `GET /spotify/audiobooks/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional), `number_of_top_results` (query, optional), `include_audiobooks` (query, optional), `include_pre_releases` (query, optional), `include_album_pre_releases` (query, optional), `include_authors` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Search Spotify audiobooks |
| `chapter` / `chapter` | `GET /spotify/chapter` | `uri` (query, optional), `id` (query, optional) | Retrieve Spotify audiobook chapter details |
| `episodesSearch` / `episodes_search` | `GET /spotify/episodes/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional) | Search Spotify episodes |
| `featuredChartsByCountry` / `featured_charts_by_country` | `GET /spotify/featured-charts-by-country` | `country_code` (query, optional), `content_id` (query, optional; values: `CHARTS`, `POPULAR_ALBUMS`, `POPULAR_ARTISTS`, `TRENDING_SONGS`) | Retrieve Spotify featured charts by country |
| `genre` / `genre` | `GET /spotify/genre` | `uri` (query, optional), `page_offset` (query, optional), `page_limit` (query, optional), `section_offset` (query, optional), `section_limit` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify genre page |
| `home` / `home` | `GET /spotify/home` | `time_zone` (query, optional), `sp_t` (query, optional), `facet` (query, optional), `section_items_limit` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify home sections |
| `playlist` / `playlist` | `GET /spotify/playlist` | `uri` (query, optional), `id` (query, optional), `offset` (query, optional), `limit` (query, optional), `enable_watch_feed_entrypoint` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify playlist details |
| `playlistsSearch` / `playlists_search` | `GET /spotify/playlists/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional), `number_of_top_results` (query, optional), `include_audiobooks` (query, optional), `include_pre_releases` (query, optional), `include_album_pre_releases` (query, optional), `include_authors` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Search Spotify playlists |
| `podcastsCategories` / `podcasts_categories` | `GET /spotify-podcasts/categories` | `uri` (query, optional), `page_offset` (query, optional), `page_limit` (query, optional), `section_offset` (query, optional), `section_limit` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify Podcasts categories |
| `podcastsCharts` / `podcasts_charts` | `GET /spotify-podcasts/charts` | `chart` (query, optional; values: `top-podcasts`, `top-episodes`, `trending`, `arts`, `business`, `comedy`, `education`, `fiction`, `health-fitness`, `history`, `leisure`, `music`, `news`, `religion-spirituality`, `science`, `society-culture`, `sports`, `technology`, `true-crime`, `tv-film`), `region` (query, optional; values: `ar`, `au`, `at`, `br`, `ca`, `cl`, `co`, `dk`, `fi`, `fr`, `de`, `in`, `id`, `ie`, `it`, `jp`, `mx`, `nz`, `no`, `ph`, `pl`, `es`, `se`, `nl`, `gb`, `us`), `limit` (query, optional) | Retrieve Spotify podcast charts |
| `podcastsEpisode` / `podcasts_episode` | `GET /spotify-podcasts/episode` | `uri` (query, optional), `id` (query, optional) | Retrieve Spotify podcast episode details |
| `podcastsHome` / `podcasts_home` | `GET /spotify-podcasts/home` | `uri` (query, optional), `page_offset` (query, optional), `page_limit` (query, optional), `section_offset` (query, optional), `section_limit` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify Podcasts home |
| `podcastsSearch` / `podcasts_search` | `GET /spotify-podcasts/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional), `number_of_top_results` (query, optional), `include_pre_releases` (query, optional), `include_album_pre_releases` (query, optional), `include_audiobooks` (query, optional), `include_authors` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Search Spotify Podcasts |
| `podcastsShow` / `podcasts_show` | `GET /spotify-podcasts/show` | `uri` (query, optional), `include_content_capability_trait` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify podcast show metadata |
| `podcastsShowEpisodes` / `podcasts_show_episodes` | `GET /spotify-podcasts/show/episodes` | `uri` (query, optional), `offset` (query, optional), `limit` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify podcast show episodes |
| `podcastsShowRecommendations` / `podcasts_show_recommendations` | `GET /spotify-podcasts/show/recommendations` | `uri` (query, optional) | Retrieve Spotify podcast recommendations |
| `popularByCountry` / `popular_by_country` | `GET /spotify/popular-by-country` | `country_code` (query, optional) | Retrieve Spotify popular by country |
| `profile` / `profile` | `GET /spotify/profile` | `username` (query, optional), `uri` (query, optional), `url` (query, optional), `playlist_limit` (query, optional), `artist_limit` (query, optional), `episode_limit` (query, optional) | Retrieve Spotify public profile |
| `profileFollowers` / `profile_followers` | `GET /spotify/profile/followers` | `username` (query, optional), `uri` (query, optional), `url` (query, optional), `offset` (query, optional), `limit` (query, optional) | Retrieve Spotify public profile followers |
| `profilePlaylists` / `profile_playlists` | `GET /spotify/profile/playlists` | `username` (query, optional), `uri` (query, optional), `url` (query, optional), `offset` (query, optional), `limit` (query, optional) | Retrieve Spotify public profile playlists |
| `profilesSearch` / `profiles_search` | `GET /spotify/profiles/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional), `number_of_top_results` (query, optional), `include_audiobooks` (query, optional), `include_pre_releases` (query, optional), `include_album_pre_releases` (query, optional), `include_authors` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Search Spotify profiles |
| `search` / `search` | `GET /spotify/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional), `number_of_top_results` (query, optional), `include_audiobooks` (query, optional), `include_artist_has_concerts_field` (query, optional), `include_pre_releases` (query, optional), `include_album_pre_releases` (query, optional), `include_authors` (query, optional), `include_episode_content_ratings_v2` (query, optional), `is_prefix` (query, optional) | Search Spotify catalog |
| `section` / `section` | `GET /spotify/section` | `uri` (query, optional), `offset` (query, optional), `limit` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Retrieve Spotify browse section |
| `showsSearch` / `shows_search` | `GET /spotify/shows/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional) | Search Spotify shows |
| `track` / `track` | `GET /spotify/track` | `uri` (query, optional), `id` (query, optional) | Retrieve Spotify track details |
| `trackRecommended` / `track_recommended` | `GET /spotify/track/recommended` | `uri` (query, optional), `id` (query, optional), `limit` (query, optional) | Retrieve Spotify recommended tracks |
| `trackSimilarAlbums` / `track_similar_albums` | `GET /spotify/track/similar-albums` | `uri` (query, optional), `id` (query, optional), `limit` (query, optional), `albums_only` (query, optional) | Retrieve Spotify track similar albums |
| `tracksSearch` / `tracks_search` | `GET /spotify/tracks/search` | `q` (query, required), `offset` (query, optional), `limit` (query, optional), `number_of_top_results` (query, optional), `include_audiobooks` (query, optional), `include_pre_releases` (query, optional), `include_album_pre_releases` (query, optional), `include_authors` (query, optional), `include_episode_content_ratings_v2` (query, optional) | Search Spotify tracks |

## Client forms

- JavaScript: import `SpotifyClient` (also exported as `Client`) from `@crawlora-org/spotify`; use `new SpotifyClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `SpotifyClient` (also exported as `Client`) from `crawlora_spotify`; use `with SpotifyClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncSpotifyClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
