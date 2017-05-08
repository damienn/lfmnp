import Tkinter as tk
from PIL import Image, ImageTk
from LFM import NowPlaying

#lastfm username
username = "thirst_"
#size of window
windowsize = "200x200"
#xy location of window
windowloc = "0+0"
#string to initiate window
geo = windowsize + "+" + windowloc
#size of art, we set it to same size as window here
size = map(int, (windowsize.split("x")))
#delay before checking for updates
delay = 1000

#gets image from lfm np
def GetLFM():
    lfm = NowPlaying(username)
    art = Image.open(lfm.Cover).resize((size[0], size[1]), Image.ANTIALIAS)
    return art
#returns image of the art we just got resized to our window size

#initiate window class
root = tk.Tk()
root.title("albumart")
root.geometry(geo)
#remove decorations/titlebar from window
root.overrideredirect(1)
#setup our panel to display art
panel = tk.Label(root)
panel.pack(side="bottom", fill="both", expand="yes")
img = None

#loop that displays art and updates every second
def UpdateLoop():
    img = ImageTk.PhotoImage(GetLFM())
    panel.configure(image=img)
    panel.image = img
    root.update_idletasks()
    root.after(delay,UpdateLoop)

UpdateLoop()
root.mainloop()