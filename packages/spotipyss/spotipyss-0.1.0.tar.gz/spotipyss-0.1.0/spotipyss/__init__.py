import spotipy
import jellyfish


from spotipy.oauth2 import SpotifyClientCredentials

def gen_queries(track, artist):
    return [f'track:{track} artist:{artist}',
     f'{track}',
     f'{artist}',
     f'track:{track}',
     f'artist:{artist}']

def gen_tokenized_queries(track,artist):
    tokens = artist.split()
    result = []
    for token in tokens:
        result += gen_queries(track, token)
    result += gen_queries(track,artist)
    return result

def jaro_metric(lhs, rhs):
    return jellyfish.jaro_similarity(lhs,rhs) >= 0.9

def substr(lhs,rhs):
    return lhs in rhs or rhs in lhs

def get_most_matched(items, target_track, target_artist):
    tracks = items['tracks']['items']
    for track in tracks:
        track_name = track['name'].lower()
        target_artist = target_artist.lower()
        target_track = target_track.lower()

        metrics = [jaro_metric, substr]
        track_matched = any( metric(track_name, target_track) for metric in metrics)
        if track_matched:
            #for token in target_artist.split():
            #    artist_matched = any(metric(artist, target_artist) for metric in metrics)
            #    if artist_matched:
            return track

    return None

class SpotipySS:
    def __init__(self,client_id=None, client_secret=None, language='ko'):
        self._sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        ),language='ko')

    def search(self, track=None, artist=None):
        queries = gen_tokenized_queries(track, artist)
        for query in queries:
            items = self._sp.search(query, limit=20)
            res = get_most_matched(items, track,artist)
            if res is not None:
                break
        if res is None:
            raise Exception(f'cannot find track with {track} and {artist}')
        return Track(res)

class Track:
    def __init__(self, track_json):
        self._json = track_json
    def spotify_uri(self):
        return self._json['external_urls']['spotify']
    def album_name(self):
        return self._json['album']['name']
