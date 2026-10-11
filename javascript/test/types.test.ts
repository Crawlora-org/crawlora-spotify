import { SpotifyClient } from "../src/index.js";

const client = new SpotifyClient({ apiKey: "test-key" });
void client.podcastsSearch({"q": "sample"});
void client.request("spotify-podcasts-search", {"q": "sample"});
const streamResponse: Promise<Response> = client.request("spotify-podcasts-search", {"q": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("spotify-podcasts-search", {"q": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.podcastsSearch({"q": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("spotify-podcasts-search", {"q": "sample", "offset": 1, "limit": 1, "number_of_top_results": 1, "include_pre_releases": true, "include_album_pre_releases": true, "include_audiobooks": true, "include_authors": true, "include_episode_content_ratings_v2": true}, { responseType: "text" });
const rawText: Promise<string> = client.request("spotify-podcasts-search", {"q": "sample"}, { responseType: "text" });
void rawText;


void client.podcastsCategories();
void client.request("spotify-podcasts-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.podcastsSearch();
