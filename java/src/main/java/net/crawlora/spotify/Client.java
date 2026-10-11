package net.crawlora.spotify;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Spotify endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 38;
    public static final List<String> OPERATION_IDS = List.of(
            "spotify-album",
            "spotify-album-tracks",
            "spotify-albums-search",
            "spotify-artist",
            "spotify-artist-albums",
            "spotify-artist-playlists",
            "spotify-artist-related",
            "spotify-artists-search",
            "spotify-audiobook",
            "spotify-audiobook-chapters",
            "spotify-audiobooks-search",
            "spotify-chapter",
            "spotify-episodes-search",
            "spotify-featured-charts-by-country",
            "spotify-genre",
            "spotify-home",
            "spotify-playlist",
            "spotify-playlists-search",
            "spotify-podcasts-categories",
            "spotify-podcasts-charts",
            "spotify-podcasts-episode",
            "spotify-podcasts-home",
            "spotify-podcasts-search",
            "spotify-podcasts-show",
            "spotify-podcasts-show-episodes",
            "spotify-podcasts-show-recommendations",
            "spotify-popular-by-country",
            "spotify-profile",
            "spotify-profile-followers",
            "spotify-profile-playlists",
            "spotify-profiles-search",
            "spotify-search",
            "spotify-section",
            "spotify-shows-search",
            "spotify-track",
            "spotify-track-recommended",
            "spotify-track-similar-albums",
            "spotify-tracks-search"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("spotify-podcasts-categories", new Operation("spotify-podcasts-categories", "GET", "/spotify-podcasts/categories", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("page_offset", new Param("page_offset", "query", false, "integer", List.of(), "csv")), Map.entry("page_limit", new Param("page_limit", "query", false, "integer", List.of(), "csv")), Map.entry("section_offset", new Param("section_offset", "query", false, "integer", List.of(), "csv")), Map.entry("section_limit", new Param("section_limit", "query", false, "integer", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-podcasts-charts", new Operation("spotify-podcasts-charts", "GET", "/spotify-podcasts/charts", Map.ofEntries(Map.entry("chart", new Param("chart", "query", false, "string", List.of("top-podcasts", "top-episodes", "trending", "arts", "business", "comedy", "education", "fiction", "health-fitness", "history", "leisure", "music", "news", "religion-spirituality", "science", "society-culture", "sports", "technology", "true-crime", "tv-film"), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of("ar", "au", "at", "br", "ca", "cl", "co", "dk", "fi", "fr", "de", "in", "id", "ie", "it", "jp", "mx", "nz", "no", "ph", "pl", "es", "se", "nl", "gb", "us"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-podcasts-episode", new Operation("spotify-podcasts-episode", "GET", "/spotify-podcasts/episode", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-podcasts-home", new Operation("spotify-podcasts-home", "GET", "/spotify-podcasts/home", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("page_offset", new Param("page_offset", "query", false, "integer", List.of(), "csv")), Map.entry("page_limit", new Param("page_limit", "query", false, "integer", List.of(), "csv")), Map.entry("section_offset", new Param("section_offset", "query", false, "integer", List.of(), "csv")), Map.entry("section_limit", new Param("section_limit", "query", false, "integer", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-podcasts-search", new Operation("spotify-podcasts-search", "GET", "/spotify-podcasts/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("number_of_top_results", new Param("number_of_top_results", "query", false, "integer", List.of(), "csv")), Map.entry("include_pre_releases", new Param("include_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_album_pre_releases", new Param("include_album_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_audiobooks", new Param("include_audiobooks", "query", false, "boolean", List.of(), "csv")), Map.entry("include_authors", new Param("include_authors", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-podcasts-show", new Operation("spotify-podcasts-show", "GET", "/spotify-podcasts/show", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("include_content_capability_trait", new Param("include_content_capability_trait", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-podcasts-show-episodes", new Operation("spotify-podcasts-show-episodes", "GET", "/spotify-podcasts/show/episodes", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-podcasts-show-recommendations", new Operation("spotify-podcasts-show-recommendations", "GET", "/spotify-podcasts/show/recommendations", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-album", new Operation("spotify-album", "GET", "/spotify/album", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-album-tracks", new Operation("spotify-album-tracks", "GET", "/spotify/album/tracks", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-albums-search", new Operation("spotify-albums-search", "GET", "/spotify/albums/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("number_of_top_results", new Param("number_of_top_results", "query", false, "integer", List.of(), "csv")), Map.entry("include_audiobooks", new Param("include_audiobooks", "query", false, "boolean", List.of(), "csv")), Map.entry("include_pre_releases", new Param("include_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_album_pre_releases", new Param("include_album_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_authors", new Param("include_authors", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-artist", new Operation("spotify-artist", "GET", "/spotify/artist", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-artist-albums", new Operation("spotify-artist-albums", "GET", "/spotify/artist/albums", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("album", "single", "compilation", "appears_on", "all"), "csv")), Map.entry("order", new Param("order", "query", false, "string", List.of("date_desc", "date_asc", "name_asc", "name_desc"), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-artist-playlists", new Operation("spotify-artist-playlists", "GET", "/spotify/artist/playlists", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-artist-related", new Operation("spotify-artist-related", "GET", "/spotify/artist/related", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-artists-search", new Operation("spotify-artists-search", "GET", "/spotify/artists/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-audiobook", new Operation("spotify-audiobook", "GET", "/spotify/audiobook", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-audiobook-chapters", new Operation("spotify-audiobook-chapters", "GET", "/spotify/audiobook/chapters", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-audiobooks-search", new Operation("spotify-audiobooks-search", "GET", "/spotify/audiobooks/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("number_of_top_results", new Param("number_of_top_results", "query", false, "integer", List.of(), "csv")), Map.entry("include_audiobooks", new Param("include_audiobooks", "query", false, "boolean", List.of(), "csv")), Map.entry("include_pre_releases", new Param("include_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_album_pre_releases", new Param("include_album_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_authors", new Param("include_authors", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-chapter", new Operation("spotify-chapter", "GET", "/spotify/chapter", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-episodes-search", new Operation("spotify-episodes-search", "GET", "/spotify/episodes/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-featured-charts-by-country", new Operation("spotify-featured-charts-by-country", "GET", "/spotify/featured-charts-by-country", Map.ofEntries(Map.entry("country_code", new Param("country_code", "query", false, "string", List.of(), "csv")), Map.entry("content_id", new Param("content_id", "query", false, "string", List.of("CHARTS", "POPULAR_ALBUMS", "POPULAR_ARTISTS", "TRENDING_SONGS"), "csv"))), List.of("application/json")));
        operations.put("spotify-genre", new Operation("spotify-genre", "GET", "/spotify/genre", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("page_offset", new Param("page_offset", "query", false, "integer", List.of(), "csv")), Map.entry("page_limit", new Param("page_limit", "query", false, "integer", List.of(), "csv")), Map.entry("section_offset", new Param("section_offset", "query", false, "integer", List.of(), "csv")), Map.entry("section_limit", new Param("section_limit", "query", false, "integer", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-home", new Operation("spotify-home", "GET", "/spotify/home", Map.ofEntries(Map.entry("time_zone", new Param("time_zone", "query", false, "string", List.of(), "csv")), Map.entry("sp_t", new Param("sp_t", "query", false, "string", List.of(), "csv")), Map.entry("facet", new Param("facet", "query", false, "string", List.of(), "csv")), Map.entry("section_items_limit", new Param("section_items_limit", "query", false, "integer", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-playlist", new Operation("spotify-playlist", "GET", "/spotify/playlist", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("enable_watch_feed_entrypoint", new Param("enable_watch_feed_entrypoint", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-playlists-search", new Operation("spotify-playlists-search", "GET", "/spotify/playlists/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("number_of_top_results", new Param("number_of_top_results", "query", false, "integer", List.of(), "csv")), Map.entry("include_audiobooks", new Param("include_audiobooks", "query", false, "boolean", List.of(), "csv")), Map.entry("include_pre_releases", new Param("include_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_album_pre_releases", new Param("include_album_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_authors", new Param("include_authors", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-popular-by-country", new Operation("spotify-popular-by-country", "GET", "/spotify/popular-by-country", Map.ofEntries(Map.entry("country_code", new Param("country_code", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-profile", new Operation("spotify-profile", "GET", "/spotify/profile", Map.ofEntries(Map.entry("username", new Param("username", "query", false, "string", List.of(), "csv")), Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("playlist_limit", new Param("playlist_limit", "query", false, "integer", List.of(), "csv")), Map.entry("artist_limit", new Param("artist_limit", "query", false, "integer", List.of(), "csv")), Map.entry("episode_limit", new Param("episode_limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-profile-followers", new Operation("spotify-profile-followers", "GET", "/spotify/profile/followers", Map.ofEntries(Map.entry("username", new Param("username", "query", false, "string", List.of(), "csv")), Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-profile-playlists", new Operation("spotify-profile-playlists", "GET", "/spotify/profile/playlists", Map.ofEntries(Map.entry("username", new Param("username", "query", false, "string", List.of(), "csv")), Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-profiles-search", new Operation("spotify-profiles-search", "GET", "/spotify/profiles/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("number_of_top_results", new Param("number_of_top_results", "query", false, "integer", List.of(), "csv")), Map.entry("include_audiobooks", new Param("include_audiobooks", "query", false, "boolean", List.of(), "csv")), Map.entry("include_pre_releases", new Param("include_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_album_pre_releases", new Param("include_album_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_authors", new Param("include_authors", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-search", new Operation("spotify-search", "GET", "/spotify/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("number_of_top_results", new Param("number_of_top_results", "query", false, "integer", List.of(), "csv")), Map.entry("include_audiobooks", new Param("include_audiobooks", "query", false, "boolean", List.of(), "csv")), Map.entry("include_artist_has_concerts_field", new Param("include_artist_has_concerts_field", "query", false, "boolean", List.of(), "csv")), Map.entry("include_pre_releases", new Param("include_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_album_pre_releases", new Param("include_album_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_authors", new Param("include_authors", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv")), Map.entry("is_prefix", new Param("is_prefix", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-section", new Operation("spotify-section", "GET", "/spotify/section", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-shows-search", new Operation("spotify-shows-search", "GET", "/spotify/shows/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-track", new Operation("spotify-track", "GET", "/spotify/track", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-track-recommended", new Operation("spotify-track-recommended", "GET", "/spotify/track/recommended", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-track-similar-albums", new Operation("spotify-track-similar-albums", "GET", "/spotify/track/similar-albums", Map.ofEntries(Map.entry("uri", new Param("uri", "query", false, "string", List.of(), "csv")), Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("albums_only", new Param("albums_only", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("spotify-tracks-search", new Operation("spotify-tracks-search", "GET", "/spotify/tracks/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("number_of_top_results", new Param("number_of_top_results", "query", false, "integer", List.of(), "csv")), Map.entry("include_audiobooks", new Param("include_audiobooks", "query", false, "boolean", List.of(), "csv")), Map.entry("include_pre_releases", new Param("include_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_album_pre_releases", new Param("include_album_pre_releases", "query", false, "boolean", List.of(), "csv")), Map.entry("include_authors", new Param("include_authors", "query", false, "boolean", List.of(), "csv")), Map.entry("include_episode_content_ratings_v2", new Param("include_episode_content_ratings_v2", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Spotify operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object podcastsCategories(Map<String, ?> params) { return request("spotify-podcasts-categories", params); }
    public Object podcastsCharts(Map<String, ?> params) { return request("spotify-podcasts-charts", params); }
    public Object podcastsEpisode(Map<String, ?> params) { return request("spotify-podcasts-episode", params); }
    public Object podcastsHome(Map<String, ?> params) { return request("spotify-podcasts-home", params); }
    public Object podcastsSearch(Map<String, ?> params) { return request("spotify-podcasts-search", params); }
    public Object podcastsShow(Map<String, ?> params) { return request("spotify-podcasts-show", params); }
    public Object podcastsShowEpisodes(Map<String, ?> params) { return request("spotify-podcasts-show-episodes", params); }
    public Object podcastsShowRecommendations(Map<String, ?> params) { return request("spotify-podcasts-show-recommendations", params); }
    public Object album(Map<String, ?> params) { return request("spotify-album", params); }
    public Object albumTracks(Map<String, ?> params) { return request("spotify-album-tracks", params); }
    public Object albumsSearch(Map<String, ?> params) { return request("spotify-albums-search", params); }
    public Object artist(Map<String, ?> params) { return request("spotify-artist", params); }
    public Object artistAlbums(Map<String, ?> params) { return request("spotify-artist-albums", params); }
    public Object artistPlaylists(Map<String, ?> params) { return request("spotify-artist-playlists", params); }
    public Object artistRelated(Map<String, ?> params) { return request("spotify-artist-related", params); }
    public Object artistsSearch(Map<String, ?> params) { return request("spotify-artists-search", params); }
    public Object audiobook(Map<String, ?> params) { return request("spotify-audiobook", params); }
    public Object audiobookChapters(Map<String, ?> params) { return request("spotify-audiobook-chapters", params); }
    public Object audiobooksSearch(Map<String, ?> params) { return request("spotify-audiobooks-search", params); }
    public Object chapter(Map<String, ?> params) { return request("spotify-chapter", params); }
    public Object episodesSearch(Map<String, ?> params) { return request("spotify-episodes-search", params); }
    public Object featuredChartsByCountry(Map<String, ?> params) { return request("spotify-featured-charts-by-country", params); }
    public Object genre(Map<String, ?> params) { return request("spotify-genre", params); }
    public Object home(Map<String, ?> params) { return request("spotify-home", params); }
    public Object playlist(Map<String, ?> params) { return request("spotify-playlist", params); }
    public Object playlistsSearch(Map<String, ?> params) { return request("spotify-playlists-search", params); }
    public Object popularByCountry(Map<String, ?> params) { return request("spotify-popular-by-country", params); }
    public Object profile(Map<String, ?> params) { return request("spotify-profile", params); }
    public Object profileFollowers(Map<String, ?> params) { return request("spotify-profile-followers", params); }
    public Object profilePlaylists(Map<String, ?> params) { return request("spotify-profile-playlists", params); }
    public Object profilesSearch(Map<String, ?> params) { return request("spotify-profiles-search", params); }
    public Object search(Map<String, ?> params) { return request("spotify-search", params); }
    public Object section(Map<String, ?> params) { return request("spotify-section", params); }
    public Object showsSearch(Map<String, ?> params) { return request("spotify-shows-search", params); }
    public Object track(Map<String, ?> params) { return request("spotify-track", params); }
    public Object trackRecommended(Map<String, ?> params) { return request("spotify-track-recommended", params); }
    public Object trackSimilarAlbums(Map<String, ?> params) { return request("spotify-track-similar-albums", params); }
    public Object tracksSearch(Map<String, ?> params) { return request("spotify-tracks-search", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
