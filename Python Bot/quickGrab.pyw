from PIL import ImageGrab
import os
import time

'''
Resolution used: 1080 x 1920
Website: http://www.freearcade.com/SushiGoRound.flash/SushiGoRound.html
Position: 4 arrow keys down
'''

x_pad = 608
y_pad = 337

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
