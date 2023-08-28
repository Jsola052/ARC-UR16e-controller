import urx
import socket
from collections.abc import Iterable
import curses, time 
import threading

def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): 
                break
            time.sleep(0.05)
    finally:
        curses.endwin()
    return chr(ch)



HOST="192.168.1.54" #replace by the IP address of the UR robot
PORT=63352 #PORT used by robotiq gripper 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b"GET POS\n")
data = s.recv(2**10)
print("Gripper finger position is: ", data)

rob = urx.Robot("192.168.1.54")
def gripperMove(x,):

    s.sendall(b"SET POS "+ x + "\n")
    # s.sendall(b"SET ACT 1\n")
    return 0



# rob.set_tcp((0, 0, 0.1, 0, 0, 0))
# rob.set_payload(2, (0, 0, 0.1))

def home():
        rob.movej((-1.705, -0.081, -2.572, -2.071, -1.493, 4.148), 0.8, 0.75)

def moveF(): 
    rob.movej((0.877, -0.405, -0.970, 0.045, 0.45, 0.13), 0.8, 0.75)  
    

def moveL():
    rob.movej((0.877, -0.405, -0.970, 0.045, 0.45, 0.13), 0.8, 0.75)    
    rob.movej((-1.705, -0.081, -2.572, -2.071, -1.493, 4.148), 0.8, 0.75)
    
def getGripper():
    rob.movej((convertRad(-8.33), convertRad(-25.81), convertRad(67.26), convertRad(-131.29), convertRad(-89.22), convertRad(82.15)), 0.7, 0.70)
    t = True
    while(t == True):
        print("Enter 1")
        a = int(input())
        if (a == 1):
            t = False

        else:
            t = True
    rob.movej((convertRad(-8.33), convertRad(-21.32), convertRad(66.37), convertRad(-134.98), convertRad(-89.09), convertRad(81.95)), 0.1, 0.10)
    t = True
    while(t == True):
        print("Enter 1")
        a = int(input())
        if (a == 1):
            t = False

        else:
            t = True
            
    rob.movej((convertRad(-8.34), convertRad(-22.48), convertRad(66.88), convertRad(-134.47), convertRad(-89.08), convertRad(81.95)), 0.05, 0.051)
    rob.movej((convertRad(-8.34), convertRad(-23.61), convertRad(67.16), convertRad(-133.63), convertRad(-89.08), convertRad(81.95)), 0.05, 0.051)
    rob.movej((convertRad(-8.34), convertRad(-43.25), convertRad(55.94), convertRad(-102.63), convertRad(-89.00), convertRad(81.84)), 0.4, 0.6)
    
def returnGripper():
    rob.movej((convertRad(-8.34), convertRad(-43.25), convertRad(55.94), convertRad(-102.63), convertRad(-89.00), convertRad(81.84)), 0.8, 0.75)
    rob.movej((convertRad(-8.34), convertRad(-23.61), convertRad(67.16), convertRad(-133.63), convertRad(-89.08), convertRad(81.95)), 0.05, 0.051)
    rob.movej((convertRad(-8.34), convertRad(-22.48), convertRad(66.88), convertRad(-134.47), convertRad(-89.08), convertRad(81.95)), 0.05, 0.051)
    rob.movej((convertRad(-8.33), convertRad(-21.32), convertRad(66.37), convertRad(-134.98), convertRad(-89.09), convertRad(81.95)), 0.1, 0.10)
    t = True
    while(t == True):
        print("Enter 1")
        a = int(input())
        if (a == 1):
            t = False

        else:
            t = True
    rob.movej((convertRad(-8.34), convertRad(-23.61), convertRad(67.16), convertRad(-133.63), convertRad(-89.08), convertRad(81.95)), 0.05, 0.051)

