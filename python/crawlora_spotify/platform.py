"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class SpotifyClient(CrawloraClient):
    """Synchronous Spotify API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-spotify-python/0.1.1')
        super().__init__(*args, **kwargs)

    def podcasts_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def podcasts_charts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-charts', params, response_type=response_type, timeout=timeout, headers=headers)

    def podcasts_episode(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-episode', params, response_type=response_type, timeout=timeout, headers=headers)

    def podcasts_home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-home', params, response_type=response_type, timeout=timeout, headers=headers)

    def podcasts_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def podcasts_show(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-show', params, response_type=response_type, timeout=timeout, headers=headers)

    def podcasts_show_episodes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-show-episodes', params, response_type=response_type, timeout=timeout, headers=headers)

    def podcasts_show_recommendations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-podcasts-show-recommendations', params, response_type=response_type, timeout=timeout, headers=headers)

    def album(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-album', params, response_type=response_type, timeout=timeout, headers=headers)

    def album_tracks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-album-tracks', params, response_type=response_type, timeout=timeout, headers=headers)

    def albums_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-albums-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def artist(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-artist', params, response_type=response_type, timeout=timeout, headers=headers)

    def artist_albums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-artist-albums', params, response_type=response_type, timeout=timeout, headers=headers)

    def artist_playlists(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-artist-playlists', params, response_type=response_type, timeout=timeout, headers=headers)

    def artist_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-artist-related', params, response_type=response_type, timeout=timeout, headers=headers)

    def artists_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-artists-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def audiobook(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-audiobook', params, response_type=response_type, timeout=timeout, headers=headers)

    def audiobook_chapters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-audiobook-chapters', params, response_type=response_type, timeout=timeout, headers=headers)

    def audiobooks_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-audiobooks-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def chapter(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-chapter', params, response_type=response_type, timeout=timeout, headers=headers)

    def episodes_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-episodes-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def featured_charts_by_country(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-featured-charts-by-country', params, response_type=response_type, timeout=timeout, headers=headers)

    def genre(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-genre', params, response_type=response_type, timeout=timeout, headers=headers)

    def home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-home', params, response_type=response_type, timeout=timeout, headers=headers)

    def playlist(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-playlist', params, response_type=response_type, timeout=timeout, headers=headers)

    def playlists_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-playlists-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def popular_by_country(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-popular-by-country', params, response_type=response_type, timeout=timeout, headers=headers)

    def profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-profile', params, response_type=response_type, timeout=timeout, headers=headers)

    def profile_followers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-profile-followers', params, response_type=response_type, timeout=timeout, headers=headers)

    def profile_playlists(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-profile-playlists', params, response_type=response_type, timeout=timeout, headers=headers)

    def profiles_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-profiles-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def section(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-section', params, response_type=response_type, timeout=timeout, headers=headers)

    def shows_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-shows-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def track(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-track', params, response_type=response_type, timeout=timeout, headers=headers)

    def track_recommended(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-track-recommended', params, response_type=response_type, timeout=timeout, headers=headers)

    def track_similar_albums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-track-similar-albums', params, response_type=response_type, timeout=timeout, headers=headers)

    def tracks_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('spotify-tracks-search', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncSpotifyClient(AsyncCrawloraClient):
    """Asynchronous Spotify API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-spotify-python/0.1.1')
        super().__init__(*args, **kwargs)

    async def podcasts_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def podcasts_charts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-charts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def podcasts_episode(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-episode', params, response_type=response_type, timeout=timeout, headers=headers)

    async def podcasts_home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-home', params, response_type=response_type, timeout=timeout, headers=headers)

    async def podcasts_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def podcasts_show(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-show', params, response_type=response_type, timeout=timeout, headers=headers)

    async def podcasts_show_episodes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-show-episodes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def podcasts_show_recommendations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-podcasts-show-recommendations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def album(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-album', params, response_type=response_type, timeout=timeout, headers=headers)

    async def album_tracks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-album-tracks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def albums_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-albums-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def artist(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-artist', params, response_type=response_type, timeout=timeout, headers=headers)

    async def artist_albums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-artist-albums', params, response_type=response_type, timeout=timeout, headers=headers)

    async def artist_playlists(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-artist-playlists', params, response_type=response_type, timeout=timeout, headers=headers)

    async def artist_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-artist-related', params, response_type=response_type, timeout=timeout, headers=headers)

    async def artists_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-artists-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def audiobook(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-audiobook', params, response_type=response_type, timeout=timeout, headers=headers)

    async def audiobook_chapters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-audiobook-chapters', params, response_type=response_type, timeout=timeout, headers=headers)

    async def audiobooks_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-audiobooks-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def chapter(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-chapter', params, response_type=response_type, timeout=timeout, headers=headers)

    async def episodes_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-episodes-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def featured_charts_by_country(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-featured-charts-by-country', params, response_type=response_type, timeout=timeout, headers=headers)

    async def genre(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-genre', params, response_type=response_type, timeout=timeout, headers=headers)

    async def home(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-home', params, response_type=response_type, timeout=timeout, headers=headers)

    async def playlist(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-playlist', params, response_type=response_type, timeout=timeout, headers=headers)

    async def playlists_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-playlists-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def popular_by_country(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-popular-by-country', params, response_type=response_type, timeout=timeout, headers=headers)

    async def profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-profile', params, response_type=response_type, timeout=timeout, headers=headers)

    async def profile_followers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-profile-followers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def profile_playlists(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-profile-playlists', params, response_type=response_type, timeout=timeout, headers=headers)

    async def profiles_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-profiles-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def section(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-section', params, response_type=response_type, timeout=timeout, headers=headers)

    async def shows_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-shows-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def track(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-track', params, response_type=response_type, timeout=timeout, headers=headers)

    async def track_recommended(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-track-recommended', params, response_type=response_type, timeout=timeout, headers=headers)

    async def track_similar_albums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-track-similar-albums', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tracks_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('spotify-tracks-search', params, response_type=response_type, timeout=timeout, headers=headers)
