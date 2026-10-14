"""Typed Spotify client for the Crawlora hosted API."""

from .platform import SpotifyClient, AsyncSpotifyClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SpotifyClient
AsyncClient = AsyncSpotifyClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Spotify'
PLATFORM = 'spotify'
CONTRACT_REVISION = 'sha256:91b19237dd78b7fc691d9a20e9214e3ce7b3aa857ed5462a1a812d944ef44b0d'

__all__ = [
    "SpotifyClient", "AsyncSpotifyClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
