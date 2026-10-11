import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class SpotifyClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsCategories(params?: OperationParamsMap["spotify-podcasts-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsCharts(params?: OperationParamsMap["spotify-podcasts-charts"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsEpisode(params?: OperationParamsMap["spotify-podcasts-episode"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsHome(params?: OperationParamsMap["spotify-podcasts-home"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsSearch(params: OperationParamsMap["spotify-podcasts-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsShow(params?: OperationParamsMap["spotify-podcasts-show"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsShowEpisodes(params?: OperationParamsMap["spotify-podcasts-show-episodes"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  podcastsShowRecommendations(params?: OperationParamsMap["spotify-podcasts-show-recommendations"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  album(params?: OperationParamsMap["spotify-album"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  albumTracks(params?: OperationParamsMap["spotify-album-tracks"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  albumsSearch(params: OperationParamsMap["spotify-albums-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  artist(params?: OperationParamsMap["spotify-artist"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  artistAlbums(params?: OperationParamsMap["spotify-artist-albums"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  artistPlaylists(params?: OperationParamsMap["spotify-artist-playlists"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  artistRelated(params?: OperationParamsMap["spotify-artist-related"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  artistsSearch(params: OperationParamsMap["spotify-artists-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  audiobook(params?: OperationParamsMap["spotify-audiobook"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  audiobookChapters(params?: OperationParamsMap["spotify-audiobook-chapters"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  audiobooksSearch(params: OperationParamsMap["spotify-audiobooks-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  chapter(params?: OperationParamsMap["spotify-chapter"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  episodesSearch(params: OperationParamsMap["spotify-episodes-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  featuredChartsByCountry(params?: OperationParamsMap["spotify-featured-charts-by-country"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  genre(params?: OperationParamsMap["spotify-genre"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  home(params?: OperationParamsMap["spotify-home"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playlist(params?: OperationParamsMap["spotify-playlist"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playlistsSearch(params: OperationParamsMap["spotify-playlists-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  popularByCountry(params?: OperationParamsMap["spotify-popular-by-country"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  profile(params?: OperationParamsMap["spotify-profile"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  profileFollowers(params?: OperationParamsMap["spotify-profile-followers"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  profilePlaylists(params?: OperationParamsMap["spotify-profile-playlists"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  profilesSearch(params: OperationParamsMap["spotify-profiles-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["spotify-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  section(params?: OperationParamsMap["spotify-section"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  showsSearch(params: OperationParamsMap["spotify-shows-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  track(params?: OperationParamsMap["spotify-track"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trackRecommended(params?: OperationParamsMap["spotify-track-recommended"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trackSimilarAlbums(params?: OperationParamsMap["spotify-track-similar-albums"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tracksSearch(params: OperationParamsMap["spotify-tracks-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsCategories(params?: OperationParamsMap["spotify-podcasts-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsCharts(params?: OperationParamsMap["spotify-podcasts-charts"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsEpisode(params?: OperationParamsMap["spotify-podcasts-episode"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsHome(params?: OperationParamsMap["spotify-podcasts-home"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsSearch(params: OperationParamsMap["spotify-podcasts-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsShow(params?: OperationParamsMap["spotify-podcasts-show"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsShowEpisodes(params?: OperationParamsMap["spotify-podcasts-show-episodes"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  podcastsShowRecommendations(params?: OperationParamsMap["spotify-podcasts-show-recommendations"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  album(params?: OperationParamsMap["spotify-album"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  albumTracks(params?: OperationParamsMap["spotify-album-tracks"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  albumsSearch(params: OperationParamsMap["spotify-albums-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  artist(params?: OperationParamsMap["spotify-artist"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  artistAlbums(params?: OperationParamsMap["spotify-artist-albums"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  artistPlaylists(params?: OperationParamsMap["spotify-artist-playlists"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  artistRelated(params?: OperationParamsMap["spotify-artist-related"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  artistsSearch(params: OperationParamsMap["spotify-artists-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  audiobook(params?: OperationParamsMap["spotify-audiobook"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  audiobookChapters(params?: OperationParamsMap["spotify-audiobook-chapters"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  audiobooksSearch(params: OperationParamsMap["spotify-audiobooks-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  chapter(params?: OperationParamsMap["spotify-chapter"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  episodesSearch(params: OperationParamsMap["spotify-episodes-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  featuredChartsByCountry(params?: OperationParamsMap["spotify-featured-charts-by-country"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  genre(params?: OperationParamsMap["spotify-genre"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  home(params?: OperationParamsMap["spotify-home"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playlist(params?: OperationParamsMap["spotify-playlist"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playlistsSearch(params: OperationParamsMap["spotify-playlists-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  popularByCountry(params?: OperationParamsMap["spotify-popular-by-country"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  profile(params?: OperationParamsMap["spotify-profile"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  profileFollowers(params?: OperationParamsMap["spotify-profile-followers"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  profilePlaylists(params?: OperationParamsMap["spotify-profile-playlists"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  profilesSearch(params: OperationParamsMap["spotify-profiles-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["spotify-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  section(params?: OperationParamsMap["spotify-section"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  showsSearch(params: OperationParamsMap["spotify-shows-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  track(params?: OperationParamsMap["spotify-track"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trackRecommended(params?: OperationParamsMap["spotify-track-recommended"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trackSimilarAlbums(params?: OperationParamsMap["spotify-track-similar-albums"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tracksSearch(params: OperationParamsMap["spotify-tracks-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  podcastsCategories(...args: OperationRequestArgs<"spotify-podcasts-categories">): Promise<OperationResponseMap["spotify-podcasts-categories"]>;
  podcastsCharts(...args: OperationRequestArgs<"spotify-podcasts-charts">): Promise<OperationResponseMap["spotify-podcasts-charts"]>;
  podcastsEpisode(...args: OperationRequestArgs<"spotify-podcasts-episode">): Promise<OperationResponseMap["spotify-podcasts-episode"]>;
  podcastsHome(...args: OperationRequestArgs<"spotify-podcasts-home">): Promise<OperationResponseMap["spotify-podcasts-home"]>;
  podcastsSearch(...args: OperationRequestArgs<"spotify-podcasts-search">): Promise<OperationResponseMap["spotify-podcasts-search"]>;
  podcastsShow(...args: OperationRequestArgs<"spotify-podcasts-show">): Promise<OperationResponseMap["spotify-podcasts-show"]>;
  podcastsShowEpisodes(...args: OperationRequestArgs<"spotify-podcasts-show-episodes">): Promise<OperationResponseMap["spotify-podcasts-show-episodes"]>;
  podcastsShowRecommendations(...args: OperationRequestArgs<"spotify-podcasts-show-recommendations">): Promise<OperationResponseMap["spotify-podcasts-show-recommendations"]>;
  album(...args: OperationRequestArgs<"spotify-album">): Promise<OperationResponseMap["spotify-album"]>;
  albumTracks(...args: OperationRequestArgs<"spotify-album-tracks">): Promise<OperationResponseMap["spotify-album-tracks"]>;
  albumsSearch(...args: OperationRequestArgs<"spotify-albums-search">): Promise<OperationResponseMap["spotify-albums-search"]>;
  artist(...args: OperationRequestArgs<"spotify-artist">): Promise<OperationResponseMap["spotify-artist"]>;
  artistAlbums(...args: OperationRequestArgs<"spotify-artist-albums">): Promise<OperationResponseMap["spotify-artist-albums"]>;
  artistPlaylists(...args: OperationRequestArgs<"spotify-artist-playlists">): Promise<OperationResponseMap["spotify-artist-playlists"]>;
  artistRelated(...args: OperationRequestArgs<"spotify-artist-related">): Promise<OperationResponseMap["spotify-artist-related"]>;
  artistsSearch(...args: OperationRequestArgs<"spotify-artists-search">): Promise<OperationResponseMap["spotify-artists-search"]>;
  audiobook(...args: OperationRequestArgs<"spotify-audiobook">): Promise<OperationResponseMap["spotify-audiobook"]>;
  audiobookChapters(...args: OperationRequestArgs<"spotify-audiobook-chapters">): Promise<OperationResponseMap["spotify-audiobook-chapters"]>;
  audiobooksSearch(...args: OperationRequestArgs<"spotify-audiobooks-search">): Promise<OperationResponseMap["spotify-audiobooks-search"]>;
  chapter(...args: OperationRequestArgs<"spotify-chapter">): Promise<OperationResponseMap["spotify-chapter"]>;
  episodesSearch(...args: OperationRequestArgs<"spotify-episodes-search">): Promise<OperationResponseMap["spotify-episodes-search"]>;
  featuredChartsByCountry(...args: OperationRequestArgs<"spotify-featured-charts-by-country">): Promise<OperationResponseMap["spotify-featured-charts-by-country"]>;
  genre(...args: OperationRequestArgs<"spotify-genre">): Promise<OperationResponseMap["spotify-genre"]>;
  home(...args: OperationRequestArgs<"spotify-home">): Promise<OperationResponseMap["spotify-home"]>;
  playlist(...args: OperationRequestArgs<"spotify-playlist">): Promise<OperationResponseMap["spotify-playlist"]>;
  playlistsSearch(...args: OperationRequestArgs<"spotify-playlists-search">): Promise<OperationResponseMap["spotify-playlists-search"]>;
  popularByCountry(...args: OperationRequestArgs<"spotify-popular-by-country">): Promise<OperationResponseMap["spotify-popular-by-country"]>;
  profile(...args: OperationRequestArgs<"spotify-profile">): Promise<OperationResponseMap["spotify-profile"]>;
  profileFollowers(...args: OperationRequestArgs<"spotify-profile-followers">): Promise<OperationResponseMap["spotify-profile-followers"]>;
  profilePlaylists(...args: OperationRequestArgs<"spotify-profile-playlists">): Promise<OperationResponseMap["spotify-profile-playlists"]>;
  profilesSearch(...args: OperationRequestArgs<"spotify-profiles-search">): Promise<OperationResponseMap["spotify-profiles-search"]>;
  search(...args: OperationRequestArgs<"spotify-search">): Promise<OperationResponseMap["spotify-search"]>;
  section(...args: OperationRequestArgs<"spotify-section">): Promise<OperationResponseMap["spotify-section"]>;
  showsSearch(...args: OperationRequestArgs<"spotify-shows-search">): Promise<OperationResponseMap["spotify-shows-search"]>;
  track(...args: OperationRequestArgs<"spotify-track">): Promise<OperationResponseMap["spotify-track"]>;
  trackRecommended(...args: OperationRequestArgs<"spotify-track-recommended">): Promise<OperationResponseMap["spotify-track-recommended"]>;
  trackSimilarAlbums(...args: OperationRequestArgs<"spotify-track-similar-albums">): Promise<OperationResponseMap["spotify-track-similar-albums"]>;
  tracksSearch(...args: OperationRequestArgs<"spotify-tracks-search">): Promise<OperationResponseMap["spotify-tracks-search"]>;
}
export { SpotifyClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default SpotifyClient;
