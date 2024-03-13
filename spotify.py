import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = 'http://localhost'


sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope='playlist-read-private')

token_info = sp_oauth.get_access_token(as_dict=False)


sp = spotipy.Spotify(auth=token_info)


playlist_id = os.getenv("playlist_id")
playlist_info = sp.playlist_tracks(playlist_id)

all_musics = []

all_musics.extend(playlist_info['items'])

while playlist_info['next']:
    playlist_info = sp.next(playlist_info)
    all_musics.extend(playlist_info['items'])


file_path = 'playlist_info.txt'


with open(file_path, 'w', encoding='utf-8') as file:
    
    for track in all_musics:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        file.write(f'{track_name} - {artist_name}\n')

print(f'Info saved on: {file_path}')