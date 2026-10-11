import os

from crawlora_spotify import SpotifyClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with SpotifyClient(api_key=api_key) as client:
    search = client.search(q='daft punk')
    print('search', search)
    track = client.track(id='4cOdK2wGLETKBW3PvgPWqT')
    print('track', track)
