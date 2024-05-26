import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# from pprint import pprint

CLIENT_ID = "f9e4c9bd10ea467185e22b5a8fd49a23"
CLIENT_SECRET = "369e29955cf54059b96a28907c3f3518"
REDIRECT_URI = "https://example.com/"
DISPLAY_NAME = "Suvam"

dates = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# dates = "2002-10-21"
year = dates.split("-")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{dates}")
# print(response.text)

billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
all_songs = soup.select(selector="h3", class_="c-title")
all_songs = [song.getText().strip("\t\n") for song in all_songs]
songs = [song for song in all_songs if song not in ["Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:", "Gains in Weekly Performance", "Additional Awards"]]
songs = songs[1:101]

# all_artists = soup.find_all(name="span", class_="c-label")
# all_artists = [artist.getText().strip("\t\n") for artist in all_artists]
# number_list = [str(item) for item in range(101)] + ["-", "NEW"]
# artists = [artist for artist in all_artists if artist not in number_list]

# print(songs)
# print(len(songs))
# print(artists.index("Kellie Coffey"))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope="playlist-modify-private", show_dialog=True, cache_path="token.txt", username=DISPLAY_NAME))
# user_id = sp.current_user()
user_id = sp.current_user()["id"]
# print(user_id)

song_uris = []
for song in songs:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        # print(result["tracks"]["items"][0]["uri"])
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{dates} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
