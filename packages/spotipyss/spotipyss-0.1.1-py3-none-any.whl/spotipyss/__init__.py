"""Spotipy Simple Search"""
import spotipy
import jellyfish


from spotipy.oauth2 import SpotifyClientCredentials


def gen_queries(track, artist):
    """Generate queries based on track and artist name"""
    return [
        f"track:{track} artist:{artist}",
        f"{track}",
        f"{artist}",
        f"track:{track}",
        f"artist:{artist}",
    ]


def gen_tokenized_queries(track, artist):
    """Genearte queries by tokenizing artist name"""
    tokens = artist.split()
    result = []
    for token in tokens:
        result += gen_queries(track, token)
    result += gen_queries(track, artist)
    return result


def jaro_metric(lhs, rhs):
    """Returns if two strings are same in meaning by jaro metric"""
    return jellyfish.jaro_similarity(lhs, rhs) >= 0.9


def substr(lhs, rhs):
    """Returns if two string has sub-string relation"""
    return lhs in rhs or rhs in lhs


def get_most_matched(items, target_track, target_artist):
    """Returns the most matching track using track and artist name"""
    tracks = items["tracks"]["items"]
    for track in tracks:
        track_name = track["name"].lower()
        target_artist = target_artist.lower()
        target_track = target_track.lower()

        metrics = [jaro_metric, substr]
        track_matched = any(metric(track_name, target_track) for metric in metrics)
        if track_matched:
            for token in target_artist.split():
                artist_matched = any(metric(token, target_artist) for metric in metrics)
                if artist_matched:
                    return track

    return None


class SpotipySS:
    """Spotipy Wrapper for simple search"""

    def __init__(self, client_id=None, client_secret=None, language="ko"):
        self._sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=client_id, client_secret=client_secret
            ),
            language=language,
        )

    def search(self, track=None, artist=None):
        """Returns the most matching track by track name and artist"""
        queries = gen_tokenized_queries(track, artist)
        for query in queries:
            items = self._sp.search(query, limit=20)
            res = get_most_matched(items, track, artist)
            if res is not None:
                break
        if res is None:
            raise RuntimeError(f"cannot find track with {track} and {artist}")
        return Track(res)


class Track:
    """Helper class for tracks"""

    def __init__(self, track_json):
        self._json = track_json

    def spotify_uri(self):
        """Returns spotify uri of this track"""
        return self._json["external_urls"]["spotify"]

    def album_name(self):
        """Returns album name of this track"""
        return self._json["album"]["name"]
