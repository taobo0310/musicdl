'''
Function:
    Implementation of SpotifyMusicClient Cookies Builder
Author:
    Zhenchao Jin
WeChat Official Account (微信公众号):
    Charles的皮卡丘
'''
import base64
import requests


'''settings'''
CLIENT_ID = 'Your Client ID Applied from https://developer.spotify.com/dashboard'
CLIENT_SECRET = 'Your Secret ID Applied from https://developer.spotify.com/dashboard'


'''buildspotifycookies'''
def buildspotifycookies():
    auth = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers, data = {"Authorization": f"Basic {auth}"}, {"grant_type": "client_credentials"}
    resp = (session := requests.Session()).post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    cookies: dict = requests.utils.dict_from_cookiejar(resp.cookies)
    cookies.update(requests.utils.dict_from_cookiejar(session.cookies))
    cookies.update(resp.json()); cookies.update({'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET})
    return cookies


'''tests'''
if __name__ == '__main__':
    print(buildspotifycookies())