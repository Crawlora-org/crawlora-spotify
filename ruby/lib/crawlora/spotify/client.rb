require "json"
require "net/http"
require "uri"

module Crawlora
  module Spotify
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"spotify-album": {"bodyParam": null, "bodyRequired": false, "id": "spotify-album", "method": "GET", "params": [{"description": "Spotify album URI or open.spotify.com album URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:album:4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Spotify album ID", "in": "query", "name": "id", "type": "string", "x-example": "4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Track offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Track limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/album", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-album-tracks": {"bodyParam": null, "bodyRequired": false, "id": "spotify-album-tracks", "method": "GET", "params": [{"description": "Spotify album URI or open.spotify.com album URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:album:4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Spotify album ID", "in": "query", "name": "id", "type": "string", "x-example": "4aawyAB9vmqN3uQ7FjRGTy"}, {"description": "Track offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Track limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/album/tracks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-albums-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-albums-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Album result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/albums/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-artist": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}], "path": "/spotify/artist", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-artist-albums": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist-albums", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}, {"description": "album, single, compilation, appears_on, or all", "enum": ["album", "single", "compilation", "appears_on", "all"], "in": "query", "name": "type", "type": "string", "x-example": "album"}, {"description": "date_desc, date_asc, name_asc, or name_desc", "enum": ["date_desc", "date_asc", "name_asc", "name_desc"], "in": "query", "name": "order", "type": "string", "x-example": "date_desc"}, {"description": "Offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/artist/albums", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"enum": ["album", "single", "compilation", "appears_on", "all"], "in": "query", "name": "type", "type": "string"}, {"enum": ["date_desc", "date_asc", "name_asc", "name_desc"], "in": "query", "name": "order", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-artist-playlists": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist-playlists", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}], "path": "/spotify/artist/playlists", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-artist-related": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artist-related", "method": "GET", "params": [{"description": "Spotify artist URI or open.spotify.com artist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:artist:0TnOYISbd1XYRBk9myaseg"}, {"description": "Spotify artist ID", "in": "query", "name": "id", "type": "string", "x-example": "0TnOYISbd1XYRBk9myaseg"}], "path": "/spotify/artist/related", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-artists-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-artists-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/artists/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-audiobook": {"bodyParam": null, "bodyRequired": false, "id": "spotify-audiobook", "method": "GET", "params": [{"description": "Spotify audiobook/show URI or open.spotify.com show URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:76GTo4lM62dFR11VuALF01"}, {"description": "Spotify show ID", "in": "query", "name": "id", "type": "string", "x-example": "76GTo4lM62dFR11VuALF01"}], "path": "/spotify/audiobook", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-audiobook-chapters": {"bodyParam": null, "bodyRequired": false, "id": "spotify-audiobook-chapters", "method": "GET", "params": [{"description": "Spotify audiobook/show URI or open.spotify.com show URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:76GTo4lM62dFR11VuALF01"}, {"description": "Spotify show ID", "in": "query", "name": "id", "type": "string", "x-example": "76GTo4lM62dFR11VuALF01"}, {"description": "Chapter offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Chapter limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/spotify/audiobook/chapters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-audiobooks-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-audiobooks-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Audiobook result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook results", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": true}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/audiobooks/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-chapter": {"bodyParam": null, "bodyRequired": false, "id": "spotify-chapter", "method": "GET", "params": [{"description": "Spotify chapter or episode URI/URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:episode:2C2Y5kNq7qCVOVhbA0G3os"}, {"description": "Spotify chapter/episode ID", "in": "query", "name": "id", "type": "string", "x-example": "2C2Y5kNq7qCVOVhbA0G3os"}], "path": "/spotify/chapter", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-episodes-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-episodes-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/episodes/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-featured-charts-by-country": {"bodyParam": null, "bodyRequired": false, "id": "spotify-featured-charts-by-country", "method": "GET", "params": [{"description": "Two-letter Spotify popular-in country code", "in": "query", "name": "country_code", "type": "string", "x-example": "id"}, {"description": "Country hub content ID. Allowed: CHARTS, POPULAR_ALBUMS, POPULAR_ARTISTS, TRENDING_SONGS", "enum": ["CHARTS", "POPULAR_ALBUMS", "POPULAR_ARTISTS", "TRENDING_SONGS"], "in": "query", "name": "content_id", "type": "string", "x-example": "CHARTS"}], "path": "/spotify/featured-charts-by-country", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "type": "string"}, {"enum": ["CHARTS", "POPULAR_ALBUMS", "POPULAR_ARTISTS", "TRENDING_SONGS"], "in": "query", "name": "content_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-genre": {"bodyParam": null, "bodyRequired": false, "id": "spotify-genre", "method": "GET", "params": [{"description": "Spotify genre or page URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:page:0JQ5DAB3zgCauRwnvdEQjJ"}, {"description": "Page pagination offset", "in": "query", "name": "page_offset", "type": "integer", "x-example": 0}, {"description": "Page pagination limit, clamped to 1-50", "in": "query", "name": "page_limit", "type": "integer", "x-example": 10}, {"description": "Section pagination offset", "in": "query", "name": "section_offset", "type": "integer", "x-example": 0}, {"description": "Section pagination limit, clamped to 1-50", "in": "query", "name": "section_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/genre", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "page_offset", "type": "integer"}, {"in": "query", "name": "page_limit", "type": "integer"}, {"in": "query", "name": "section_offset", "type": "integer"}, {"in": "query", "name": "section_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-home": {"bodyParam": null, "bodyRequired": false, "id": "spotify-home", "method": "GET", "params": [{"description": "IANA time zone used by Spotify home personalization", "in": "query", "name": "time_zone", "type": "string", "x-example": "Asia/Shanghai"}, {"description": "Optional Spotify session token. A random UUID is generated when omitted", "in": "query", "name": "sp_t", "type": "string", "x-example": "00000000-0000-4000-8000-000000000000"}, {"description": "Optional Spotify home facet", "in": "query", "name": "facet", "type": "string", "x-example": ""}, {"description": "Per-section item limit, clamped to 1-50", "in": "query", "name": "section_items_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "time_zone", "type": "string"}, {"in": "query", "name": "sp_t", "type": "string"}, {"in": "query", "name": "facet", "type": "string"}, {"in": "query", "name": "section_items_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-playlist": {"bodyParam": null, "bodyRequired": false, "id": "spotify-playlist", "method": "GET", "params": [{"description": "Spotify playlist URI or open.spotify.com playlist URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:playlist:37i9dQZEVXbLwpL8TjsxOG"}, {"description": "Spotify playlist ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "37i9dQZEVXbLwpL8TjsxOG"}, {"description": "Playlist item offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Playlist item limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 25}, {"description": "Enable watch feed entrypoint", "in": "query", "name": "enable_watch_feed_entrypoint", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/playlist", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "enable_watch_feed_entrypoint", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-playlists-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-playlists-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Playlist result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/playlists/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-categories": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-categories", "method": "GET", "params": [{"description": "Spotify podcast categories page URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:page:0JQ5DArNBzkmxXHCqFLx2U"}, {"description": "Page pagination offset", "in": "query", "name": "page_offset", "type": "integer", "x-example": 0}, {"description": "Page pagination limit, clamped to 1-50", "in": "query", "name": "page_limit", "type": "integer", "x-example": 10}, {"description": "Section pagination offset", "in": "query", "name": "section_offset", "type": "integer", "x-example": 0}, {"description": "Section pagination limit, clamped to 1-50", "in": "query", "name": "section_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "page_offset", "type": "integer"}, {"in": "query", "name": "page_limit", "type": "integer"}, {"in": "query", "name": "section_offset", "type": "integer"}, {"in": "query", "name": "section_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-charts": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-charts", "method": "GET", "params": [{"description": "Chart slug. Allowed: top-podcasts, top-episodes, trending, arts, business, comedy, education, fiction, health-fitness, history, leisure, music, news, religion-spirituality, science, society-culture, sports, technology, true-crime, tv-film", "enum": ["top-podcasts", "top-episodes", "trending", "arts", "business", "comedy", "education", "fiction", "health-fitness", "history", "leisure", "music", "news", "religion-spirituality", "science", "society-culture", "sports", "technology", "true-crime", "tv-film"], "in": "query", "name": "chart", "type": "string", "x-example": "religion-spirituality"}, {"description": "Two-letter region code. Allowed: ar, au, at, br, ca, cl, co, dk, fi, fr, de, in, id, ie, it, jp, mx, nz, no, ph, pl, es, se, nl, gb, us", "enum": ["ar", "au", "at", "br", "ca", "cl", "co", "dk", "fi", "fr", "de", "in", "id", "ie", "it", "jp", "mx", "nz", "no", "ph", "pl", "es", "se", "nl", "gb", "us"], "in": "query", "name": "region", "type": "string", "x-example": "us"}, {"description": "Result limit, clamped to 1-100", "in": "query", "name": "limit", "type": "integer", "x-example": 100}], "path": "/spotify-podcasts/charts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["top-podcasts", "top-episodes", "trending", "arts", "business", "comedy", "education", "fiction", "health-fitness", "history", "leisure", "music", "news", "religion-spirituality", "science", "society-culture", "sports", "technology", "true-crime", "tv-film"], "in": "query", "name": "chart", "type": "string"}, {"enum": ["ar", "au", "at", "br", "ca", "cl", "co", "dk", "fi", "fr", "de", "in", "id", "ie", "it", "jp", "mx", "nz", "no", "ph", "pl", "es", "se", "nl", "gb", "us"], "in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-episode": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-episode", "method": "GET", "params": [{"description": "Spotify episode URI or open.spotify.com episode URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:episode:2C2Y5kNq7qCVOVhbA0G3os"}, {"description": "Spotify episode ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "2C2Y5kNq7qCVOVhbA0G3os"}], "path": "/spotify-podcasts/episode", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-home": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-home", "method": "GET", "params": [{"description": "Spotify page or genre URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:genre:podcasts-web"}, {"description": "Page pagination offset", "in": "query", "name": "page_offset", "type": "integer", "x-example": 0}, {"description": "Page pagination limit, clamped to 1-50", "in": "query", "name": "page_limit", "type": "integer", "x-example": 10}, {"description": "Section pagination offset", "in": "query", "name": "section_offset", "type": "integer", "x-example": 0}, {"description": "Section pagination limit, clamped to 1-50", "in": "query", "name": "section_limit", "type": "integer", "x-example": 10}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/home", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "page_offset", "type": "integer"}, {"in": "query", "name": "page_limit", "type": "integer"}, {"in": "query", "name": "section_offset", "type": "integer"}, {"in": "query", "name": "section_limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-search", "method": "GET", "params": [{"description": "Podcast search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "chatgpt"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include audiobooks", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-show": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-show", "method": "GET", "params": [{"description": "Spotify show URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:1QQJ7FElLE0K6CIfZNCxU4"}, {"description": "Include content capability trait", "in": "query", "name": "include_content_capability_trait", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/show", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "include_content_capability_trait", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-show-episodes": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-show-episodes", "method": "GET", "params": [{"description": "Spotify show URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:1QQJ7FElLE0K6CIfZNCxU4"}, {"description": "Episode offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Episode limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify-podcasts/show/episodes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-podcasts-show-recommendations": {"bodyParam": null, "bodyRequired": false, "id": "spotify-podcasts-show-recommendations", "method": "GET", "params": [{"description": "Spotify show URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:show:1QQJ7FElLE0K6CIfZNCxU4"}], "path": "/spotify-podcasts/show/recommendations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-popular-by-country": {"bodyParam": null, "bodyRequired": false, "id": "spotify-popular-by-country", "method": "GET", "params": [{"description": "Two-letter Spotify popular-in country code", "in": "query", "name": "country_code", "type": "string", "x-example": "us"}], "path": "/spotify/popular-by-country", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-profile": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profile", "method": "GET", "params": [{"description": "Spotify username", "in": "query", "name": "username", "type": "string", "x-example": "spotify"}, {"description": "Spotify user URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:user:spotify"}, {"description": "open.spotify.com user URL", "in": "query", "name": "url", "type": "string", "x-example": "https://open.spotify.com/user/spotify"}, {"description": "Embedded public playlist limit, clamped to 0-50", "in": "query", "name": "playlist_limit", "type": "integer", "x-example": 10}, {"description": "Recently played artist limit, clamped to 0-50", "in": "query", "name": "artist_limit", "type": "integer", "x-example": 10}, {"description": "Embedded episode limit, clamped to 0-50", "in": "query", "name": "episode_limit", "type": "integer", "x-example": 0}], "path": "/spotify/profile", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "type": "string"}, {"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "playlist_limit", "type": "integer"}, {"in": "query", "name": "artist_limit", "type": "integer"}, {"in": "query", "name": "episode_limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-profile-followers": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profile-followers", "method": "GET", "params": [{"description": "Spotify username", "in": "query", "name": "username", "type": "string", "x-example": "spotify"}, {"description": "Spotify user URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:user:spotify"}, {"description": "open.spotify.com user URL", "in": "query", "name": "url", "type": "string", "x-example": "https://open.spotify.com/user/spotify"}, {"description": "Follower offset applied locally", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Follower limit, clamped to 1-200", "in": "query", "name": "limit", "type": "integer", "x-example": 50}], "path": "/spotify/profile/followers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "type": "string"}, {"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-profile-playlists": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profile-playlists", "method": "GET", "params": [{"description": "Spotify username", "in": "query", "name": "username", "type": "string", "x-example": "spotify"}, {"description": "Spotify user URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:user:spotify"}, {"description": "open.spotify.com user URL", "in": "query", "name": "url", "type": "string", "x-example": "https://open.spotify.com/user/spotify"}, {"description": "Playlist offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Playlist limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/profile/playlists", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "type": "string"}, {"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-profiles-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-profiles-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Profile result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 30}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/profiles/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit per section, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 5}, {"description": "Include audiobook results", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include artist concert availability fields", "in": "query", "name": "include_artist_has_concerts_field", "type": "boolean", "x-example": false}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": true}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}, {"description": "Treat the search term as a prefix", "in": "query", "name": "is_prefix", "type": "boolean", "x-example": false}], "path": "/spotify/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_artist_has_concerts_field", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}, {"in": "query", "name": "is_prefix", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-section": {"bodyParam": null, "bodyRequired": false, "id": "spotify-section", "method": "GET", "params": [{"description": "Spotify section URI", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:section:0JQ5IMCbQBLqNPkcmYxQPQ"}, {"description": "Section item offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Section item limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/section", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-shows-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-shows-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}], "path": "/spotify/shows/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-track": {"bodyParam": null, "bodyRequired": false, "id": "spotify-track", "method": "GET", "params": [{"description": "Spotify track URI or open.spotify.com track URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:track:4vGg44GdCw3X8i8r01XJH0"}, {"description": "Spotify track ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "4vGg44GdCw3X8i8r01XJH0"}], "path": "/spotify/track", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}], "security": ["ApiKeyAuth"]}, "spotify-track-recommended": {"bodyParam": null, "bodyRequired": false, "id": "spotify-track-recommended", "method": "GET", "params": [{"description": "Spotify track URI or open.spotify.com track URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:track:4vGg44GdCw3X8i8r01XJH0"}, {"description": "Spotify track ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "4vGg44GdCw3X8i8r01XJH0"}, {"description": "Recommendation limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 5}], "path": "/spotify/track/recommended", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "spotify-track-similar-albums": {"bodyParam": null, "bodyRequired": false, "id": "spotify-track-similar-albums", "method": "GET", "params": [{"description": "Spotify track URI or open.spotify.com track URL", "in": "query", "name": "uri", "type": "string", "x-example": "spotify:track:4vGg44GdCw3X8i8r01XJH0"}, {"description": "Spotify track ID. Used when uri is omitted", "in": "query", "name": "id", "type": "string", "x-example": "4vGg44GdCw3X8i8r01XJH0"}, {"description": "Album limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 50}, {"description": "Request albums-only recommendations", "in": "query", "name": "albums_only", "type": "boolean", "x-example": true}], "path": "/spotify/track/similar-albums", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "uri", "type": "string"}, {"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "albums_only", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "spotify-tracks-search": {"bodyParam": null, "bodyRequired": false, "id": "spotify-tracks-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "hello"}, {"description": "Search offset", "in": "query", "name": "offset", "type": "integer", "x-example": 0}, {"description": "Track result limit, clamped to 1-50", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Top result limit, clamped to 1-50", "in": "query", "name": "number_of_top_results", "type": "integer", "x-example": 20}, {"description": "Include audiobook context where available", "in": "query", "name": "include_audiobooks", "type": "boolean", "x-example": true}, {"description": "Include pre-release results", "in": "query", "name": "include_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include album pre-release results", "in": "query", "name": "include_album_pre_releases", "type": "boolean", "x-example": false}, {"description": "Include authors", "in": "query", "name": "include_authors", "type": "boolean", "x-example": false}, {"description": "Include Spotify episode content ratings v2", "in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean", "x-example": false}], "path": "/spotify/tracks/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "number_of_top_results", "type": "integer"}, {"in": "query", "name": "include_audiobooks", "type": "boolean"}, {"in": "query", "name": "include_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_album_pre_releases", "type": "boolean"}, {"in": "query", "name": "include_authors", "type": "boolean"}, {"in": "query", "name": "include_episode_content_ratings_v2", "type": "boolean"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["spotify-album", "spotify-album-tracks", "spotify-albums-search", "spotify-artist", "spotify-artist-albums", "spotify-artist-playlists", "spotify-artist-related", "spotify-artists-search", "spotify-audiobook", "spotify-audiobook-chapters", "spotify-audiobooks-search", "spotify-chapter", "spotify-episodes-search", "spotify-featured-charts-by-country", "spotify-genre", "spotify-home", "spotify-playlist", "spotify-playlists-search", "spotify-podcasts-categories", "spotify-podcasts-charts", "spotify-podcasts-episode", "spotify-podcasts-home", "spotify-podcasts-search", "spotify-podcasts-show", "spotify-podcasts-show-episodes", "spotify-podcasts-show-recommendations", "spotify-popular-by-country", "spotify-profile", "spotify-profile-followers", "spotify-profile-playlists", "spotify-profiles-search", "spotify-search", "spotify-section", "spotify-shows-search", "spotify-track", "spotify-track-recommended", "spotify-track-similar-albums", "spotify-tracks-search"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-spotify-ruby/0.1.1", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('podcasts_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-categories', params, response_type: response_type)
      end
      define_method('podcasts_charts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-charts', params, response_type: response_type)
      end
      define_method('podcasts_episode') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-episode', params, response_type: response_type)
      end
      define_method('podcasts_home') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-home', params, response_type: response_type)
      end
      define_method('podcasts_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-search', params, response_type: response_type)
      end
      define_method('podcasts_show') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-show', params, response_type: response_type)
      end
      define_method('podcasts_show_episodes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-show-episodes', params, response_type: response_type)
      end
      define_method('podcasts_show_recommendations') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-podcasts-show-recommendations', params, response_type: response_type)
      end
      define_method('album') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-album', params, response_type: response_type)
      end
      define_method('album_tracks') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-album-tracks', params, response_type: response_type)
      end
      define_method('albums_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-albums-search', params, response_type: response_type)
      end
      define_method('artist') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-artist', params, response_type: response_type)
      end
      define_method('artist_albums') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-artist-albums', params, response_type: response_type)
      end
      define_method('artist_playlists') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-artist-playlists', params, response_type: response_type)
      end
      define_method('artist_related') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-artist-related', params, response_type: response_type)
      end
      define_method('artists_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-artists-search', params, response_type: response_type)
      end
      define_method('audiobook') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-audiobook', params, response_type: response_type)
      end
      define_method('audiobook_chapters') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-audiobook-chapters', params, response_type: response_type)
      end
      define_method('audiobooks_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-audiobooks-search', params, response_type: response_type)
      end
      define_method('chapter') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-chapter', params, response_type: response_type)
      end
      define_method('episodes_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-episodes-search', params, response_type: response_type)
      end
      define_method('featured_charts_by_country') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-featured-charts-by-country', params, response_type: response_type)
      end
      define_method('genre') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-genre', params, response_type: response_type)
      end
      define_method('home') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-home', params, response_type: response_type)
      end
      define_method('playlist') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-playlist', params, response_type: response_type)
      end
      define_method('playlists_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-playlists-search', params, response_type: response_type)
      end
      define_method('popular_by_country') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-popular-by-country', params, response_type: response_type)
      end
      define_method('profile') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-profile', params, response_type: response_type)
      end
      define_method('profile_followers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-profile-followers', params, response_type: response_type)
      end
      define_method('profile_playlists') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-profile-playlists', params, response_type: response_type)
      end
      define_method('profiles_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-profiles-search', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-search', params, response_type: response_type)
      end
      define_method('section') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-section', params, response_type: response_type)
      end
      define_method('shows_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-shows-search', params, response_type: response_type)
      end
      define_method('track') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-track', params, response_type: response_type)
      end
      define_method('track_recommended') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-track-recommended', params, response_type: response_type)
      end
      define_method('track_similar_albums') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-track-similar-albums', params, response_type: response_type)
      end
      define_method('tracks_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('spotify-tracks-search', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
