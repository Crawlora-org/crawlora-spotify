from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifySearchCatalogResponseDoc = TypedDict('ModelSpotifySearchCatalogResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifySearchResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifySearchResponse = TypedDict('ModelSpotifySearchResponse', {
    'albums': NotRequired[list[ModelSpotifySearchResultSummary]],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'audiobooks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'episodes': NotRequired[list[ModelSpotifySearchResultSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifySearchMeta],
    'offset': NotRequired[int],
    'playlists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'results': NotRequired[list[ModelSpotifySearchResultSummary]],
    'searchTerm': NotRequired[str],
    'shows': NotRequired[list[ModelSpotifySearchResultSummary]],
    'topResults': NotRequired[list[ModelSpotifySearchResultSummary]],
    'tracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'users': NotRequired[list[ModelSpotifySearchResultSummary]],
}, total=False)

ModelSpotifySearchResultSummary = TypedDict('ModelSpotifySearchResultSummary', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'publisher': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyImageAsset = TypedDict('ModelSpotifyImageAsset', {
    'height': NotRequired[int],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelSpotifySearchMeta = TypedDict('ModelSpotifySearchMeta', {
    'albumCount': NotRequired[int],
    'appVersion': NotRequired[str],
    'artistCount': NotRequired[int],
    'audiobookCount': NotRequired[int],
    'episodeCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'playlistCount': NotRequired[int],
    'resultCount': NotRequired[int],
    'showCount': NotRequired[int],
    'topCount': NotRequired[int],
    'trackCount': NotRequired[int],
    'userCount': NotRequired[int],
}, total=False)

ModelSpotifyTrackSimilarAlbumsResponseDoc = TypedDict('ModelSpotifyTrackSimilarAlbumsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyTrackSimilarAlbumsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyTrackSimilarAlbumsResponse = TypedDict('ModelSpotifyTrackSimilarAlbumsResponse', {
    'albums': NotRequired[list[ModelSpotifySearchResultSummary]],
    'albumsOnly': NotRequired[bool],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyTrackSimilarAlbumsMeta],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyTrackSimilarAlbumsMeta = TypedDict('ModelSpotifyTrackSimilarAlbumsMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyTrackRecommendedResponseDoc = TypedDict('ModelSpotifyTrackRecommendedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyTrackRecommendedResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyTrackRecommendedResponse = TypedDict('ModelSpotifyTrackRecommendedResponse', {
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyTrackRecommendedMeta],
    'recommendations': NotRequired[list[ModelSpotifyRecommendationSummary]],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyRecommendationSummary = TypedDict('ModelSpotifyRecommendationSummary', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'publisher': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyTrackRecommendedMeta = TypedDict('ModelSpotifyTrackRecommendedMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyTrackResponseDoc = TypedDict('ModelSpotifyTrackResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyTrackResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyTrackResponse = TypedDict('ModelSpotifyTrackResponse', {
    'album': NotRequired[ModelSpotifySearchResultSummary],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'discNumber': NotRequired[int],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'meta': NotRequired[ModelSpotifyTrackMeta],
    'name': NotRequired[str],
    'playabilityReason': NotRequired[str],
    'playcount': NotRequired[str],
    'previewAudioUrl': NotRequired[str],
    'previewAudioUrls': NotRequired[list[str]],
    'shareUrl': NotRequired[str],
    'trackNumber': NotRequired[int],
    'type': NotRequired[str],
    'unplayabilityReasons': NotRequired[list[str]],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyTrackMeta = TypedDict('ModelSpotifyTrackMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyBrowseSectionResponseDoc = TypedDict('ModelSpotifyBrowseSectionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyBrowseSectionResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyBrowseSectionResponse = TypedDict('ModelSpotifyBrowseSectionResponse', {
    'items': NotRequired[list[ModelSpotifyBrowsePageItem]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyBrowseSectionMeta],
    'offset': NotRequired[int],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'totalCount': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyBrowseSectionMeta = TypedDict('ModelSpotifyBrowseSectionMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyBrowsePageItem = TypedDict('ModelSpotifyBrowsePageItem', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'publisher': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyUserProfilePlaylistsResponseDoc = TypedDict('ModelSpotifyUserProfilePlaylistsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyUserProfilePlaylistsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyUserProfilePlaylistsResponse = TypedDict('ModelSpotifyUserProfilePlaylistsResponse', {
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyUserProfileMeta],
    'offset': NotRequired[int],
    'publicPlaylists': NotRequired[list[ModelSpotifyUserProfilePlaylist]],
    'totalPublicPlaylistsCount': NotRequired[int],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfilePlaylist = TypedDict('ModelSpotifyUserProfilePlaylist', {
    'externalUrl': NotRequired[str],
    'followersCount': NotRequired[int],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'isFollowing': NotRequired[bool],
    'name': NotRequired[str],
    'ownerName': NotRequired[str],
    'ownerUri': NotRequired[str],
    'ownerUrl': NotRequired[str],
    'ownerUsername': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileMeta = TypedDict('ModelSpotifyUserProfileMeta', {
    'appVersion': NotRequired[str],
    'artistCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'playlistCount': NotRequired[int],
    'profileCount': NotRequired[int],
}, total=False)

ModelSpotifyUserProfileFollowersResponseDoc = TypedDict('ModelSpotifyUserProfileFollowersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyUserProfileFollowersResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyUserProfileFollowersResponse = TypedDict('ModelSpotifyUserProfileFollowersResponse', {
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyUserProfileMeta],
    'offset': NotRequired[int],
    'profiles': NotRequired[list[ModelSpotifyUserProfileSummary]],
    'total': NotRequired[int],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileSummary = TypedDict('ModelSpotifyUserProfileSummary', {
    'color': NotRequired[int],
    'externalUrl': NotRequired[str],
    'followersCount': NotRequired[int],
    'imageUrl': NotRequired[str],
    'isFollowing': NotRequired[bool],
    'name': NotRequired[str],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileResponseDoc = TypedDict('ModelSpotifyUserProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyUserProfileResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyUserProfileResponse = TypedDict('ModelSpotifyUserProfileResponse', {
    'allowFollows': NotRequired[bool],
    'color': NotRequired[int],
    'externalUrl': NotRequired[str],
    'followersCount': NotRequired[int],
    'followingCount': NotRequired[int],
    'hasSpotifyImage': NotRequired[bool],
    'hasSpotifyName': NotRequired[bool],
    'imageUrl': NotRequired[str],
    'isCurrentUser': NotRequired[bool],
    'isVerified': NotRequired[bool],
    'meta': NotRequired[ModelSpotifyUserProfileMeta],
    'name': NotRequired[str],
    'publicPlaylists': NotRequired[list[ModelSpotifyUserProfilePlaylist]],
    'recentlyPlayedArtists': NotRequired[list[ModelSpotifyUserProfileSummary]],
    'showFollows': NotRequired[bool],
    'topArtists': NotRequired[ModelSpotifyUserProfileTopArtists],
    'totalPublicPlaylistsCount': NotRequired[int],
    'uri': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelSpotifyUserProfileTopArtists = TypedDict('ModelSpotifyUserProfileTopArtists', {
    'imageUrl': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'topArtistsPageUri': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubResponseDoc = TypedDict('ModelSpotifyCountryHubResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyCountryHubResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyCountryHubResponse = TypedDict('ModelSpotifyCountryHubResponse', {
    'countryCode': NotRequired[str],
    'countryName': NotRequired[str],
    'hexColor': NotRequired[str],
    'meta': NotRequired[ModelSpotifyCountryHubMeta],
    'sections': NotRequired[list[ModelSpotifyCountryHubSection]],
    'supportedCountries': NotRequired[list[ModelSpotifyPopularCountry]],
}, total=False)

ModelSpotifyPopularCountry = TypedDict('ModelSpotifyPopularCountry', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubSection = TypedDict('ModelSpotifyCountryHubSection', {
    'contentId': NotRequired[str],
    'items': NotRequired[list[ModelSpotifyCountryHubItem]],
    'title': NotRequired[str],
    'totalCount': NotRequired[int],
}, total=False)

ModelSpotifyCountryHubItem = TypedDict('ModelSpotifyCountryHubItem', {
    'album': NotRequired[ModelSpotifySearchResultSummary],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'attributes': NotRequired[dict[str, str]],
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'owner': NotRequired[ModelSpotifySearchResultSummary],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubMeta = TypedDict('ModelSpotifyCountryHubMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'itemCount': NotRequired[int],
    'operationName': NotRequired[str],
    'partialErrors': NotRequired[int],
    'sectionCount': NotRequired[int],
}, total=False)

ModelSpotifyPlaylistResponseDoc = TypedDict('ModelSpotifyPlaylistResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyPlaylistResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyPlaylistResponse = TypedDict('ModelSpotifyPlaylistResponse', {
    'collaborative': NotRequired[bool],
    'description': NotRequired[str],
    'episodes': NotRequired[list[ModelSpotifySearchResultSummary]],
    'externalUrl': NotRequired[str],
    'followers': NotRequired[int],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'items': NotRequired[list[ModelSpotifySearchResultSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyPlaylistMeta],
    'name': NotRequired[str],
    'offset': NotRequired[int],
    'owner': NotRequired[ModelSpotifySearchResultSummary],
    'shareUrl': NotRequired[str],
    'total': NotRequired[int],
    'tracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyPlaylistMeta = TypedDict('ModelSpotifyPlaylistMeta', {
    'appVersion': NotRequired[str],
    'episodeCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'itemCount': NotRequired[int],
    'operationName': NotRequired[str],
    'trackCount': NotRequired[int],
}, total=False)

ModelSpotifyHomeResponseDoc = TypedDict('ModelSpotifyHomeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyHomeResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyHomeResponse = TypedDict('ModelSpotifyHomeResponse', {
    'facet': NotRequired[str],
    'greeting': NotRequired[str],
    'meta': NotRequired[ModelSpotifyHomeMeta],
    'sections': NotRequired[list[ModelSpotifyBrowsePageSection]],
    'timeZone': NotRequired[str],
}, total=False)

ModelSpotifyBrowsePageSection = TypedDict('ModelSpotifyBrowsePageSection', {
    'items': NotRequired[list[ModelSpotifyBrowsePageItem]],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'totalCount': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyHomeMeta = TypedDict('ModelSpotifyHomeMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'sectionCount': NotRequired[int],
}, total=False)

ModelSpotifyBrowsePageResponseDoc = TypedDict('ModelSpotifyBrowsePageResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyBrowsePageResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyBrowsePageResponse = TypedDict('ModelSpotifyBrowsePageResponse', {
    'meta': NotRequired[ModelSpotifyBrowsePageMeta],
    'sections': NotRequired[list[ModelSpotifyBrowsePageSection]],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyBrowsePageMeta = TypedDict('ModelSpotifyBrowsePageMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'sectionCount': NotRequired[int],
}, total=False)

ModelSpotifyCountryHubContentResponseDoc = TypedDict('ModelSpotifyCountryHubContentResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyCountryHubContentResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyCountryHubContentResponse = TypedDict('ModelSpotifyCountryHubContentResponse', {
    'contentId': NotRequired[str],
    'countryCode': NotRequired[str],
    'countryName': NotRequired[str],
    'hexColor': NotRequired[str],
    'items': NotRequired[list[ModelSpotifyCountryHubItem]],
    'meta': NotRequired[ModelSpotifyCountryHubContentMeta],
    'supportedContentIds': NotRequired[list[ModelSpotifyCountryHubContentId]],
    'supportedCountries': NotRequired[list[ModelSpotifyPopularCountry]],
    'title': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubContentId = TypedDict('ModelSpotifyCountryHubContentId', {
    'id': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelSpotifyCountryHubContentMeta = TypedDict('ModelSpotifyCountryHubContentMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'itemCount': NotRequired[int],
    'operationName': NotRequired[str],
    'partialErrors': NotRequired[int],
}, total=False)

ModelSpotifyEpisodeResponseDoc = TypedDict('ModelSpotifyEpisodeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyPodcastEpisodeResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyPodcastEpisodeResponse = TypedDict('ModelSpotifyPodcastEpisodeResponse', {
    'description': NotRequired[str],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'htmlDescription': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPaywallContent': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'mediaTypes': NotRequired[list[str]],
    'meta': NotRequired[ModelSpotifyPodcastEpisodeMeta],
    'name': NotRequired[str],
    'playabilityReason': NotRequired[str],
    'previewAudioUrl': NotRequired[str],
    'previewAudioUrls': NotRequired[list[str]],
    'previewVideoUrl': NotRequired[str],
    'releaseDate': NotRequired[str],
    'releaseDatePrecision': NotRequired[str],
    'shareUrl': NotRequired[str],
    'show': NotRequired[ModelSpotifyPodcastEpisodeShowSummary],
    'transcriptCount': NotRequired[int],
    'type': NotRequired[str],
    'unplayabilityReasons': NotRequired[list[str]],
    'uri': NotRequired[str],
    'videoThumbnailUrl': NotRequired[str],
    'videoThumbnails': NotRequired[list[ModelSpotifyImageAsset]],
}, total=False)

ModelSpotifyPodcastEpisodeShowSummary = TypedDict('ModelSpotifyPodcastEpisodeShowSummary', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'mediaType': NotRequired[str],
    'name': NotRequired[str],
    'publisher': NotRequired[str],
    'showTypes': NotRequired[list[str]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodeMeta = TypedDict('ModelSpotifyPodcastEpisodeMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'sourceUrl': NotRequired[str],
}, total=False)

ModelSpotifyAudiobookChaptersResponseDoc = TypedDict('ModelSpotifyAudiobookChaptersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyAudiobookChaptersResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyAudiobookChaptersResponse = TypedDict('ModelSpotifyAudiobookChaptersResponse', {
    'chapters': NotRequired[list[ModelSpotifyPodcastEpisodeSummary]],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyAudiobookChaptersMeta],
    'offset': NotRequired[int],
    'total': NotRequired[int],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyAudiobookChaptersMeta = TypedDict('ModelSpotifyAudiobookChaptersMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodeSummary = TypedDict('ModelSpotifyPodcastEpisodeSummary', {
    'description': NotRequired[str],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'name': NotRequired[str],
    'releaseDate': NotRequired[str],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyAudiobookResponseDoc = TypedDict('ModelSpotifyAudiobookResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyAudiobookResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyAudiobookResponse = TypedDict('ModelSpotifyAudiobookResponse', {
    'authors': NotRequired[list[str]],
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'mediaType': NotRequired[str],
    'meta': NotRequired[ModelSpotifyAudiobookMeta],
    'name': NotRequired[str],
    'narrators': NotRequired[list[str]],
    'publisher': NotRequired[str],
    'totalChapters': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyAudiobookMeta = TypedDict('ModelSpotifyAudiobookMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyArtistCollectionResponseDoc = TypedDict('ModelSpotifyArtistCollectionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyArtistCollectionResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyArtistCollectionResponse = TypedDict('ModelSpotifyArtistCollectionResponse', {
    'id': NotRequired[str],
    'items': NotRequired[list[ModelSpotifySearchResultSummary]],
    'meta': NotRequired[ModelSpotifyArtistCollectionMeta],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyArtistCollectionMeta = TypedDict('ModelSpotifyArtistCollectionMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyArtistAlbumsResponseDoc = TypedDict('ModelSpotifyArtistAlbumsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyArtistAlbumsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyArtistAlbumsResponse = TypedDict('ModelSpotifyArtistAlbumsResponse', {
    'id': NotRequired[str],
    'items': NotRequired[list[ModelSpotifySearchResultSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyArtistAlbumsMeta],
    'offset': NotRequired[int],
    'order': NotRequired[str],
    'total': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyArtistAlbumsMeta = TypedDict('ModelSpotifyArtistAlbumsMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyArtistResponseDoc = TypedDict('ModelSpotifyArtistResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyArtistResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyArtistResponse = TypedDict('ModelSpotifyArtistResponse', {
    'biography': NotRequired[str],
    'discography': NotRequired[list[ModelSpotifySearchResultSummary]],
    'externalUrl': NotRequired[str],
    'followers': NotRequired[int],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'meta': NotRequired[ModelSpotifyArtistMeta],
    'monthlyUsers': NotRequired[int],
    'name': NotRequired[str],
    'playlists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'related': NotRequired[list[ModelSpotifySearchResultSummary]],
    'shareUrl': NotRequired[str],
    'topTracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelSpotifyArtistMeta = TypedDict('ModelSpotifyArtistMeta', {
    'appVersion': NotRequired[str],
    'discographyCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'playlistCount': NotRequired[int],
    'relatedCount': NotRequired[int],
    'topTrackCount': NotRequired[int],
}, total=False)

ModelSpotifyAlbumResponseDoc = TypedDict('ModelSpotifyAlbumResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyAlbumResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyAlbumResponse = TypedDict('ModelSpotifyAlbumResponse', {
    'albumType': NotRequired[str],
    'artists': NotRequired[list[ModelSpotifySearchResultSummary]],
    'copyrights': NotRequired[list[str]],
    'durationMs': NotRequired[int],
    'externalUrl': NotRequired[str],
    'id': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'isPlayable': NotRequired[bool],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyAlbumMeta],
    'name': NotRequired[str],
    'offset': NotRequired[int],
    'releaseDate': NotRequired[str],
    'shareUrl': NotRequired[str],
    'totalTracks': NotRequired[int],
    'tracks': NotRequired[list[ModelSpotifySearchResultSummary]],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyAlbumMeta = TypedDict('ModelSpotifyAlbumMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'trackCount': NotRequired[int],
}, total=False)

ModelSpotifyShowRecommendationsResponseDoc = TypedDict('ModelSpotifyShowRecommendationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyShowRecommendationsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyShowRecommendationsResponse = TypedDict('ModelSpotifyShowRecommendationsResponse', {
    'meta': NotRequired[ModelSpotifyShowRecommendationsMeta],
    'recommendations': NotRequired[list[ModelSpotifyRecommendationSummary]],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyShowRecommendationsMeta = TypedDict('ModelSpotifyShowRecommendationsMeta', {
    'appVersion': NotRequired[str],
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyShowEpisodesResponseDoc = TypedDict('ModelSpotifyShowEpisodesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyPodcastEpisodesResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyPodcastEpisodesResponse = TypedDict('ModelSpotifyPodcastEpisodesResponse', {
    'episodes': NotRequired[list[ModelSpotifyPodcastEpisodeSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyPodcastEpisodesMeta],
    'offset': NotRequired[int],
    'total': NotRequired[int],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyPodcastEpisodesMeta = TypedDict('ModelSpotifyPodcastEpisodesMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifyShowResponseDoc = TypedDict('ModelSpotifyShowResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyShowMetadataResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyShowMetadataResponse = TypedDict('ModelSpotifyShowMetadataResponse', {
    'description': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'images': NotRequired[list[ModelSpotifyImageAsset]],
    'isExplicit': NotRequired[bool],
    'mediaType': NotRequired[str],
    'meta': NotRequired[ModelSpotifyShowMetadataMeta],
    'name': NotRequired[str],
    'publisher': NotRequired[str],
    'totalEpisodes': NotRequired[int],
    'type': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

ModelSpotifyShowMetadataMeta = TypedDict('ModelSpotifyShowMetadataMeta', {
    'appVersion': NotRequired[str],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
}, total=False)

ModelSpotifySearchResponseDoc = TypedDict('ModelSpotifySearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifySearchPodcastsResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifySearchPodcastsResponse = TypedDict('ModelSpotifySearchPodcastsResponse', {
    'episodes': NotRequired[list[ModelSpotifyPodcastEpisodeSummary]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifySearchPodcastsMeta],
    'offset': NotRequired[int],
    'searchTerm': NotRequired[str],
    'shows': NotRequired[list[ModelSpotifyRecommendationSummary]],
    'topResults': NotRequired[list[ModelSpotifySearchResultSummary]],
}, total=False)

ModelSpotifySearchPodcastsMeta = TypedDict('ModelSpotifySearchPodcastsMeta', {
    'appVersion': NotRequired[str],
    'episodeCount': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'operationName': NotRequired[str],
    'showCount': NotRequired[int],
    'topCount': NotRequired[int],
}, total=False)

ModelSpotifyChartsResponseDoc = TypedDict('ModelSpotifyChartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSpotifyChartResponse],
    'msg': NotRequired[Any],
}, total=False)

ModelSpotifyChartResponse = TypedDict('ModelSpotifyChartResponse', {
    'chart': NotRequired[str],
    'chartName': NotRequired[str],
    'chartType': NotRequired[str],
    'items': NotRequired[list[ModelSpotifyChartItem]],
    'limit': NotRequired[int],
    'meta': NotRequired[ModelSpotifyChartMeta],
    'region': NotRequired[str],
    'regionName': NotRequired[str],
}, total=False)

ModelSpotifyChartMeta = TypedDict('ModelSpotifyChartMeta', {
    'count': NotRequired[int],
    'fetchedAt': NotRequired[str],
    'sourceUrl': NotRequired[str],
}, total=False)

ModelSpotifyChartItem = TypedDict('ModelSpotifyChartItem', {
    'description': NotRequired[str],
    'episodeDescription': NotRequired[str],
    'episodeExternalUrl': NotRequired[str],
    'episodeImageUrl': NotRequired[str],
    'episodeName': NotRequired[str],
    'episodeUri': NotRequired[str],
    'externalUrl': NotRequired[str],
    'imageUrl': NotRequired[str],
    'name': NotRequired[str],
    'publisher': NotRequired[str],
    'rank': NotRequired[int],
    'rankMove': NotRequired[str],
    'showDescription': NotRequired[str],
    'showExternalUrl': NotRequired[str],
    'showImageUrl': NotRequired[str],
    'showName': NotRequired[str],
    'showPublisher': NotRequired[str],
    'showUri': NotRequired[str],
    'uri': NotRequired[str],
}, total=False)

SpotifyPodcastsCategoriesResponse = ModelSpotifyBrowsePageResponseDoc
SpotifyPodcastsCategoriesParams = TypedDict('SpotifyPodcastsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsChartsResponse = ModelSpotifyChartsResponseDoc
SpotifyPodcastsChartsParams = TypedDict('SpotifyPodcastsChartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart': NotRequired[Literal['top-podcasts', 'top-episodes', 'trending', 'arts', 'business', 'comedy', 'education', 'fiction', 'health-fitness', 'history', 'leisure', 'music', 'news', 'religion-spirituality', 'science', 'society-culture', 'sports', 'technology', 'true-crime', 'tv-film']],
    'region': NotRequired[Literal['ar', 'au', 'at', 'br', 'ca', 'cl', 'co', 'dk', 'fi', 'fr', 'de', 'in', 'id', 'ie', 'it', 'jp', 'mx', 'nz', 'no', 'ph', 'pl', 'es', 'se', 'nl', 'gb', 'us']],
    'limit': NotRequired[int],
}, total=False)

SpotifyPodcastsEpisodeResponse = ModelSpotifyEpisodeResponseDoc
SpotifyPodcastsEpisodeParams = TypedDict('SpotifyPodcastsEpisodeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyPodcastsHomeResponse = ModelSpotifyBrowsePageResponseDoc
SpotifyPodcastsHomeParams = TypedDict('SpotifyPodcastsHomeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsSearchResponse = ModelSpotifySearchResponseDoc
SpotifyPodcastsSearchParams = TypedDict('SpotifyPodcastsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_audiobooks': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowResponse = ModelSpotifyShowResponseDoc
SpotifyPodcastsShowParams = TypedDict('SpotifyPodcastsShowParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'include_content_capability_trait': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowEpisodesResponse = ModelSpotifyShowEpisodesResponseDoc
SpotifyPodcastsShowEpisodesParams = TypedDict('SpotifyPodcastsShowEpisodesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowRecommendationsResponse = ModelSpotifyShowRecommendationsResponseDoc
SpotifyPodcastsShowRecommendationsParams = TypedDict('SpotifyPodcastsShowRecommendationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
}, total=False)

SpotifyAlbumResponse = ModelSpotifyAlbumResponseDoc
SpotifyAlbumParams = TypedDict('SpotifyAlbumParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumTracksResponse = ModelSpotifyAlbumResponseDoc
SpotifyAlbumTracksParams = TypedDict('SpotifyAlbumTracksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumsSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyAlbumsSearchParams = TypedDict('SpotifyAlbumsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyArtistResponse = ModelSpotifyArtistResponseDoc
SpotifyArtistParams = TypedDict('SpotifyArtistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistAlbumsResponse = ModelSpotifyArtistAlbumsResponseDoc
SpotifyArtistAlbumsParams = TypedDict('SpotifyArtistAlbumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'type': NotRequired[Literal['album', 'single', 'compilation', 'appears_on', 'all']],
    'order': NotRequired[Literal['date_desc', 'date_asc', 'name_asc', 'name_desc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyArtistPlaylistsResponse = ModelSpotifyArtistCollectionResponseDoc
SpotifyArtistPlaylistsParams = TypedDict('SpotifyArtistPlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistRelatedResponse = ModelSpotifyArtistCollectionResponseDoc
SpotifyArtistRelatedParams = TypedDict('SpotifyArtistRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistsSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyArtistsSearchParams = TypedDict('SpotifyArtistsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobookResponse = ModelSpotifyAudiobookResponseDoc
SpotifyAudiobookParams = TypedDict('SpotifyAudiobookParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyAudiobookChaptersResponse = ModelSpotifyAudiobookChaptersResponseDoc
SpotifyAudiobookChaptersParams = TypedDict('SpotifyAudiobookChaptersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobooksSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyAudiobooksSearchParams = TypedDict('SpotifyAudiobooksSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyChapterResponse = ModelSpotifyEpisodeResponseDoc
SpotifyChapterParams = TypedDict('SpotifyChapterParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyEpisodesSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyEpisodesSearchParams = TypedDict('SpotifyEpisodesSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyFeaturedChartsByCountryResponse = ModelSpotifyCountryHubContentResponseDoc
SpotifyFeaturedChartsByCountryParams = TypedDict('SpotifyFeaturedChartsByCountryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': NotRequired[str],
    'content_id': NotRequired[Literal['CHARTS', 'POPULAR_ALBUMS', 'POPULAR_ARTISTS', 'TRENDING_SONGS']],
}, total=False)

SpotifyGenreResponse = ModelSpotifyBrowsePageResponseDoc
SpotifyGenreParams = TypedDict('SpotifyGenreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyHomeResponse = ModelSpotifyHomeResponseDoc
SpotifyHomeParams = TypedDict('SpotifyHomeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'time_zone': NotRequired[str],
    'sp_t': NotRequired[str],
    'facet': NotRequired[str],
    'section_items_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistResponse = ModelSpotifyPlaylistResponseDoc
SpotifyPlaylistParams = TypedDict('SpotifyPlaylistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'enable_watch_feed_entrypoint': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistsSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyPlaylistsSearchParams = TypedDict('SpotifyPlaylistsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPopularByCountryResponse = ModelSpotifyCountryHubResponseDoc
SpotifyPopularByCountryParams = TypedDict('SpotifyPopularByCountryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': NotRequired[str],
}, total=False)

SpotifyProfileResponse = ModelSpotifyUserProfileResponseDoc
SpotifyProfileParams = TypedDict('SpotifyProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'playlist_limit': NotRequired[int],
    'artist_limit': NotRequired[int],
    'episode_limit': NotRequired[int],
}, total=False)

SpotifyProfileFollowersResponse = ModelSpotifyUserProfileFollowersResponseDoc
SpotifyProfileFollowersParams = TypedDict('SpotifyProfileFollowersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilePlaylistsResponse = ModelSpotifyUserProfilePlaylistsResponseDoc
SpotifyProfilePlaylistsParams = TypedDict('SpotifyProfilePlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilesSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyProfilesSearchParams = TypedDict('SpotifyProfilesSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifySearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifySearchParams = TypedDict('SpotifySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_artist_has_concerts_field': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
    'is_prefix': NotRequired[bool],
}, total=False)

SpotifySectionResponse = ModelSpotifyBrowseSectionResponseDoc
SpotifySectionParams = TypedDict('SpotifySectionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyShowsSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyShowsSearchParams = TypedDict('SpotifyShowsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackResponse = ModelSpotifyTrackResponseDoc
SpotifyTrackParams = TypedDict('SpotifyTrackParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyTrackRecommendedResponse = ModelSpotifyTrackRecommendedResponseDoc
SpotifyTrackRecommendedParams = TypedDict('SpotifyTrackRecommendedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackSimilarAlbumsResponse = ModelSpotifyTrackSimilarAlbumsResponseDoc
SpotifyTrackSimilarAlbumsParams = TypedDict('SpotifyTrackSimilarAlbumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'albums_only': NotRequired[bool],
}, total=False)

SpotifyTracksSearchResponse = ModelSpotifySearchCatalogResponseDoc
SpotifyTracksSearchParams = TypedDict('SpotifyTracksSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

class SpotifyGroup:
    @overload
    def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesTextResponseParams]) -> str: ...
    @overload
    def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesDefaultParams]) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsTextResponseParams]) -> str: ...
    @overload
    def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsDefaultParams]) -> SpotifyPodcastsChartsResponse: ...
    @overload
    def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeTextResponseParams]) -> str: ...
    @overload
    def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeDefaultParams]) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeTextResponseParams]) -> str: ...
    @overload
    def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeDefaultParams]) -> SpotifyPodcastsHomeResponse: ...
    @overload
    def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchTextResponseParams]) -> str: ...
    @overload
    def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchDefaultParams]) -> SpotifyPodcastsSearchResponse: ...
    @overload
    def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowTextResponseParams]) -> str: ...
    @overload
    def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowDefaultParams]) -> SpotifyPodcastsShowResponse: ...
    @overload
    def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesTextResponseParams]) -> str: ...
    @overload
    def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesDefaultParams]) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsTextResponseParams]) -> str: ...
    @overload
    def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsDefaultParams]) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    def album(self, **params: Unpack[SpotifyAlbumStreamParams]) -> BinaryIO: ...
    @overload
    def album(self, **params: Unpack[SpotifyAlbumTextResponseParams]) -> str: ...
    @overload
    def album(self, **params: Unpack[SpotifyAlbumDefaultParams]) -> SpotifyAlbumResponse: ...
    @overload
    def album_tracks(self, **params: Unpack[SpotifyAlbumTracksStreamParams]) -> BinaryIO: ...
    @overload
    def album_tracks(self, **params: Unpack[SpotifyAlbumTracksTextResponseParams]) -> str: ...
    @overload
    def album_tracks(self, **params: Unpack[SpotifyAlbumTracksDefaultParams]) -> SpotifyAlbumTracksResponse: ...
    @overload
    def albums_search(self, **params: Unpack[SpotifyAlbumsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def albums_search(self, **params: Unpack[SpotifyAlbumsSearchTextResponseParams]) -> str: ...
    @overload
    def albums_search(self, **params: Unpack[SpotifyAlbumsSearchDefaultParams]) -> SpotifyAlbumsSearchResponse: ...
    @overload
    def artist(self, **params: Unpack[SpotifyArtistStreamParams]) -> BinaryIO: ...
    @overload
    def artist(self, **params: Unpack[SpotifyArtistTextResponseParams]) -> str: ...
    @overload
    def artist(self, **params: Unpack[SpotifyArtistDefaultParams]) -> SpotifyArtistResponse: ...
    @overload
    def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsTextResponseParams]) -> str: ...
    @overload
    def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsDefaultParams]) -> SpotifyArtistAlbumsResponse: ...
    @overload
    def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsTextResponseParams]) -> str: ...
    @overload
    def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsDefaultParams]) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    def artist_related(self, **params: Unpack[SpotifyArtistRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def artist_related(self, **params: Unpack[SpotifyArtistRelatedTextResponseParams]) -> str: ...
    @overload
    def artist_related(self, **params: Unpack[SpotifyArtistRelatedDefaultParams]) -> SpotifyArtistRelatedResponse: ...
    @overload
    def artists_search(self, **params: Unpack[SpotifyArtistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def artists_search(self, **params: Unpack[SpotifyArtistsSearchTextResponseParams]) -> str: ...
    @overload
    def artists_search(self, **params: Unpack[SpotifyArtistsSearchDefaultParams]) -> SpotifyArtistsSearchResponse: ...
    @overload
    def audiobook(self, **params: Unpack[SpotifyAudiobookStreamParams]) -> BinaryIO: ...
    @overload
    def audiobook(self, **params: Unpack[SpotifyAudiobookTextResponseParams]) -> str: ...
    @overload
    def audiobook(self, **params: Unpack[SpotifyAudiobookDefaultParams]) -> SpotifyAudiobookResponse: ...
    @overload
    def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersStreamParams]) -> BinaryIO: ...
    @overload
    def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersTextResponseParams]) -> str: ...
    @overload
    def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersDefaultParams]) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchStreamParams]) -> BinaryIO: ...
    @overload
    def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchTextResponseParams]) -> str: ...
    @overload
    def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchDefaultParams]) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    def chapter(self, **params: Unpack[SpotifyChapterStreamParams]) -> BinaryIO: ...
    @overload
    def chapter(self, **params: Unpack[SpotifyChapterTextResponseParams]) -> str: ...
    @overload
    def chapter(self, **params: Unpack[SpotifyChapterDefaultParams]) -> SpotifyChapterResponse: ...
    @overload
    def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchStreamParams]) -> BinaryIO: ...
    @overload
    def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchTextResponseParams]) -> str: ...
    @overload
    def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchDefaultParams]) -> SpotifyEpisodesSearchResponse: ...
    @overload
    def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryStreamParams]) -> BinaryIO: ...
    @overload
    def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryTextResponseParams]) -> str: ...
    @overload
    def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryDefaultParams]) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    def genre(self, **params: Unpack[SpotifyGenreStreamParams]) -> BinaryIO: ...
    @overload
    def genre(self, **params: Unpack[SpotifyGenreTextResponseParams]) -> str: ...
    @overload
    def genre(self, **params: Unpack[SpotifyGenreDefaultParams]) -> SpotifyGenreResponse: ...
    @overload
    def home(self, **params: Unpack[SpotifyHomeStreamParams]) -> BinaryIO: ...
    @overload
    def home(self, **params: Unpack[SpotifyHomeTextResponseParams]) -> str: ...
    @overload
    def home(self, **params: Unpack[SpotifyHomeDefaultParams]) -> SpotifyHomeResponse: ...
    @overload
    def playlist(self, **params: Unpack[SpotifyPlaylistStreamParams]) -> BinaryIO: ...
    @overload
    def playlist(self, **params: Unpack[SpotifyPlaylistTextResponseParams]) -> str: ...
    @overload
    def playlist(self, **params: Unpack[SpotifyPlaylistDefaultParams]) -> SpotifyPlaylistResponse: ...
    @overload
    def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchTextResponseParams]) -> str: ...
    @overload
    def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchDefaultParams]) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryStreamParams]) -> BinaryIO: ...
    @overload
    def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryTextResponseParams]) -> str: ...
    @overload
    def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryDefaultParams]) -> SpotifyPopularByCountryResponse: ...
    @overload
    def profile(self, **params: Unpack[SpotifyProfileStreamParams]) -> BinaryIO: ...
    @overload
    def profile(self, **params: Unpack[SpotifyProfileTextResponseParams]) -> str: ...
    @overload
    def profile(self, **params: Unpack[SpotifyProfileDefaultParams]) -> SpotifyProfileResponse: ...
    @overload
    def profile_followers(self, **params: Unpack[SpotifyProfileFollowersStreamParams]) -> BinaryIO: ...
    @overload
    def profile_followers(self, **params: Unpack[SpotifyProfileFollowersTextResponseParams]) -> str: ...
    @overload
    def profile_followers(self, **params: Unpack[SpotifyProfileFollowersDefaultParams]) -> SpotifyProfileFollowersResponse: ...
    @overload
    def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsTextResponseParams]) -> str: ...
    @overload
    def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsDefaultParams]) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    def profiles_search(self, **params: Unpack[SpotifyProfilesSearchStreamParams]) -> BinaryIO: ...
    @overload
    def profiles_search(self, **params: Unpack[SpotifyProfilesSearchTextResponseParams]) -> str: ...
    @overload
    def profiles_search(self, **params: Unpack[SpotifyProfilesSearchDefaultParams]) -> SpotifyProfilesSearchResponse: ...
    @overload
    def search(self, **params: Unpack[SpotifySearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[SpotifySearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[SpotifySearchDefaultParams]) -> SpotifySearchResponse: ...
    @overload
    def section(self, **params: Unpack[SpotifySectionStreamParams]) -> BinaryIO: ...
    @overload
    def section(self, **params: Unpack[SpotifySectionTextResponseParams]) -> str: ...
    @overload
    def section(self, **params: Unpack[SpotifySectionDefaultParams]) -> SpotifySectionResponse: ...
    @overload
    def shows_search(self, **params: Unpack[SpotifyShowsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def shows_search(self, **params: Unpack[SpotifyShowsSearchTextResponseParams]) -> str: ...
    @overload
    def shows_search(self, **params: Unpack[SpotifyShowsSearchDefaultParams]) -> SpotifyShowsSearchResponse: ...
    @overload
    def track(self, **params: Unpack[SpotifyTrackStreamParams]) -> BinaryIO: ...
    @overload
    def track(self, **params: Unpack[SpotifyTrackTextResponseParams]) -> str: ...
    @overload
    def track(self, **params: Unpack[SpotifyTrackDefaultParams]) -> SpotifyTrackResponse: ...
    @overload
    def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedStreamParams]) -> BinaryIO: ...
    @overload
    def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedTextResponseParams]) -> str: ...
    @overload
    def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedDefaultParams]) -> SpotifyTrackRecommendedResponse: ...
    @overload
    def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsTextResponseParams]) -> str: ...
    @overload
    def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsDefaultParams]) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    def tracks_search(self, **params: Unpack[SpotifyTracksSearchStreamParams]) -> BinaryIO: ...
    @overload
    def tracks_search(self, **params: Unpack[SpotifyTracksSearchTextResponseParams]) -> str: ...
    @overload
    def tracks_search(self, **params: Unpack[SpotifyTracksSearchDefaultParams]) -> SpotifyTracksSearchResponse: ...