def getMarker():
    rob.movej((convertRad(-36.66), convertRad(-50.90), convertRad(199.08), convertRad(-137.61), convertRad(-90.07), convertRad(143.32)), 0.5, 0.5)  
    t = True
    while(t == True):
        print("Enter 1")
        a = int(input())
        if (a == 1):
            t = False

        else:
            t = True   
    rob.movej((convertRad(-36.67), convertRad(-31.91), convertRad(99.75), convertRad(-157.27), convertRad(-90.16), convertRad(143.36)), 0.05, 0.1) 
    t = True
    while(t == True):
        print("Enter 1")
        a = int(input())
        if (a == 1):
            t = False

        else:
            t = True   
    rob.movej((convertRad(-36.68), convertRad(-32.90), convertRad(99.98), convertRad(-156.51), convertRad(-90.16), convertRad(143.36)), 0.05, 0.1) 
    rob.movej((convertRad(-36.67), convertRad(-33.99), convertRad(100.20), convertRad(-155.64), convertRad(-90.15), convertRad(143.36)), 0.05, 0.1)
    rob.movej((convertRad(-36.66), convertRad(-50.90), convertRad(199.08), convertRad(-137.61), convertRad(-90.07), convertRad(143.32)), 0.5, 0.5)  
    
def convertR():
    print("Enter coordinate: ")
    b = float(input())
    
    b = b*3.1416 / 180
    
    return b

def convertRad (b):
    
    b = b*3.1416 / 180
    
    return b


def lTest():
    rob.movej((convertRad(-99.52), convertRad(-92.18), convertRad(-94.63), convertRad(-83.85), convertRad(89.07), convertRad(234.68)), 0.8, 0.80)
    # rob.movel([-0.255, -0.451, 0.333, 2.66, -1.67, -0.03], 0.9, 0.9)
    # rob.movel([-0.289, -0.451, 0.333, 2.66, -1.67, -0.03], 0.9, 0.9)        
    # rob.movel([-0.255, -0.499, 0.333, 2.66, -1.67, -0.03], 0.9, 0.9)

def defaultPos():
    rob.movej((convertRad(-99.52), convertRad(-92.18), convertRad(-94.63), convertRad(-83.85), convertRad(89.07), convertRad(234.68)), 0.8, 0.80)

def planeMove(x, y, z):       
    while True :
        rob.movel([x, y, z, 2.66, -1.67, -0.03], 0.5,10)
        c = input_char("")
        if c.lower() in ['w']:
             x += 0.02
        elif c.lower() in ['s']:
            x -= 0.02
        elif c.lower() in ['a']:
            y += 0.02
        elif c.lower() in ['d']:
            y -= 0.02
        elif c.lower() in ['q']:
            z += 0.02
        elif c.lower() in ['e']:
            z -= 0.02
        elif c.lower() in ['x']:
            break
        

def move_and_stop(rob, direction):
    acceleration = 0.1
    time_duration = 4
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    
    # Calculate the speed vector based on the specified direction
    
    if direction == 'w':
        a = 0.1
        
    elif direction == 's':
        a = -0.1
        
    elif direction == 'a':
        b = 0.1
    elif direction == 'd':
        b = -0.1
    elif direction == 'q':
        c = 0.1
    elif direction == 'e':
        c = -0.1
    speed_vector = [a, b, c, d, e, f]
    rob.speedl(speed_vector, acceleration, time_duration)
        

            
# def test(x,y,z):
#     ans= input()
#     rob.movel([x, y, z, 2.66, -1.67, -0.03], 0.9, 0.9)
#     test2(ans,x,y,z)

        
        
    
            
        
def moveThread(l):    
    move_thread = None

    while True:
        c = input_char("")

    # If a move thread is already running, stop it
        if move_thread and move_thread.is_alive():
            move_thread.join()

        if c.lower() in ['w', 's', 'a', 'd', 'q', 'e']:
        # Start a new move thread
            move_thread = threading.Thread(target=move_and_stop, args=(rob, c))
            move_thread.start()

        elif c.lower() == 'x':
            rob.speedl((0,0,0,0,0,0),-0.1, 2)
            time.sleep(0.5)
            break    
        elif c.lower() == 'p':
            
            rob.speedl((0,0,0,0,0,0),-0.1, 2)
            time.sleep(2.5)
            print("Position ",l ,":",   rob.get_pos())
            time.sleep(2)
            l= l+1
        

