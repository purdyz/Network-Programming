from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import os
import time
import win32api, win32con

'''
Resolution used: 1080 x 1920
Website: http://www.freearcade.com/SushiGoRound.flash/SushiGoRound.html
Position: 4 arrow keys down start, 5 arrow keys down play
'''

x_pad = 608
y_pad = 337

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

sushiTypes = {2670:'onigiri',
              3143:'caliroll',
              2677:'gunkan',}

class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11598
    seat_4 = 10532
    seat_5 = 6782
    seat_6 = 9041

class Cord:
    f_shrimp = (44,351)
    f_rice = (95,351)
    f_nori = (24,406)
    f_roe = (93, 406)
    f_salmon = (45, 460)
    f_unagi = (101, 455)

    phone = (583,373)

    menu_toppings = (556,285)

    t_shrimp = (498,240)
    t_nori = (489,294)
    t_unagi = (576,239)
    t_roe = (568,296)
    t_salmon = (495,355)
    t_exit = (596,347)

    menu_rice = (544,300)
    buy_rice = (650, 298)

    delivery_norm = (493,307)
    

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
 #'.png', 'PNG')
    return im

def grab():
    box = (x_pad+1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
 #'.png', 'PNG')
    a = array(im.getcolors())
    a = a.sum()
    print ('a')
    return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ('click')

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

def mousePos(Cord):
    win32api.SetCursorPos((x_pad + Cord[0], y_pad + Cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)

def startGame():
    #location of first menu
    mousePos((306,200))
    leftClick()
    time.sleep(.1)

    #location of second menu
    mousePos((348,401))
    leftClick()
    time.sleep(.1)

    #location of third menu
    mousePos((585,439))
    leftClick()
    time.sleep(.1)

    #location of fourth menu
    mousePos((320,378))
    leftClick()
    time.sleep(.1)

def clear_tables():
    mousePos((82,209))
    leftClick()

    mousePos((182,209))
    leftClick()
    
    mousePos((284,209))
    leftClick()
    
    mousePos((387,204))
    leftClick()
    
    mousePos((485,205))
    leftClick()
    
    mousePos((586,209))
    leftClick()
    time.sleep(1)

def makeFood(food):
    if food == 'caliroll':
        print ('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print ('Making a onigiri')
        foodOnHand['rice'] -= 2 
        foodOnHand['nori'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print ('Making a gunkan')
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)

def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        # Time sleep?
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (118, 83, 85):
            print ('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
 
             
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (159, 159, 159):
            print ('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (109, 123, 127):
            print ('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                #print (s + ' is low and needs to be replenished')
                buyFood(i)

def get_seat_one():
    box = (27+x_pad,63+y_pad,27+63+x_pad,63+16+y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print ('a')
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    print (a)
    return a
 
def get_seat_two():
    box = (128+x_pad,63+y_pad,128+63+x_pad,63+16+y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print ('a')
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    print (a)
    return a
 
def get_seat_three():
    box = (229+x_pad,63+y_pad,229+63+x_pad,63+16+y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print ('a')
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    print (a)
    return a
 
def get_seat_four():
    box = (330+x_pad,63+y_pad,330+63+x_pad,63+16+y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print ('a')
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    print (a)
    return a
 
def get_seat_five():
    box = (431+x_pad,63+y_pad,431+63+x_pad,63+16+y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print ('a')
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    print (a)
    return a
 
def get_seat_six():
    box = (532+x_pad,63+y_pad,532+63+x_pad,63+16+y_pad)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print ('a')
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    print (a)
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

def check_bubs():
 
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes[s1]:
            #print ('table 1 is occupied and needs' + sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print ('sushi not found! sushiType = ')
 
    else:
        print ('Table 1 unoccupied')
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes[s2]:
            #print ('table 2 is occupied and needs ' + sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print ('sushi not found! sushiType = ')
 
    else:
        print ('Table 2 unoccupied')
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes[s3]:
            #print ('table 3 is occupied and needs ' + sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print ('sushi not found! sushiType = ')
 
    else:
        print ('Table 3 unoccupied')
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes[s4]:
            #print ('table 4 is occupied and needs ' + sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print ('sushi not found! sushiType = ')
 
    else:
        print ('Table 4 unoccupied')
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes[s5]:
            #print ('table 5 is occupied and needs ' + sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print ('sushi not found! sushiType = ')
 
    else:
        print ('Table 5 unoccupied')
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes[s6]:
            #print ('table 1 is occupied and needs ' + sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print ('sushi not found! sushiType = ')
 

    else:
        print ('Table 6 unoccupied')
 
    clear_tables()    

def main():
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()


