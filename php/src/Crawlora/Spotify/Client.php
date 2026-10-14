<?php

declare(strict_types=1);

namespace Crawlora\Spotify;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'spotify';
    public const VERSION = '0.2.0';
    public const OPERATION_COUNT = 38;
    public const OPERATION_IDS = ["spotify-album", "spotify-album-tracks", "spotify-albums-search", "spotify-artist", "spotify-artist-albums", "spotify-artist-playlists", "spotify-artist-related", "spotify-artists-search", "spotify-audiobook", "spotify-audiobook-chapters", "spotify-audiobooks-search", "spotify-chapter", "spotify-episodes-search", "spotify-featured-charts-by-country", "spotify-genre", "spotify-home", "spotify-playlist", "spotify-playlists-search", "spotify-podcasts-categories", "spotify-podcasts-charts", "spotify-podcasts-episode", "spotify-podcasts-home", "spotify-podcasts-search", "spotify-podcasts-show", "spotify-podcasts-show-episodes", "spotify-podcasts-show-recommendations", "spotify-popular-by-country", "spotify-profile", "spotify-profile-followers", "spotify-profile-playlists", "spotify-profiles-search", "spotify-search", "spotify-section", "spotify-shows-search", "spotify-track", "spotify-track-recommended", "spotify-track-similar-albums", "spotify-tracks-search"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"spotify-album": {"bodyParam": null, "bodyRequired": false, "id": "spotify-album", "method": "GET", "params": [{"description": "Spotify album URI or open.spotify.com album URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:album:4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Spotify album ID", "in": "query", "name": "id", "type": "string", "x-example": "4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Track offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Track limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/album", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-album-tracks": {"bodyParam": null, "bodyRequired": false, "id": "spotify-album-tracks", "method": "GET", "params": [{"description": "Spotify album URI or open.spotify.com album URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:album:4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Spotify album ID", "in": "query", "name": "id", "type": "string", "x-example": "4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Track offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Track limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/album/tracks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-albums-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-albums-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Album result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/albums/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-artist": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}], "path": "/spotify/artist", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-artist-albums": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist-albums", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}, {"description": "album, single, compilation, appears_on, or all", "enum": ["album", "single", "compilation", "appears_on", "all"], "in": "query", "name": "type", "type": "string", "x-example": "album"}, {"description": "date_desc, date_asc, name_asc, or name_desc", "enum": ["date_desc", "date_asc", "name_asc", "name_desc"], "in": "query", "name": "order", "type": "string", "x-example": "date_desc"}, {"description": "Offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/artist/albums", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"enum": ["album", "single", "compilation", "appears_on", "all"], "in": "query", "name": "type", "type": "string"}, {"enum": ["date_desc", "date_asc", "name_asc", "name_desc"], "in": "query", "name": "order", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-artist-playlists": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist-playlists", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}], "path": "/spotify/artist/playlists", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-artist-related": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist-related", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}], "path": "/spotify/artist/related", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-artists-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artists-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/artists/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-audiobook": {"bodyParam": null, "bodyRequired": false, "id": "spotify-audiobook", "method": "GET", "params": [{"description": "Spotify audiobook/show URI or open.spotify.com show URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:76GTo4lM62dFR11VuALF01"}, {"description": "Spotify show ID", "in": "query", "name": "id", "type": "string", "x-example": "76GTo4lM62dFR11VuALF01"}], "path": "/spotify/audiobook", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-audiobook-chapters": {"bodyParam": null, "bodyRequired": false, "id": "spotify-audiobook-chapters", "method": "GET", "params": [{"description": "Spotify audiobook/show URI or open.spotify.com show URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:76GTo4lM62dFR11VuALF01"}, {"description": "Spotify show ID", "in": "query", "name": "id", "type": "string", "x-example": "76GTo4lM62dFR11VuALF01"}, {"description": "Chapter offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Chapter limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/spotify/audiobook/chapters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-audiobooks-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-audiobooks-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Audiobook result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook results", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": true}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/audiobooks/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-chapter": {"bodyParam": null, "bodyRequired": false, "id": "spotify-chapter", "method": "GET", "params": [{"description": "Spotify chapter or episode URI/URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:episode:2C2Y5kNq7qCVOVhbA0G3os"}, {"description": "Spotify chapter/episode ID", "in": "query", "name": "id", "type": "string", "x-example": "2C2Y5kNq7qCVOVhbA0G3os"}], "path": "/spotify/chapter", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-episodes-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-episodes-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/episodes/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-featured-charts-by-country": {"bodyParam": null, "bodyRequired": false, "id": "spotify-featured-charts-by-country", "method": "GET", "params": [{"description": "Two-letter Spotify popular-in country code", "in": "query", "name": "country_code", "type": "string", "x-example": "id"}, {"description": "Country hub content ID. Allowed: CHARTS, POPULAR_ALBUMS, POPULAR_ARTISTS, TRENDING_SONGS", "enum": ["CHARTS", "POPULAR_ALBUMS", "POPULAR_ARTISTS", "TRENDING_SONGS"], "in": "query", "name": "content_id", "type": "string", "x-example": "CHARTS"}], "path": "/spotify/featured-charts-by-country", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "type": "string"}, {"enum": ["CHARTS", "POPULAR_ALBUMS", "POPULAR_ARTISTS", "TRENDING_SONGS"], "in": "query", "name": "content_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-genre": {"bodyParam": null, "bodyRequired": false, "id": "spotify-genre", "method": "GET", "params": [{"description": "Spotify genre or page URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:page:0JQ5DAB3zgCauRwnvdEQjJ"}, {"description": "Page pagination offset", "in": "query", "name": "page_offset", "type": "integer", "x-example": 0}, {"description": "Page pagination limit, clamped to 1-50", "in": "query", "name": "page_limit", "type": "integer", "x-example": 10}, {"description": "Section pagination offset", "in": "query", "name": "section_offset", "type": "integer", "x-example": 0}, {"description": "Section pagination limit, clamped to 1-50", "in": "query", "name": "section_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/genre", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "page_offset", "type": "integer"}, {"in": "query", "name": "page_limit", "type": "integer"}, {"in": "query", "name": "section_offset", "type": "integer"}, {"in": "query", "name": "section_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-home": {"bodyParam": null, "bodyRequired": false, "id": "spotify-home", "method": "GET", "params": [{"description": "IANA time zone used by Spotify home personalization", "in": "query", "name": "time_zone", "type": "string", "x-example": "Asia/Shanghai"}, {"description": "Optional Spotify session token. A random UUID is generated when omitted", "in": "query", "name": "sp_t", "type": "string", "x-example": "00000000-0000-4000-8000-000000000000"}, {"description": "Optional Spotify home facet", "in": "query", "name": "facet", "type": "string", "x-example": ""}, {"description": "Per-section item limit, clamped to 1-50", "in": "query", "name": "section_items_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "time_zone", "type": "string"}, {"in": "query", "name": "sp_t", "type": "string"}, {"in": "query", "name": "facet", "type": "string"}, {"in": "query", "name": "section_items_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-playlist": {"bodyParam": null, "bodyRequired": false, "id": "spotify-playlist", "method": "GET", "params": [{"description": "Spotify playlist URI or open.spotify.com playlist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:playlist:37i9dQZEVXbLwpL8TjsxOG"}, {"description": "Spotify playlist ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "37i9dQZEVXbLwpL8TjsxOG"}, {"description": "Playlist item offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Playlist item limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 25}, {"description": "Enable watch feed entrypoint", "in": "query", "name": "enable_watch_feed_entrypoint", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/playlist", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "enable_watch_feed_entrypoint", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-playlists-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-playlists-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Playlist result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/playlists/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-categories": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-categories", "method": "GET", "params": [{"description": "Spotify podcast categories page URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:page:0JQ5DArNBzkmxXHCqFLx2U"}, {"description": "Page pagination offset", "in": "query", "name": "page_offset", "type": "integer", "x-example": 0}, {"description": "Page pagination limit, clamped to 1-50", "in": "query", "name": "page_limit", "type": "integer", "x-example": 10}, {"description": "Section pagination offset", "in": "query", "name": "section_offset", "type": "integer", "x-example": 0}, {"description": "Section pagination limit, clamped to 1-50", "in": "query", "name": "section_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "page_offset", "type": "integer"}, {"in": "query", "name": "page_limit", "type": "integer"}, {"in": "query", "name": "section_offset", "type": "integer"}, {"in": "query", "name": "section_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-charts": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-charts", "method": "GET", "params": [{"description": "Chart slug. Allowed: top-podcasts, top-episodes, trending, arts, business, comedy, education, fiction, health-fitness, history, leisure, music, news, religion-spirituality, science, society-culture, sports, technology, true-crime, tv-film", "enum": ["top-podcasts", "top-episodes", "trending", "arts", "business", "comedy", "education", "fiction", "health-fitness", "history", "leisure", "music", "news", "religion-spirituality", "science", "society-culture", "sports", "technology", "true-crime", "tv-film"], "in": "query", "name": "chart", "type": "string", "x-example": "religion-spirituality"}, {"description": "Two-letter region code. Allowed: ar, au, at, br, ca, cl, co, dk, fi, fr, de, in, id, ie, it, jp, mx, nz, no, ph, pl, es, se, nl, gb, us", "enum": ["ar", "au", "at", "br", "ca", "cl", "co", "dk", "fi", "fr", "de", "in", "id", "ie", "it", "jp", "mx", "nz", "no", "ph", "pl", "es", "se", "nl", "gb", "us"], "in": "query", "name": "region", "type": "string", "x-example": "us"}, {"description": "Result limit, clamped to 1-100", "in": "query", "name": "limit", "type": "integer", "x-example": 100}], "path": "/spotify-podcasts/charts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["top-podcasts", "top-episodes", "trending", "arts", "business", "comedy", "education", "fiction", "health-fitness", "history", "leisure", "music", "news", "religion-spirituality", "science", "society-culture", "sports", "technology", "true-crime", "tv-film"], "in": "query", "name": "chart", "type": "string"}, {"enum": ["ar", "au", "at", "br", "ca", "cl", "co", "dk", "fi", "fr", "de", "in", "id", "ie", "it", "jp", "mx", "nz", "no", "ph", "pl", "es", "se", "nl", "gb", "us"], "in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-episode": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-episode", "method": "GET", "params": [{"description": "Spotify episode URI or open.spotify.com episode URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:episode:2C2Y5kNq7qCVOVhbA0G3os"}, {"description": "Spotify episode ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "2C2Y5kNq7qCVOVhbA0G3os"}], "path": "/spotify-podcasts/episode", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-home": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-home", "method": "GET", "params": [{"description": "Spotify page or genre URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:genre:podcasts-web"}, {"description": "Page pagination offset", "in": "query", "name": "page_offset", "type": "integer", "x-example": 0}, {"description": "Page pagination limit, clamped to 1-50", "in": "query", "name": "page_limit", "type": "integer", "x-example": 10}, {"description": "Section pagination offset", "in": "query", "name": "section_offset", "type": "integer", "x-example": 0}, {"description": "Section pagination limit, clamped to 1-50", "in": "query", "name": "section_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "page_offset", "type": "integer"}, {"in": "query", "name": "page_limit", "type": "integer"}, {"in": "query", "name": "section_offset", "type": "integer"}, {"in": "query", "name": "section_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-search", "method": "GET", "params": [{"description": "Podcast search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "chatgpt"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include audiobooks", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-show": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-show", "method": "GET", "params": [{"description": "Spotify show URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:1QQJ7FElLE0K6CIfZNCxU4"}, {"description": "Include content capability trait", "in": "query", "name": "include_content_capability_trait", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/show", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "include_content_capability_trait", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-show-episodes": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-show-episodes", "method": "GET", "params": [{"description": "Spotify show URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:1QQJ7FElLE0K6CIfZNCxU4"}, {"description": "Episode offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Episode limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/show/episodes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-show-recommendations": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-show-recommendations", "method": "GET", "params": [{"description": "Spotify show URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:1QQJ7FElLE0K6CIfZNCxU4"}], "path": "/spotify-podcasts/show/recommendations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-popular-by-country": {"bodyParam": null, "bodyRequired": false, "id": "spotify-popular-by-country", "method": "GET", "params": [{"description": "Two-letter Spotify popular-in country code", "in": "query", "name": "country_code", "type": "string", "x-example": "us"}], "path": "/spotify/popular-by-country", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-profile": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profile", "method": "GET", "params": [{"description": "Spotify username", "in": "query", "name": "username", "type": "string", "x-example": "spotify"}, {"description": "Spotify user URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:user:spotify"}, {"description": "open.spotify.com user URL", "in": "query", "name": "url", "type": "string", "x-example": "https://open.spotify.com/user/spotify"}, {"description": "Embedded public playlist limit, clamped to 0-50", "in": "query", "name": "playlist_limit", "type": "integer", "x-example": 10}, {"description": "Recently played artist limit, clamped to 0-50", "in": "query", "name": "artist_limit", "type": "integer", "x-example": 10}, {"description": "Embedded episode limit, clamped to 0-50", "in": "query", "name": "episode_limit", "type": "integer", "x-example": 0}], "path": "/spotify/profile", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "type": "string"}, {"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "playlist_limit", "type": "integer"}, {"in": "query", "name": "artist_limit", "type": "integer"}, {"in": "query", "name": "episode_limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-profile-followers": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profile-followers", "method": "GET", "params": [{"description": "Spotify username", "in": "query", "name": "username", "type": "string", "x-example": "spotify"}, {"description": "Spotify user URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:user:spotify"}, {"description": "open.spotify.com user URL", "in": "query", "name": "url", "type": "string", "x-example": "https://open.spotify.com/user/spotify"}, {"description": "Follower offset applied locally", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Follower limit, clamped to 1-200", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/profile/followers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "type": "string"}, {"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-profile-playlists": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profile-playlists", "method": "GET", "params": [{"description": "Spotify username", "in": "query", "name": "username", "type": "string", "x-example": "spotify"}, {"description": "Spotify user URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:user:spotify"}, {"description": "open.spotify.com user URL", "in": "query", "name": "url", "type": "string", "x-example": "https://open.spotify.com/user/spotify"}, {"description": "Playlist offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Playlist limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/profile/playlists", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "type": "string"}, {"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-profiles-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profiles-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Profile result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/profiles/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit per section, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 5}, {"description": "Include audiobook results", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include artist concert availability fields", "in": "query", "name": "include_artist_has_concerts_field", "type": "boolean", "x-example": false}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": true}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}, {"description": "Treat the search term as a prefix", "in": "query", "name": "is_prefix", "type": "boolean", "x-example": false}], "path": "/spotify/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_artist_has_concerts_field", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}, {"in": "query", "name": "is_prefix", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-section": {"bodyParam": null, "bodyRequired": false, "id": "spotify-section", "method": "GET", "params": [{"description": "Spotify section URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:section:0JQ5IMCbQBLqNPkcmYxQPQ"}, {"description": "Section item offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Section item limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/section", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-shows-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-shows-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/shows/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-track": {"bodyParam": null, "bodyRequired": false, "id": "spotify-track", "method": "GET", "params": [{"description": "Spotify track URI or open.spotify.com track URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:track:4vGg44GdCw3X8i8r01XJH0"}, {"description": "Spotify track ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "4vGg44GdCw3X8i8r01XJH0"}], "path": "/spotify/track", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-track-recommended": {"bodyParam": null, "bodyRequired": false, "id": "spotify-track-recommended", "method": "GET", "params": [{"description": "Spotify track URI or open.spotify.com track URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:track:4vGg44GdCw3X8i8r01XJH0"}, {"description": "Spotify track ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "4vGg44GdCw3X8i8r01XJH0"}, {"description": "Recommendation limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 5}], "path": "/spotify/track/recommended", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-track-similar-albums": {"bodyParam": null, "bodyRequired": false, "id": "spotify-track-similar-albums", "method": "GET", "params": [{"description": "Spotify track URI or open.spotify.com track URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:track:4vGg44GdCw3X8i8r01XJH0"}, {"description": "Spotify track ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "4vGg44GdCw3X8i8r01XJH0"}, {"description": "Album limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}, {"description": "Request albums-only recommendations", "in": "query", "name": "albums_only", "type": "boolean", "x-example": true}], "path": "/spotify/track/similar-albums", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "albums_only", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-tracks-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-tracks-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Track result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/tracks/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-spotify-php/0.2.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function podcasts_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-categories", $params, $responseType);
    }
    public function podcasts_charts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-charts", $params, $responseType);
    }
    public function podcasts_episode(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-episode", $params, $responseType);
    }
    public function podcasts_home(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-home", $params, $responseType);
    }
    public function podcasts_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-search", $params, $responseType);
    }
    public function podcasts_show(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-show", $params, $responseType);
    }
    public function podcasts_show_episodes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-show-episodes", $params, $responseType);
    }
    public function podcasts_show_recommendations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-podcasts-show-recommendations", $params, $responseType);
    }
    public function album(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-album", $params, $responseType);
    }
    public function album_tracks(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-album-tracks", $params, $responseType);
    }
    public function albums_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-albums-search", $params, $responseType);
    }
    public function artist(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-artist", $params, $responseType);
    }
    public function artist_albums(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-artist-albums", $params, $responseType);
    }
    public function artist_playlists(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-artist-playlists", $params, $responseType);
    }
    public function artist_related(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-artist-related", $params, $responseType);
    }
    public function artists_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-artists-search", $params, $responseType);
    }
    public function audiobook(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-audiobook", $params, $responseType);
    }
    public function audiobook_chapters(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-audiobook-chapters", $params, $responseType);
    }
    public function audiobooks_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-audiobooks-search", $params, $responseType);
    }
    public function chapter(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-chapter", $params, $responseType);
    }
    public function episodes_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-episodes-search", $params, $responseType);
    }
    public function featured_charts_by_country(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-featured-charts-by-country", $params, $responseType);
    }
    public function genre(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-genre", $params, $responseType);
    }
    public function home(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-home", $params, $responseType);
    }
    public function playlist(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-playlist", $params, $responseType);
    }
    public function playlists_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-playlists-search", $params, $responseType);
    }
    public function popular_by_country(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-popular-by-country", $params, $responseType);
    }
    public function profile(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-profile", $params, $responseType);
    }
    public function profile_followers(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-profile-followers", $params, $responseType);
    }
    public function profile_playlists(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-profile-playlists", $params, $responseType);
    }
    public function profiles_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-profiles-search", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-search", $params, $responseType);
    }
    public function section(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-section", $params, $responseType);
    }
    public function shows_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-shows-search", $params, $responseType);
    }
    public function track(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-track", $params, $responseType);
    }
    public function track_recommended(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-track-recommended", $params, $responseType);
    }
    public function track_similar_albums(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-track-similar-albums", $params, $responseType);
    }
    public function tracks_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("spotify-tracks-search", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