# home()
# # Desired end-effector pose [x, y, z, rx, ry, rz] in meters and radians
# pose = [-0.25548, -0.45827, -0.03296, 0, 0, 0]

home()
defaultPos()
moveThread(0)
home()
rob.close()

# home() 

# getGripper()
# home()
# returnGripper()
# home()
# getMarker()
# home()

# lTest()


 
# rob.movej((convertRad(-97.16), convertRad(-117.12), convertRad(-46.51), convertRad(-69.87), convertRad(-270.16), convertRad(237.7)), 0.8, 0.75)

# rob.movej((convertRad(-97.16), convertRad(-119.5), convertRad(-78.87), convertRad(-69.87), convertRad(-270.16), convertRad(237.7)), 0.8, 0.75)

# rob.movej((convertRad(-97.20), convertRad(-97.20), convertRad(-102.97), convertRad(-69.87), convertRad(-270.16), convertRad(237.7)), 0.8, 0.75)
  
# # moveF()

# moveL()
    
# rob.movej((convertR(), convertR(), convertR(), convertR(), convertR(), convertR()), 0.8, 0.75)

# home()

# rob.movej((convertRad(-72.82), convertRad(-103.50), convertRad(-126.20), convertRad(-42.25), convertRad(-271.96), convertRad(296.21)), 0.8, 0.75)


        
# rob.movej((convertRad(-72.83), convertRad(-110.44), convertRad(-129.94), convertRad(-30.71), convertRad(-272.00), convertRad(296.23)), 0.1, 0.10)


# t = True
# while(t == True):
#     print("Enter 1")
#     a = int(input())
#     if (a == 1):
#         t = False

#     else:
#         t = True
        
# rob.movej((convertRad(-72.82), convertRad(-100.35), convertRad(-123.74), convertRad(-47.86), convertRad(-271.94), convertRad(296.20)), 0.8, 0.75)
# t = True
# while(t == True):
#     print("Enter 1")
#     a = int(input())
#     if (a == 1):
#         t = False

#     else:
#         t = True
        
# rob.movej((convertRad(-108.25), convertRad(-138.75), convertRad(-59.13), convertRad(-70.16), convertRad(-272.44), convertRad(237.71)), 0.9, 0.75)

# rob.movej((convertRad(-108.25), convertRad(-142.65), convertRad(-63.94), convertRad(-61.45), convertRad(-272.45), convertRad(237.74)), 0.9, 0.75)
# rob.movej((convertRad(-100.50), convertRad(-136.96), convertRad(-76.29), convertRad(-55.16), convertRad(-272.72), convertRad(245.53)), 0.9, 0.75)

# rob.movej((convertRad(-72.82), convertRad(-100.35), convertRad(-123.74), convertRad(-47.86), convertRad(-271.94), convertRad(296.20)), 0.8, 0.75)
# t = True
# while(t == True):
#     print("Enter 1")
#     a = int(input())
#     if (a == 1):
#         t = False

#     else:
#         t = True
        
# rob.movej((convertRad(-72.83), convertRad(-110.44), convertRad(-129.94), convertRad(-30.71), convertRad(-272.00), convertRad(296.23)), 0.1, 0.10)


# t = True
# while(t == True):
#     print("Enter 1")
#     a = int(input())
#     if (a == 1):
#         t = False

#     else:
#         t = True
        
# rob.movej((convertRad(-72.82), convertRad(-103.50), convertRad(-126.20), convertRad(-42.25), convertRad(-271.96), convertRad(296.21)), 0.8, 0.75)
    
# home()