OperationId = Literal[
    'spotify-podcasts-categories',
    'spotify-podcasts-charts',
    'spotify-podcasts-episode',
    'spotify-podcasts-home',
    'spotify-podcasts-search',
    'spotify-podcasts-show',
    'spotify-podcasts-show-episodes',
    'spotify-podcasts-show-recommendations',
    'spotify-album',
    'spotify-album-tracks',
    'spotify-albums-search',
    'spotify-artist',
    'spotify-artist-albums',
    'spotify-artist-playlists',
    'spotify-artist-related',
    'spotify-artists-search',
    'spotify-audiobook',
    'spotify-audiobook-chapters',
    'spotify-audiobooks-search',
    'spotify-chapter',
    'spotify-episodes-search',
    'spotify-featured-charts-by-country',
    'spotify-genre',
    'spotify-home',
    'spotify-playlist',
    'spotify-playlists-search',
    'spotify-popular-by-country',
    'spotify-profile',
    'spotify-profile-followers',
    'spotify-profile-playlists',
    'spotify-profiles-search',
    'spotify-search',
    'spotify-section',
    'spotify-shows-search',
    'spotify-track',
    'spotify-track-recommended',
    'spotify-track-similar-albums',
    'spotify-tracks-search',
]

class CrawloraClient:
    spotify: SpotifyGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-categories'],
        params: SpotifyPodcastsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-charts'],
        params: SpotifyPodcastsChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsChartsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-episode'],
        params: SpotifyPodcastsEpisodeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-home'],
        params: SpotifyPodcastsHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsHomeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-search'],
        params: SpotifyPodcastsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-show'],
        params: SpotifyPodcastsShowParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-show-episodes'],
        params: SpotifyPodcastsShowEpisodesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-podcasts-show-recommendations'],
        params: SpotifyPodcastsShowRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-album'],
        params: SpotifyAlbumParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-album-tracks'],
        params: SpotifyAlbumTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumTracksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-albums-search'],
        params: SpotifyAlbumsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist'],
        params: SpotifyArtistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist-albums'],
        params: SpotifyArtistAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistAlbumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist-playlists'],
        params: SpotifyArtistPlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artist-related'],
        params: SpotifyArtistRelatedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-artists-search'],
        params: SpotifyArtistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-audiobook'],
        params: SpotifyAudiobookParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-audiobook-chapters'],
        params: SpotifyAudiobookChaptersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-audiobooks-search'],
        params: SpotifyAudiobooksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-chapter'],
        params: SpotifyChapterParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyChapterResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-episodes-search'],
        params: SpotifyEpisodesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyEpisodesSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-featured-charts-by-country'],
        params: SpotifyFeaturedChartsByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-genre'],
        params: SpotifyGenreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyGenreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-home'],
        params: SpotifyHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyHomeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-playlist'],
        params: SpotifyPlaylistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-playlists-search'],
        params: SpotifyPlaylistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-popular-by-country'],
        params: SpotifyPopularByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPopularByCountryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profile'],
        params: SpotifyProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profile-followers'],
        params: SpotifyProfileFollowersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileFollowersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profile-playlists'],
        params: SpotifyProfilePlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-profiles-search'],
        params: SpotifyProfilesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilesSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-search'],
        params: SpotifySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-section'],
        params: SpotifySectionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySectionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-shows-search'],
        params: SpotifyShowsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyShowsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-track'],
        params: SpotifyTrackParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-track-recommended'],
        params: SpotifyTrackRecommendedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackRecommendedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-track-similar-albums'],
        params: SpotifyTrackSimilarAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['spotify-tracks-search'],
        params: SpotifyTracksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTracksSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-categories'],
        params: SpotifyPodcastsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-charts'],
        params: SpotifyPodcastsChartsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsChartsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-episode'],
        params: SpotifyPodcastsEpisodeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-home'],
        params: SpotifyPodcastsHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsHomeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-search'],
        params: SpotifyPodcastsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-show'],
        params: SpotifyPodcastsShowParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-show-episodes'],
        params: SpotifyPodcastsShowEpisodesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-podcasts-show-recommendations'],
        params: SpotifyPodcastsShowRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-album'],
        params: SpotifyAlbumParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-album-tracks'],
        params: SpotifyAlbumTracksParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumTracksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-albums-search'],
        params: SpotifyAlbumsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAlbumsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist'],
        params: SpotifyArtistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist-albums'],
        params: SpotifyArtistAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistAlbumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist-playlists'],
        params: SpotifyArtistPlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artist-related'],
        params: SpotifyArtistRelatedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-artists-search'],
        params: SpotifyArtistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyArtistsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-audiobook'],
        params: SpotifyAudiobookParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-audiobook-chapters'],
        params: SpotifyAudiobookChaptersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-audiobooks-search'],
        params: SpotifyAudiobooksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-chapter'],
        params: SpotifyChapterParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyChapterResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-episodes-search'],
        params: SpotifyEpisodesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyEpisodesSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-featured-charts-by-country'],
        params: SpotifyFeaturedChartsByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-genre'],
        params: SpotifyGenreParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyGenreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-home'],
        params: SpotifyHomeParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyHomeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-playlist'],
        params: SpotifyPlaylistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-playlists-search'],
        params: SpotifyPlaylistsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-popular-by-country'],
        params: SpotifyPopularByCountryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyPopularByCountryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profile'],
        params: SpotifyProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profile-followers'],
        params: SpotifyProfileFollowersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfileFollowersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profile-playlists'],
        params: SpotifyProfilePlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-profiles-search'],
        params: SpotifyProfilesSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyProfilesSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-search'],
        params: SpotifySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-section'],
        params: SpotifySectionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifySectionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-shows-search'],
        params: SpotifyShowsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyShowsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-track'],
        params: SpotifyTrackParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-track-recommended'],
        params: SpotifyTrackRecommendedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackRecommendedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-track-similar-albums'],
        params: SpotifyTrackSimilarAlbumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['spotify-tracks-search'],
        params: SpotifyTracksSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SpotifyTracksSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class SpotifyClient(CrawloraClient):
    def __enter__(self) -> SpotifyClient: ...
    @overload
    def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesTextResponseParams]) -> str: ...
    @overload
    def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesDefaultParams]) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsTextResponseParams]) -> str: ...
    @overload
    def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsDefaultParams]) -> SpotifyPodcastsChartsResponse: ...
    @overload
    def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeTextResponseParams]) -> str: ...
    @overload
    def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeDefaultParams]) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeTextResponseParams]) -> str: ...
    @overload
    def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeDefaultParams]) -> SpotifyPodcastsHomeResponse: ...
    @overload
    def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchTextResponseParams]) -> str: ...
    @overload
    def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchDefaultParams]) -> SpotifyPodcastsSearchResponse: ...
    @overload
    def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowTextResponseParams]) -> str: ...
    @overload
    def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowDefaultParams]) -> SpotifyPodcastsShowResponse: ...
    @overload
    def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesTextResponseParams]) -> str: ...
    @overload
    def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesDefaultParams]) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsTextResponseParams]) -> str: ...
    @overload
    def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsDefaultParams]) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    def album(self, **params: Unpack[SpotifyAlbumStreamParams]) -> BinaryIO: ...
    @overload
    def album(self, **params: Unpack[SpotifyAlbumTextResponseParams]) -> str: ...
    @overload
    def album(self, **params: Unpack[SpotifyAlbumDefaultParams]) -> SpotifyAlbumResponse: ...
    @overload
    def album_tracks(self, **params: Unpack[SpotifyAlbumTracksStreamParams]) -> BinaryIO: ...
    @overload
    def album_tracks(self, **params: Unpack[SpotifyAlbumTracksTextResponseParams]) -> str: ...
    @overload
    def album_tracks(self, **params: Unpack[SpotifyAlbumTracksDefaultParams]) -> SpotifyAlbumTracksResponse: ...
    @overload
    def albums_search(self, **params: Unpack[SpotifyAlbumsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def albums_search(self, **params: Unpack[SpotifyAlbumsSearchTextResponseParams]) -> str: ...
    @overload
    def albums_search(self, **params: Unpack[SpotifyAlbumsSearchDefaultParams]) -> SpotifyAlbumsSearchResponse: ...
    @overload
    def artist(self, **params: Unpack[SpotifyArtistStreamParams]) -> BinaryIO: ...
    @overload
    def artist(self, **params: Unpack[SpotifyArtistTextResponseParams]) -> str: ...
    @overload
    def artist(self, **params: Unpack[SpotifyArtistDefaultParams]) -> SpotifyArtistResponse: ...
    @overload
    def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsTextResponseParams]) -> str: ...
    @overload
    def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsDefaultParams]) -> SpotifyArtistAlbumsResponse: ...
    @overload
    def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsTextResponseParams]) -> str: ...
    @overload
    def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsDefaultParams]) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    def artist_related(self, **params: Unpack[SpotifyArtistRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def artist_related(self, **params: Unpack[SpotifyArtistRelatedTextResponseParams]) -> str: ...
    @overload
    def artist_related(self, **params: Unpack[SpotifyArtistRelatedDefaultParams]) -> SpotifyArtistRelatedResponse: ...
    @overload
    def artists_search(self, **params: Unpack[SpotifyArtistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def artists_search(self, **params: Unpack[SpotifyArtistsSearchTextResponseParams]) -> str: ...
    @overload
    def artists_search(self, **params: Unpack[SpotifyArtistsSearchDefaultParams]) -> SpotifyArtistsSearchResponse: ...
    @overload
    def audiobook(self, **params: Unpack[SpotifyAudiobookStreamParams]) -> BinaryIO: ...
    @overload
    def audiobook(self, **params: Unpack[SpotifyAudiobookTextResponseParams]) -> str: ...
    @overload
    def audiobook(self, **params: Unpack[SpotifyAudiobookDefaultParams]) -> SpotifyAudiobookResponse: ...
    @overload
    def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersStreamParams]) -> BinaryIO: ...
    @overload
    def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersTextResponseParams]) -> str: ...
    @overload
    def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersDefaultParams]) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchStreamParams]) -> BinaryIO: ...
    @overload
    def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchTextResponseParams]) -> str: ...
    @overload
    def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchDefaultParams]) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    def chapter(self, **params: Unpack[SpotifyChapterStreamParams]) -> BinaryIO: ...
    @overload
    def chapter(self, **params: Unpack[SpotifyChapterTextResponseParams]) -> str: ...
    @overload
    def chapter(self, **params: Unpack[SpotifyChapterDefaultParams]) -> SpotifyChapterResponse: ...
    @overload
    def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchStreamParams]) -> BinaryIO: ...
    @overload
    def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchTextResponseParams]) -> str: ...
    @overload
    def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchDefaultParams]) -> SpotifyEpisodesSearchResponse: ...
    @overload
    def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryStreamParams]) -> BinaryIO: ...
    @overload
    def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryTextResponseParams]) -> str: ...
    @overload
    def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryDefaultParams]) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    def genre(self, **params: Unpack[SpotifyGenreStreamParams]) -> BinaryIO: ...
    @overload
    def genre(self, **params: Unpack[SpotifyGenreTextResponseParams]) -> str: ...
    @overload
    def genre(self, **params: Unpack[SpotifyGenreDefaultParams]) -> SpotifyGenreResponse: ...
    @overload
    def home(self, **params: Unpack[SpotifyHomeStreamParams]) -> BinaryIO: ...
    @overload
    def home(self, **params: Unpack[SpotifyHomeTextResponseParams]) -> str: ...
    @overload
    def home(self, **params: Unpack[SpotifyHomeDefaultParams]) -> SpotifyHomeResponse: ...
    @overload
    def playlist(self, **params: Unpack[SpotifyPlaylistStreamParams]) -> BinaryIO: ...
    @overload
    def playlist(self, **params: Unpack[SpotifyPlaylistTextResponseParams]) -> str: ...
    @overload
    def playlist(self, **params: Unpack[SpotifyPlaylistDefaultParams]) -> SpotifyPlaylistResponse: ...
    @overload
    def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchTextResponseParams]) -> str: ...
    @overload
    def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchDefaultParams]) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryStreamParams]) -> BinaryIO: ...
    @overload
    def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryTextResponseParams]) -> str: ...
    @overload
    def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryDefaultParams]) -> SpotifyPopularByCountryResponse: ...
    @overload
    def profile(self, **params: Unpack[SpotifyProfileStreamParams]) -> BinaryIO: ...
    @overload
    def profile(self, **params: Unpack[SpotifyProfileTextResponseParams]) -> str: ...
    @overload
    def profile(self, **params: Unpack[SpotifyProfileDefaultParams]) -> SpotifyProfileResponse: ...
    @overload
    def profile_followers(self, **params: Unpack[SpotifyProfileFollowersStreamParams]) -> BinaryIO: ...
    @overload
    def profile_followers(self, **params: Unpack[SpotifyProfileFollowersTextResponseParams]) -> str: ...
    @overload
    def profile_followers(self, **params: Unpack[SpotifyProfileFollowersDefaultParams]) -> SpotifyProfileFollowersResponse: ...
    @overload
    def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsTextResponseParams]) -> str: ...
    @overload
    def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsDefaultParams]) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    def profiles_search(self, **params: Unpack[SpotifyProfilesSearchStreamParams]) -> BinaryIO: ...
    @overload
    def profiles_search(self, **params: Unpack[SpotifyProfilesSearchTextResponseParams]) -> str: ...
    @overload
    def profiles_search(self, **params: Unpack[SpotifyProfilesSearchDefaultParams]) -> SpotifyProfilesSearchResponse: ...
    @overload
    def search(self, **params: Unpack[SpotifySearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[SpotifySearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[SpotifySearchDefaultParams]) -> SpotifySearchResponse: ...
    @overload
    def section(self, **params: Unpack[SpotifySectionStreamParams]) -> BinaryIO: ...
    @overload
    def section(self, **params: Unpack[SpotifySectionTextResponseParams]) -> str: ...
    @overload
    def section(self, **params: Unpack[SpotifySectionDefaultParams]) -> SpotifySectionResponse: ...
    @overload
    def shows_search(self, **params: Unpack[SpotifyShowsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def shows_search(self, **params: Unpack[SpotifyShowsSearchTextResponseParams]) -> str: ...
    @overload
    def shows_search(self, **params: Unpack[SpotifyShowsSearchDefaultParams]) -> SpotifyShowsSearchResponse: ...
    @overload
    def track(self, **params: Unpack[SpotifyTrackStreamParams]) -> BinaryIO: ...
    @overload
    def track(self, **params: Unpack[SpotifyTrackTextResponseParams]) -> str: ...
    @overload
    def track(self, **params: Unpack[SpotifyTrackDefaultParams]) -> SpotifyTrackResponse: ...
    @overload
    def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedStreamParams]) -> BinaryIO: ...
    @overload
    def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedTextResponseParams]) -> str: ...
    @overload
    def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedDefaultParams]) -> SpotifyTrackRecommendedResponse: ...
    @overload
    def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsTextResponseParams]) -> str: ...
    @overload
    def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsDefaultParams]) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    def tracks_search(self, **params: Unpack[SpotifyTracksSearchStreamParams]) -> BinaryIO: ...
    @overload
    def tracks_search(self, **params: Unpack[SpotifyTracksSearchTextResponseParams]) -> str: ...
    @overload
    def tracks_search(self, **params: Unpack[SpotifyTracksSearchDefaultParams]) -> SpotifyTracksSearchResponse: ...

class AsyncSpotifyClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncSpotifyClient: ...
    spotify: _AsyncSpotifyGroup
    @overload
    async def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesDefaultParams]) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    async def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsTextResponseParams]) -> str: ...
    @overload
    async def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsDefaultParams]) -> SpotifyPodcastsChartsResponse: ...
    @overload
    async def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeTextResponseParams]) -> str: ...
    @overload
    async def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeDefaultParams]) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    async def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeTextResponseParams]) -> str: ...
    @overload
    async def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeDefaultParams]) -> SpotifyPodcastsHomeResponse: ...
    @overload
    async def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchTextResponseParams]) -> str: ...
    @overload
    async def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchDefaultParams]) -> SpotifyPodcastsSearchResponse: ...
    @overload
    async def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowTextResponseParams]) -> str: ...
    @overload
    async def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowDefaultParams]) -> SpotifyPodcastsShowResponse: ...
    @overload
    async def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesTextResponseParams]) -> str: ...
    @overload
    async def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesDefaultParams]) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    async def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsDefaultParams]) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    async def album(self, **params: Unpack[SpotifyAlbumStreamParams]) -> BinaryIO: ...
    @overload
    async def album(self, **params: Unpack[SpotifyAlbumTextResponseParams]) -> str: ...
    @overload
    async def album(self, **params: Unpack[SpotifyAlbumDefaultParams]) -> SpotifyAlbumResponse: ...
    @overload
    async def album_tracks(self, **params: Unpack[SpotifyAlbumTracksStreamParams]) -> BinaryIO: ...
    @overload
    async def album_tracks(self, **params: Unpack[SpotifyAlbumTracksTextResponseParams]) -> str: ...
    @overload
    async def album_tracks(self, **params: Unpack[SpotifyAlbumTracksDefaultParams]) -> SpotifyAlbumTracksResponse: ...
    @overload
    async def albums_search(self, **params: Unpack[SpotifyAlbumsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def albums_search(self, **params: Unpack[SpotifyAlbumsSearchTextResponseParams]) -> str: ...
    @overload
    async def albums_search(self, **params: Unpack[SpotifyAlbumsSearchDefaultParams]) -> SpotifyAlbumsSearchResponse: ...
    @overload
    async def artist(self, **params: Unpack[SpotifyArtistStreamParams]) -> BinaryIO: ...
    @overload
    async def artist(self, **params: Unpack[SpotifyArtistTextResponseParams]) -> str: ...
    @overload
    async def artist(self, **params: Unpack[SpotifyArtistDefaultParams]) -> SpotifyArtistResponse: ...
    @overload
    async def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    async def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsTextResponseParams]) -> str: ...
    @overload
    async def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsDefaultParams]) -> SpotifyArtistAlbumsResponse: ...
    @overload
    async def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    async def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsTextResponseParams]) -> str: ...
    @overload
    async def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsDefaultParams]) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    async def artist_related(self, **params: Unpack[SpotifyArtistRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def artist_related(self, **params: Unpack[SpotifyArtistRelatedTextResponseParams]) -> str: ...
    @overload
    async def artist_related(self, **params: Unpack[SpotifyArtistRelatedDefaultParams]) -> SpotifyArtistRelatedResponse: ...
    @overload
    async def artists_search(self, **params: Unpack[SpotifyArtistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def artists_search(self, **params: Unpack[SpotifyArtistsSearchTextResponseParams]) -> str: ...
    @overload
    async def artists_search(self, **params: Unpack[SpotifyArtistsSearchDefaultParams]) -> SpotifyArtistsSearchResponse: ...
    @overload
    async def audiobook(self, **params: Unpack[SpotifyAudiobookStreamParams]) -> BinaryIO: ...
    @overload
    async def audiobook(self, **params: Unpack[SpotifyAudiobookTextResponseParams]) -> str: ...
    @overload
    async def audiobook(self, **params: Unpack[SpotifyAudiobookDefaultParams]) -> SpotifyAudiobookResponse: ...
    @overload
    async def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersStreamParams]) -> BinaryIO: ...
    @overload
    async def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersTextResponseParams]) -> str: ...
    @overload
    async def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersDefaultParams]) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    async def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchTextResponseParams]) -> str: ...
    @overload
    async def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchDefaultParams]) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    async def chapter(self, **params: Unpack[SpotifyChapterStreamParams]) -> BinaryIO: ...
    @overload
    async def chapter(self, **params: Unpack[SpotifyChapterTextResponseParams]) -> str: ...
    @overload
    async def chapter(self, **params: Unpack[SpotifyChapterDefaultParams]) -> SpotifyChapterResponse: ...
    @overload
    async def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchTextResponseParams]) -> str: ...
    @overload
    async def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchDefaultParams]) -> SpotifyEpisodesSearchResponse: ...
    @overload
    async def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryStreamParams]) -> BinaryIO: ...
    @overload
    async def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryTextResponseParams]) -> str: ...
    @overload
    async def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryDefaultParams]) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    async def genre(self, **params: Unpack[SpotifyGenreStreamParams]) -> BinaryIO: ...
    @overload
    async def genre(self, **params: Unpack[SpotifyGenreTextResponseParams]) -> str: ...
    @overload
    async def genre(self, **params: Unpack[SpotifyGenreDefaultParams]) -> SpotifyGenreResponse: ...
    @overload
    async def home(self, **params: Unpack[SpotifyHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def home(self, **params: Unpack[SpotifyHomeTextResponseParams]) -> str: ...
    @overload
    async def home(self, **params: Unpack[SpotifyHomeDefaultParams]) -> SpotifyHomeResponse: ...
    @overload
    async def playlist(self, **params: Unpack[SpotifyPlaylistStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist(self, **params: Unpack[SpotifyPlaylistTextResponseParams]) -> str: ...
    @overload
    async def playlist(self, **params: Unpack[SpotifyPlaylistDefaultParams]) -> SpotifyPlaylistResponse: ...
    @overload
    async def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchTextResponseParams]) -> str: ...
    @overload
    async def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchDefaultParams]) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    async def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryStreamParams]) -> BinaryIO: ...
    @overload
    async def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryTextResponseParams]) -> str: ...
    @overload
    async def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryDefaultParams]) -> SpotifyPopularByCountryResponse: ...
    @overload
    async def profile(self, **params: Unpack[SpotifyProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def profile(self, **params: Unpack[SpotifyProfileTextResponseParams]) -> str: ...
    @overload
    async def profile(self, **params: Unpack[SpotifyProfileDefaultParams]) -> SpotifyProfileResponse: ...
    @overload
    async def profile_followers(self, **params: Unpack[SpotifyProfileFollowersStreamParams]) -> BinaryIO: ...
    @overload
    async def profile_followers(self, **params: Unpack[SpotifyProfileFollowersTextResponseParams]) -> str: ...
    @overload
    async def profile_followers(self, **params: Unpack[SpotifyProfileFollowersDefaultParams]) -> SpotifyProfileFollowersResponse: ...
    @overload
    async def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    async def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsTextResponseParams]) -> str: ...
    @overload
    async def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsDefaultParams]) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    async def profiles_search(self, **params: Unpack[SpotifyProfilesSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def profiles_search(self, **params: Unpack[SpotifyProfilesSearchTextResponseParams]) -> str: ...
    @overload
    async def profiles_search(self, **params: Unpack[SpotifyProfilesSearchDefaultParams]) -> SpotifyProfilesSearchResponse: ...
    @overload
    async def search(self, **params: Unpack[SpotifySearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[SpotifySearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[SpotifySearchDefaultParams]) -> SpotifySearchResponse: ...
    @overload
    async def section(self, **params: Unpack[SpotifySectionStreamParams]) -> BinaryIO: ...
    @overload
    async def section(self, **params: Unpack[SpotifySectionTextResponseParams]) -> str: ...
    @overload
    async def section(self, **params: Unpack[SpotifySectionDefaultParams]) -> SpotifySectionResponse: ...
    @overload
    async def shows_search(self, **params: Unpack[SpotifyShowsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def shows_search(self, **params: Unpack[SpotifyShowsSearchTextResponseParams]) -> str: ...
    @overload
    async def shows_search(self, **params: Unpack[SpotifyShowsSearchDefaultParams]) -> SpotifyShowsSearchResponse: ...
    @overload
    async def track(self, **params: Unpack[SpotifyTrackStreamParams]) -> BinaryIO: ...
    @overload
    async def track(self, **params: Unpack[SpotifyTrackTextResponseParams]) -> str: ...
    @overload
    async def track(self, **params: Unpack[SpotifyTrackDefaultParams]) -> SpotifyTrackResponse: ...
    @overload
    async def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedStreamParams]) -> BinaryIO: ...
    @overload
    async def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedTextResponseParams]) -> str: ...
    @overload
    async def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedDefaultParams]) -> SpotifyTrackRecommendedResponse: ...
    @overload
    async def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    async def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsTextResponseParams]) -> str: ...
    @overload
    async def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsDefaultParams]) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    async def tracks_search(self, **params: Unpack[SpotifyTracksSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def tracks_search(self, **params: Unpack[SpotifyTracksSearchTextResponseParams]) -> str: ...
    @overload
    async def tracks_search(self, **params: Unpack[SpotifyTracksSearchDefaultParams]) -> SpotifyTracksSearchResponse: ...

class _AsyncSpotifyGroup:
    @overload
    async def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def podcasts_categories(self, **params: Unpack[SpotifyPodcastsCategoriesDefaultParams]) -> SpotifyPodcastsCategoriesResponse: ...
    @overload
    async def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsTextResponseParams]) -> str: ...
    @overload
    async def podcasts_charts(self, **params: Unpack[SpotifyPodcastsChartsDefaultParams]) -> SpotifyPodcastsChartsResponse: ...
    @overload
    async def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeTextResponseParams]) -> str: ...
    @overload
    async def podcasts_episode(self, **params: Unpack[SpotifyPodcastsEpisodeDefaultParams]) -> SpotifyPodcastsEpisodeResponse: ...
    @overload
    async def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeTextResponseParams]) -> str: ...
    @overload
    async def podcasts_home(self, **params: Unpack[SpotifyPodcastsHomeDefaultParams]) -> SpotifyPodcastsHomeResponse: ...
    @overload
    async def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchTextResponseParams]) -> str: ...
    @overload
    async def podcasts_search(self, **params: Unpack[SpotifyPodcastsSearchDefaultParams]) -> SpotifyPodcastsSearchResponse: ...
    @overload
    async def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowTextResponseParams]) -> str: ...
    @overload
    async def podcasts_show(self, **params: Unpack[SpotifyPodcastsShowDefaultParams]) -> SpotifyPodcastsShowResponse: ...
    @overload
    async def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesTextResponseParams]) -> str: ...
    @overload
    async def podcasts_show_episodes(self, **params: Unpack[SpotifyPodcastsShowEpisodesDefaultParams]) -> SpotifyPodcastsShowEpisodesResponse: ...
    @overload
    async def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def podcasts_show_recommendations(self, **params: Unpack[SpotifyPodcastsShowRecommendationsDefaultParams]) -> SpotifyPodcastsShowRecommendationsResponse: ...
    @overload
    async def album(self, **params: Unpack[SpotifyAlbumStreamParams]) -> BinaryIO: ...
    @overload
    async def album(self, **params: Unpack[SpotifyAlbumTextResponseParams]) -> str: ...
    @overload
    async def album(self, **params: Unpack[SpotifyAlbumDefaultParams]) -> SpotifyAlbumResponse: ...
    @overload
    async def album_tracks(self, **params: Unpack[SpotifyAlbumTracksStreamParams]) -> BinaryIO: ...
    @overload
    async def album_tracks(self, **params: Unpack[SpotifyAlbumTracksTextResponseParams]) -> str: ...
    @overload
    async def album_tracks(self, **params: Unpack[SpotifyAlbumTracksDefaultParams]) -> SpotifyAlbumTracksResponse: ...
    @overload
    async def albums_search(self, **params: Unpack[SpotifyAlbumsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def albums_search(self, **params: Unpack[SpotifyAlbumsSearchTextResponseParams]) -> str: ...
    @overload
    async def albums_search(self, **params: Unpack[SpotifyAlbumsSearchDefaultParams]) -> SpotifyAlbumsSearchResponse: ...
    @overload
    async def artist(self, **params: Unpack[SpotifyArtistStreamParams]) -> BinaryIO: ...
    @overload
    async def artist(self, **params: Unpack[SpotifyArtistTextResponseParams]) -> str: ...
    @overload
    async def artist(self, **params: Unpack[SpotifyArtistDefaultParams]) -> SpotifyArtistResponse: ...
    @overload
    async def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    async def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsTextResponseParams]) -> str: ...
    @overload
    async def artist_albums(self, **params: Unpack[SpotifyArtistAlbumsDefaultParams]) -> SpotifyArtistAlbumsResponse: ...
    @overload
    async def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    async def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsTextResponseParams]) -> str: ...
    @overload
    async def artist_playlists(self, **params: Unpack[SpotifyArtistPlaylistsDefaultParams]) -> SpotifyArtistPlaylistsResponse: ...
    @overload
    async def artist_related(self, **params: Unpack[SpotifyArtistRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def artist_related(self, **params: Unpack[SpotifyArtistRelatedTextResponseParams]) -> str: ...
    @overload
    async def artist_related(self, **params: Unpack[SpotifyArtistRelatedDefaultParams]) -> SpotifyArtistRelatedResponse: ...
    @overload
    async def artists_search(self, **params: Unpack[SpotifyArtistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def artists_search(self, **params: Unpack[SpotifyArtistsSearchTextResponseParams]) -> str: ...
    @overload
    async def artists_search(self, **params: Unpack[SpotifyArtistsSearchDefaultParams]) -> SpotifyArtistsSearchResponse: ...
    @overload
    async def audiobook(self, **params: Unpack[SpotifyAudiobookStreamParams]) -> BinaryIO: ...
    @overload
    async def audiobook(self, **params: Unpack[SpotifyAudiobookTextResponseParams]) -> str: ...
    @overload
    async def audiobook(self, **params: Unpack[SpotifyAudiobookDefaultParams]) -> SpotifyAudiobookResponse: ...
    @overload
    async def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersStreamParams]) -> BinaryIO: ...
    @overload
    async def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersTextResponseParams]) -> str: ...
    @overload
    async def audiobook_chapters(self, **params: Unpack[SpotifyAudiobookChaptersDefaultParams]) -> SpotifyAudiobookChaptersResponse: ...
    @overload
    async def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchTextResponseParams]) -> str: ...
    @overload
    async def audiobooks_search(self, **params: Unpack[SpotifyAudiobooksSearchDefaultParams]) -> SpotifyAudiobooksSearchResponse: ...
    @overload
    async def chapter(self, **params: Unpack[SpotifyChapterStreamParams]) -> BinaryIO: ...
    @overload
    async def chapter(self, **params: Unpack[SpotifyChapterTextResponseParams]) -> str: ...
    @overload
    async def chapter(self, **params: Unpack[SpotifyChapterDefaultParams]) -> SpotifyChapterResponse: ...
    @overload
    async def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchTextResponseParams]) -> str: ...
    @overload
    async def episodes_search(self, **params: Unpack[SpotifyEpisodesSearchDefaultParams]) -> SpotifyEpisodesSearchResponse: ...
    @overload
    async def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryStreamParams]) -> BinaryIO: ...
    @overload
    async def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryTextResponseParams]) -> str: ...
    @overload
    async def featured_charts_by_country(self, **params: Unpack[SpotifyFeaturedChartsByCountryDefaultParams]) -> SpotifyFeaturedChartsByCountryResponse: ...
    @overload
    async def genre(self, **params: Unpack[SpotifyGenreStreamParams]) -> BinaryIO: ...
    @overload
    async def genre(self, **params: Unpack[SpotifyGenreTextResponseParams]) -> str: ...
    @overload
    async def genre(self, **params: Unpack[SpotifyGenreDefaultParams]) -> SpotifyGenreResponse: ...
    @overload
    async def home(self, **params: Unpack[SpotifyHomeStreamParams]) -> BinaryIO: ...
    @overload
    async def home(self, **params: Unpack[SpotifyHomeTextResponseParams]) -> str: ...
    @overload
    async def home(self, **params: Unpack[SpotifyHomeDefaultParams]) -> SpotifyHomeResponse: ...
    @overload
    async def playlist(self, **params: Unpack[SpotifyPlaylistStreamParams]) -> BinaryIO: ...
    @overload
    async def playlist(self, **params: Unpack[SpotifyPlaylistTextResponseParams]) -> str: ...
    @overload
    async def playlist(self, **params: Unpack[SpotifyPlaylistDefaultParams]) -> SpotifyPlaylistResponse: ...
    @overload
    async def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchTextResponseParams]) -> str: ...
    @overload
    async def playlists_search(self, **params: Unpack[SpotifyPlaylistsSearchDefaultParams]) -> SpotifyPlaylistsSearchResponse: ...
    @overload
    async def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryStreamParams]) -> BinaryIO: ...
    @overload
    async def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryTextResponseParams]) -> str: ...
    @overload
    async def popular_by_country(self, **params: Unpack[SpotifyPopularByCountryDefaultParams]) -> SpotifyPopularByCountryResponse: ...
    @overload
    async def profile(self, **params: Unpack[SpotifyProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def profile(self, **params: Unpack[SpotifyProfileTextResponseParams]) -> str: ...
    @overload
    async def profile(self, **params: Unpack[SpotifyProfileDefaultParams]) -> SpotifyProfileResponse: ...
    @overload
    async def profile_followers(self, **params: Unpack[SpotifyProfileFollowersStreamParams]) -> BinaryIO: ...
    @overload
    async def profile_followers(self, **params: Unpack[SpotifyProfileFollowersTextResponseParams]) -> str: ...
    @overload
    async def profile_followers(self, **params: Unpack[SpotifyProfileFollowersDefaultParams]) -> SpotifyProfileFollowersResponse: ...
    @overload
    async def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    async def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsTextResponseParams]) -> str: ...
    @overload
    async def profile_playlists(self, **params: Unpack[SpotifyProfilePlaylistsDefaultParams]) -> SpotifyProfilePlaylistsResponse: ...
    @overload
    async def profiles_search(self, **params: Unpack[SpotifyProfilesSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def profiles_search(self, **params: Unpack[SpotifyProfilesSearchTextResponseParams]) -> str: ...
    @overload
    async def profiles_search(self, **params: Unpack[SpotifyProfilesSearchDefaultParams]) -> SpotifyProfilesSearchResponse: ...
    @overload
    async def search(self, **params: Unpack[SpotifySearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[SpotifySearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[SpotifySearchDefaultParams]) -> SpotifySearchResponse: ...
    @overload
    async def section(self, **params: Unpack[SpotifySectionStreamParams]) -> BinaryIO: ...
    @overload
    async def section(self, **params: Unpack[SpotifySectionTextResponseParams]) -> str: ...
    @overload
    async def section(self, **params: Unpack[SpotifySectionDefaultParams]) -> SpotifySectionResponse: ...
    @overload
    async def shows_search(self, **params: Unpack[SpotifyShowsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def shows_search(self, **params: Unpack[SpotifyShowsSearchTextResponseParams]) -> str: ...
    @overload
    async def shows_search(self, **params: Unpack[SpotifyShowsSearchDefaultParams]) -> SpotifyShowsSearchResponse: ...
    @overload
    async def track(self, **params: Unpack[SpotifyTrackStreamParams]) -> BinaryIO: ...
    @overload
    async def track(self, **params: Unpack[SpotifyTrackTextResponseParams]) -> str: ...
    @overload
    async def track(self, **params: Unpack[SpotifyTrackDefaultParams]) -> SpotifyTrackResponse: ...
    @overload
    async def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedStreamParams]) -> BinaryIO: ...
    @overload
    async def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedTextResponseParams]) -> str: ...
    @overload
    async def track_recommended(self, **params: Unpack[SpotifyTrackRecommendedDefaultParams]) -> SpotifyTrackRecommendedResponse: ...
    @overload
    async def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsStreamParams]) -> BinaryIO: ...
    @overload
    async def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsTextResponseParams]) -> str: ...
    @overload
    async def track_similar_albums(self, **params: Unpack[SpotifyTrackSimilarAlbumsDefaultParams]) -> SpotifyTrackSimilarAlbumsResponse: ...
    @overload
    async def tracks_search(self, **params: Unpack[SpotifyTracksSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def tracks_search(self, **params: Unpack[SpotifyTracksSearchTextResponseParams]) -> str: ...
    @overload
    async def tracks_search(self, **params: Unpack[SpotifyTracksSearchDefaultParams]) -> SpotifyTracksSearchResponse: ...

SpotifyPodcastsCategoriesDefaultParams = TypedDict('SpotifyPodcastsCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsCategoriesTextResponseParams = TypedDict('SpotifyPodcastsCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsCategoriesStreamParams = TypedDict('SpotifyPodcastsCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsChartsDefaultParams = TypedDict('SpotifyPodcastsChartsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'chart': NotRequired[Literal['top-podcasts', 'top-episodes', 'trending', 'arts', 'business', 'comedy', 'education', 'fiction', 'health-fitness', 'history', 'leisure', 'music', 'news', 'religion-spirituality', 'science', 'society-culture', 'sports', 'technology', 'true-crime', 'tv-film']],
    'region': NotRequired[Literal['ar', 'au', 'at', 'br', 'ca', 'cl', 'co', 'dk', 'fi', 'fr', 'de', 'in', 'id', 'ie', 'it', 'jp', 'mx', 'nz', 'no', 'ph', 'pl', 'es', 'se', 'nl', 'gb', 'us']],
    'limit': NotRequired[int],
}, total=False)

SpotifyPodcastsChartsTextResponseParams = TypedDict('SpotifyPodcastsChartsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'chart': NotRequired[Literal['top-podcasts', 'top-episodes', 'trending', 'arts', 'business', 'comedy', 'education', 'fiction', 'health-fitness', 'history', 'leisure', 'music', 'news', 'religion-spirituality', 'science', 'society-culture', 'sports', 'technology', 'true-crime', 'tv-film']],
    'region': NotRequired[Literal['ar', 'au', 'at', 'br', 'ca', 'cl', 'co', 'dk', 'fi', 'fr', 'de', 'in', 'id', 'ie', 'it', 'jp', 'mx', 'nz', 'no', 'ph', 'pl', 'es', 'se', 'nl', 'gb', 'us']],
    'limit': NotRequired[int],
}, total=False)

SpotifyPodcastsChartsStreamParams = TypedDict('SpotifyPodcastsChartsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'chart': NotRequired[Literal['top-podcasts', 'top-episodes', 'trending', 'arts', 'business', 'comedy', 'education', 'fiction', 'health-fitness', 'history', 'leisure', 'music', 'news', 'religion-spirituality', 'science', 'society-culture', 'sports', 'technology', 'true-crime', 'tv-film']],
    'region': NotRequired[Literal['ar', 'au', 'at', 'br', 'ca', 'cl', 'co', 'dk', 'fi', 'fr', 'de', 'in', 'id', 'ie', 'it', 'jp', 'mx', 'nz', 'no', 'ph', 'pl', 'es', 'se', 'nl', 'gb', 'us']],
    'limit': NotRequired[int],
}, total=False)

