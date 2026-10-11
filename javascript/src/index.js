import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class SpotifyClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-spotify-js/0.1.0" });
    this["podcastsCategories"] = (...args) => this.request("spotify-podcasts-categories", ...args);
    this["podcastsCharts"] = (...args) => this.request("spotify-podcasts-charts", ...args);
    this["podcastsEpisode"] = (...args) => this.request("spotify-podcasts-episode", ...args);
    this["podcastsHome"] = (...args) => this.request("spotify-podcasts-home", ...args);
    this["podcastsSearch"] = (...args) => this.request("spotify-podcasts-search", ...args);
    this["podcastsShow"] = (...args) => this.request("spotify-podcasts-show", ...args);
    this["podcastsShowEpisodes"] = (...args) => this.request("spotify-podcasts-show-episodes", ...args);
    this["podcastsShowRecommendations"] = (...args) => this.request("spotify-podcasts-show-recommendations", ...args);
    this["album"] = (...args) => this.request("spotify-album", ...args);
    this["albumTracks"] = (...args) => this.request("spotify-album-tracks", ...args);
    this["albumsSearch"] = (...args) => this.request("spotify-albums-search", ...args);
    this["artist"] = (...args) => this.request("spotify-artist", ...args);
    this["artistAlbums"] = (...args) => this.request("spotify-artist-albums", ...args);
    this["artistPlaylists"] = (...args) => this.request("spotify-artist-playlists", ...args);
    this["artistRelated"] = (...args) => this.request("spotify-artist-related", ...args);
    this["artistsSearch"] = (...args) => this.request("spotify-artists-search", ...args);
    this["audiobook"] = (...args) => this.request("spotify-audiobook", ...args);
    this["audiobookChapters"] = (...args) => this.request("spotify-audiobook-chapters", ...args);
    this["audiobooksSearch"] = (...args) => this.request("spotify-audiobooks-search", ...args);
    this["chapter"] = (...args) => this.request("spotify-chapter", ...args);
    this["episodesSearch"] = (...args) => this.request("spotify-episodes-search", ...args);
    this["featuredChartsByCountry"] = (...args) => this.request("spotify-featured-charts-by-country", ...args);
    this["genre"] = (...args) => this.request("spotify-genre", ...args);
    this["home"] = (...args) => this.request("spotify-home", ...args);
    this["playlist"] = (...args) => this.request("spotify-playlist", ...args);
    this["playlistsSearch"] = (...args) => this.request("spotify-playlists-search", ...args);
    this["popularByCountry"] = (...args) => this.request("spotify-popular-by-country", ...args);
    this["profile"] = (...args) => this.request("spotify-profile", ...args);
    this["profileFollowers"] = (...args) => this.request("spotify-profile-followers", ...args);
    this["profilePlaylists"] = (...args) => this.request("spotify-profile-playlists", ...args);
    this["profilesSearch"] = (...args) => this.request("spotify-profiles-search", ...args);
    this["search"] = (...args) => this.request("spotify-search", ...args);
    this["section"] = (...args) => this.request("spotify-section", ...args);
    this["showsSearch"] = (...args) => this.request("spotify-shows-search", ...args);
    this["track"] = (...args) => this.request("spotify-track", ...args);
    this["trackRecommended"] = (...args) => this.request("spotify-track-recommended", ...args);
    this["trackSimilarAlbums"] = (...args) => this.request("spotify-track-similar-albums", ...args);
    this["tracksSearch"] = (...args) => this.request("spotify-tracks-search", ...args);
  }
}

export { SpotifyClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default SpotifyClient;
