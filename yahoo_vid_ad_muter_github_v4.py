# Mute ads on Yahoo View videos

# Works by detecting the color of a pixel in the cross-bar of the "A" in "Ad"
# in the upper left-hand corner. If it matches particular shades of white,
# mute the volume. When it no longer matches, unmute.

# Python 3.5.3, Windows 10

# May 27-29, 2017
# Author: E.M.A. Sundin

# verison 1 (May 27): dead end (just a few lines of code)
# version 2 (May 27): first working version
# version 3 (May 28): streamlined and prettified
# version 4 (May 29): took out wikipedia stuff

# using Pillow with python 3.5.3
# (installed with pip as "pillow", but imported here as "PIL")

from PIL import ImageGrab
import time
import win32api

ad_pix_x = 27
ad_pix_y = 25
ad_pix_colors = ((238,238,238),(237,237,237))

# time, in seconds, to sleep between iterations of main loop:
loop_period = 5



def get_pix_color(x,y):
    ''' Return the color, as an (R,G,B) tuple, of the color of pixel x,y '''
    # Ref: https://stackoverflow.com/a/6321120
    px = ImageGrab.grab().load()
    color = px[x,y]
    return color


def press_mute_key():
    ''' Mute the system volume by pressing the mute key through API '''
    # Ref: https://gist.github.com/chriskiehl/2906125 (very useful)
    win32api.keybd_event(0xAD, 0,0,0)


def main_loop():
    '''
    Mute Yahoo View ads (only works in fullscreen).

    (Get the pixel's color, check it against "ad" color.
    If ad, mute system audio.
    Rinse and repeat...forever.)
    '''

    is_muted = False
    
    while 1:
        color = get_pix_color(ad_pix_x,ad_pix_y)
        print("Current pix color:",color)
        print("is_muted = ",is_muted)

        if color in ad_pix_colors:
            print("This is an advert.")
            if is_muted is False:
                print("Muting volume")
                press_mute_key()
                is_muted = True    
            else:
                print("Already muted. Do nothing.")
                
        elif color not in ad_pix_colors:
            print("Not an advert.")
            if is_muted is True:
                print("Unmute!")
                press_mute_key()
                is_muted = False
            else:
                print("Already unmuted. Do nothing.")

        print("\n")     
        time.sleep(loop_period)
  

main_loop()

        
        
