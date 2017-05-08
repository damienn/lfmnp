import json, urllib2, cStringIO, StringIO
import PIL.Image

class NowPlaying:

    _API_KEY = "APIKEYHERE"
    _username = ""
    _numrecents = "1"
    _recents = ""
    _data = ""
    Artist = ""
    Song = ""
    Album = ""
    Cover = None

    def _unknowncover(self, color):
        img = PIL.Image.new("RGB", [1,1], color)
        cover = StringIO.StringIO()
        img.save(cover, format="JPEG")
        return cover

    def _updatedata(self):
        self._data = json.load(urllib2.urlopen(self._recents))['recenttracks']['track'][0]
        self.Artist = self._data['artist']['#text']
        self.Song = self._data['name']
        self.Album = self._data['album']['#text']

    def _albumart(self):
        try:
            nowplaying = self._data['@attr']['nowplaying']
        except:
            nowplaying = "false"
        art = self._data['image'][3]['#text']

        if nowplaying == "true":
            try:
                file = cStringIO.StringIO(urllib2.urlopen(art).read())
            except:
                file = self._unknowncover("gray")
        else:
            file = self._unknowncover("black")

        return file

    def updatedata(self):
        self._updatedata()
        self.Cover = self._albumart()

    def __init__(self, username):
        self._username = username
        self._recents = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user="+self._username+"&limit="+self._numrecents+"&api_key="+self._API_KEY+"&format=json"
        self.updatedata()