from shutil import register_unpack_format
from uuid import RESERVED_FUTURE
from flask import Flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

app.secret_key = "cOqrUR7Wtd"
app.config['SESSION_COKKIE_NAME'] = 'Emre Cookie'

@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect():
    return 'redirect'

@app.route('/getTracks')
def getTracks():
    return "Some drake songs or something"

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "517cdd50fdde4800a8c0dfbd5d3e216a",
        client_secret = "e9d577ebc7d34a7f852211ec3dd31bec",
        redirect_uri = url_for('https://emrekardas.azurewebsites.net/redirectPage', _external = True),
        scope = "user-library-read"
    )
