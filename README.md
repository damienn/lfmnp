# lfmnp
Minimal LastFM lib for displaying NowPlaying info
First you will need to replace APIKEY your own LastFM API key from https://www.last.fm/api/account/create

Call the class NowPlaying with your LFM Username, it will immediately pull data from LFM, you can update the class at anytime to refresh now playing info with updatedata()

There are only a few properties in this small class:
Artist = Artist name as string
Song = Song title as string
Album = Album name as string
Cover = Album art as PIL image.
