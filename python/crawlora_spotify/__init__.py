"""Typed Spotify client for the Crawlora hosted API."""

from .platform import SpotifyClient, AsyncSpotifyClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SpotifyClient
AsyncClient = AsyncSpotifyClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Spotify'
PLATFORM = 'spotify'
CONTRACT_REVISION = 'sha256:f451f5340517c087f7a6f601dab3c1eef266bade0631f9b5d1b4455dd90c24c0'

__all__ = [
    "SpotifyClient", "AsyncSpotifyClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