SpotifyPodcastsEpisodeDefaultParams = TypedDict('SpotifyPodcastsEpisodeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyPodcastsEpisodeTextResponseParams = TypedDict('SpotifyPodcastsEpisodeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyPodcastsEpisodeStreamParams = TypedDict('SpotifyPodcastsEpisodeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyPodcastsHomeDefaultParams = TypedDict('SpotifyPodcastsHomeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsHomeTextResponseParams = TypedDict('SpotifyPodcastsHomeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsHomeStreamParams = TypedDict('SpotifyPodcastsHomeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsSearchDefaultParams = TypedDict('SpotifyPodcastsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_audiobooks': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsSearchTextResponseParams = TypedDict('SpotifyPodcastsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_audiobooks': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsSearchStreamParams = TypedDict('SpotifyPodcastsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_audiobooks': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowDefaultParams = TypedDict('SpotifyPodcastsShowDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'include_content_capability_trait': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowTextResponseParams = TypedDict('SpotifyPodcastsShowTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'include_content_capability_trait': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowStreamParams = TypedDict('SpotifyPodcastsShowStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'include_content_capability_trait': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowEpisodesDefaultParams = TypedDict('SpotifyPodcastsShowEpisodesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowEpisodesTextResponseParams = TypedDict('SpotifyPodcastsShowEpisodesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowEpisodesStreamParams = TypedDict('SpotifyPodcastsShowEpisodesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPodcastsShowRecommendationsDefaultParams = TypedDict('SpotifyPodcastsShowRecommendationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
}, total=False)

SpotifyPodcastsShowRecommendationsTextResponseParams = TypedDict('SpotifyPodcastsShowRecommendationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
}, total=False)

SpotifyPodcastsShowRecommendationsStreamParams = TypedDict('SpotifyPodcastsShowRecommendationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
}, total=False)

SpotifyAlbumDefaultParams = TypedDict('SpotifyAlbumDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumTextResponseParams = TypedDict('SpotifyAlbumTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumStreamParams = TypedDict('SpotifyAlbumStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumTracksDefaultParams = TypedDict('SpotifyAlbumTracksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumTracksTextResponseParams = TypedDict('SpotifyAlbumTracksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumTracksStreamParams = TypedDict('SpotifyAlbumTracksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAlbumsSearchDefaultParams = TypedDict('SpotifyAlbumsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyAlbumsSearchTextResponseParams = TypedDict('SpotifyAlbumsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyAlbumsSearchStreamParams = TypedDict('SpotifyAlbumsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyArtistDefaultParams = TypedDict('SpotifyArtistDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistTextResponseParams = TypedDict('SpotifyArtistTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistStreamParams = TypedDict('SpotifyArtistStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistAlbumsDefaultParams = TypedDict('SpotifyArtistAlbumsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'type': NotRequired[Literal['album', 'single', 'compilation', 'appears_on', 'all']],
    'order': NotRequired[Literal['date_desc', 'date_asc', 'name_asc', 'name_desc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyArtistAlbumsTextResponseParams = TypedDict('SpotifyArtistAlbumsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'type': NotRequired[Literal['album', 'single', 'compilation', 'appears_on', 'all']],
    'order': NotRequired[Literal['date_desc', 'date_asc', 'name_asc', 'name_desc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyArtistAlbumsStreamParams = TypedDict('SpotifyArtistAlbumsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'type': NotRequired[Literal['album', 'single', 'compilation', 'appears_on', 'all']],
    'order': NotRequired[Literal['date_desc', 'date_asc', 'name_asc', 'name_desc']],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyArtistPlaylistsDefaultParams = TypedDict('SpotifyArtistPlaylistsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistPlaylistsTextResponseParams = TypedDict('SpotifyArtistPlaylistsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistPlaylistsStreamParams = TypedDict('SpotifyArtistPlaylistsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistRelatedDefaultParams = TypedDict('SpotifyArtistRelatedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistRelatedTextResponseParams = TypedDict('SpotifyArtistRelatedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistRelatedStreamParams = TypedDict('SpotifyArtistRelatedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyArtistsSearchDefaultParams = TypedDict('SpotifyArtistsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyArtistsSearchTextResponseParams = TypedDict('SpotifyArtistsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyArtistsSearchStreamParams = TypedDict('SpotifyArtistsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobookDefaultParams = TypedDict('SpotifyAudiobookDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyAudiobookTextResponseParams = TypedDict('SpotifyAudiobookTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyAudiobookStreamParams = TypedDict('SpotifyAudiobookStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyAudiobookChaptersDefaultParams = TypedDict('SpotifyAudiobookChaptersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobookChaptersTextResponseParams = TypedDict('SpotifyAudiobookChaptersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobookChaptersStreamParams = TypedDict('SpotifyAudiobookChaptersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyAudiobooksSearchDefaultParams = TypedDict('SpotifyAudiobooksSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyAudiobooksSearchTextResponseParams = TypedDict('SpotifyAudiobooksSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyAudiobooksSearchStreamParams = TypedDict('SpotifyAudiobooksSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyChapterDefaultParams = TypedDict('SpotifyChapterDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyChapterTextResponseParams = TypedDict('SpotifyChapterTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyChapterStreamParams = TypedDict('SpotifyChapterStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyEpisodesSearchDefaultParams = TypedDict('SpotifyEpisodesSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyEpisodesSearchTextResponseParams = TypedDict('SpotifyEpisodesSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyEpisodesSearchStreamParams = TypedDict('SpotifyEpisodesSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyFeaturedChartsByCountryDefaultParams = TypedDict('SpotifyFeaturedChartsByCountryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country_code': NotRequired[str],
    'content_id': NotRequired[Literal['CHARTS', 'POPULAR_ALBUMS', 'POPULAR_ARTISTS', 'TRENDING_SONGS']],
}, total=False)

SpotifyFeaturedChartsByCountryTextResponseParams = TypedDict('SpotifyFeaturedChartsByCountryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country_code': NotRequired[str],
    'content_id': NotRequired[Literal['CHARTS', 'POPULAR_ALBUMS', 'POPULAR_ARTISTS', 'TRENDING_SONGS']],
}, total=False)

SpotifyFeaturedChartsByCountryStreamParams = TypedDict('SpotifyFeaturedChartsByCountryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country_code': NotRequired[str],
    'content_id': NotRequired[Literal['CHARTS', 'POPULAR_ALBUMS', 'POPULAR_ARTISTS', 'TRENDING_SONGS']],
}, total=False)

SpotifyGenreDefaultParams = TypedDict('SpotifyGenreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyGenreTextResponseParams = TypedDict('SpotifyGenreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyGenreStreamParams = TypedDict('SpotifyGenreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'page_offset': NotRequired[int],
    'page_limit': NotRequired[int],
    'section_offset': NotRequired[int],
    'section_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyHomeDefaultParams = TypedDict('SpotifyHomeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'time_zone': NotRequired[str],
    'sp_t': NotRequired[str],
    'facet': NotRequired[str],
    'section_items_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyHomeTextResponseParams = TypedDict('SpotifyHomeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'time_zone': NotRequired[str],
    'sp_t': NotRequired[str],
    'facet': NotRequired[str],
    'section_items_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyHomeStreamParams = TypedDict('SpotifyHomeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'time_zone': NotRequired[str],
    'sp_t': NotRequired[str],
    'facet': NotRequired[str],
    'section_items_limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistDefaultParams = TypedDict('SpotifyPlaylistDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'enable_watch_feed_entrypoint': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistTextResponseParams = TypedDict('SpotifyPlaylistTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'enable_watch_feed_entrypoint': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistStreamParams = TypedDict('SpotifyPlaylistStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'enable_watch_feed_entrypoint': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistsSearchDefaultParams = TypedDict('SpotifyPlaylistsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistsSearchTextResponseParams = TypedDict('SpotifyPlaylistsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPlaylistsSearchStreamParams = TypedDict('SpotifyPlaylistsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyPopularByCountryDefaultParams = TypedDict('SpotifyPopularByCountryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country_code': NotRequired[str],
}, total=False)

SpotifyPopularByCountryTextResponseParams = TypedDict('SpotifyPopularByCountryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country_code': NotRequired[str],
}, total=False)

SpotifyPopularByCountryStreamParams = TypedDict('SpotifyPopularByCountryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country_code': NotRequired[str],
}, total=False)

SpotifyProfileDefaultParams = TypedDict('SpotifyProfileDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'playlist_limit': NotRequired[int],
    'artist_limit': NotRequired[int],
    'episode_limit': NotRequired[int],
}, total=False)

SpotifyProfileTextResponseParams = TypedDict('SpotifyProfileTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'playlist_limit': NotRequired[int],
    'artist_limit': NotRequired[int],
    'episode_limit': NotRequired[int],
}, total=False)

SpotifyProfileStreamParams = TypedDict('SpotifyProfileStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'playlist_limit': NotRequired[int],
    'artist_limit': NotRequired[int],
    'episode_limit': NotRequired[int],
}, total=False)

SpotifyProfileFollowersDefaultParams = TypedDict('SpotifyProfileFollowersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfileFollowersTextResponseParams = TypedDict('SpotifyProfileFollowersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfileFollowersStreamParams = TypedDict('SpotifyProfileFollowersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilePlaylistsDefaultParams = TypedDict('SpotifyProfilePlaylistsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilePlaylistsTextResponseParams = TypedDict('SpotifyProfilePlaylistsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilePlaylistsStreamParams = TypedDict('SpotifyProfilePlaylistsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': NotRequired[str],
    'uri': NotRequired[str],
    'url': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyProfilesSearchDefaultParams = TypedDict('SpotifyProfilesSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyProfilesSearchTextResponseParams = TypedDict('SpotifyProfilesSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyProfilesSearchStreamParams = TypedDict('SpotifyProfilesSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifySearchDefaultParams = TypedDict('SpotifySearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_artist_has_concerts_field': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
    'is_prefix': NotRequired[bool],
}, total=False)

SpotifySearchTextResponseParams = TypedDict('SpotifySearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_artist_has_concerts_field': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
    'is_prefix': NotRequired[bool],
}, total=False)

SpotifySearchStreamParams = TypedDict('SpotifySearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_artist_has_concerts_field': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
    'is_prefix': NotRequired[bool],
}, total=False)

SpotifySectionDefaultParams = TypedDict('SpotifySectionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifySectionTextResponseParams = TypedDict('SpotifySectionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifySectionStreamParams = TypedDict('SpotifySectionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyShowsSearchDefaultParams = TypedDict('SpotifyShowsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyShowsSearchTextResponseParams = TypedDict('SpotifyShowsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyShowsSearchStreamParams = TypedDict('SpotifyShowsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackDefaultParams = TypedDict('SpotifyTrackDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyTrackTextResponseParams = TypedDict('SpotifyTrackTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyTrackStreamParams = TypedDict('SpotifyTrackStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
}, total=False)

SpotifyTrackRecommendedDefaultParams = TypedDict('SpotifyTrackRecommendedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackRecommendedTextResponseParams = TypedDict('SpotifyTrackRecommendedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackRecommendedStreamParams = TypedDict('SpotifyTrackRecommendedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

SpotifyTrackSimilarAlbumsDefaultParams = TypedDict('SpotifyTrackSimilarAlbumsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'albums_only': NotRequired[bool],
}, total=False)

SpotifyTrackSimilarAlbumsTextResponseParams = TypedDict('SpotifyTrackSimilarAlbumsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'albums_only': NotRequired[bool],
}, total=False)

SpotifyTrackSimilarAlbumsStreamParams = TypedDict('SpotifyTrackSimilarAlbumsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'uri': NotRequired[str],
    'id': NotRequired[str],
    'limit': NotRequired[int],
    'albums_only': NotRequired[bool],
}, total=False)

SpotifyTracksSearchDefaultParams = TypedDict('SpotifyTracksSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyTracksSearchTextResponseParams = TypedDict('SpotifyTracksSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)

SpotifyTracksSearchStreamParams = TypedDict('SpotifyTracksSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'limit': NotRequired[int],
    'number_of_top_results': NotRequired[int],
    'include_audiobooks': NotRequired[bool],
    'include_pre_releases': NotRequired[bool],
    'include_album_pre_releases': NotRequired[bool],
    'include_authors': NotRequired[bool],
    'include_episode_content_ratings_v2': NotRequired[bool],
}, total=False)
