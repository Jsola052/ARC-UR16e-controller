import urx
import curses, time 
import time
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

robot = urx.Robot("192.168.1.54")
def planeMove2():
    waypoint_stack = []
    for waypoint in waypoint_stack:
        robot.speedl(waypoint, 0.1, 1)
    while True:
        c = input_char("")
        if c.lower() in ['w']:
            waypoint_stack.append((0.1, 0, 0, 0, 0, 0))
            break
        elif c.lower() in ['s']:
            waypoint_stack.append((-0.1, 0, 0, 0, 0, 0))
            break
        elif c.lower() in ['a']:
            waypoint_stack.append((0, 0.1, 0, 0, 0, 0))
            break
        elif c.lower() in ['d']:
            waypoint_stack.append((0, -0.1, 0, 0, 0, 0))
            break
        elif c.lower() in ['q']:
            waypoint_stack.append((0, 0, 0.1, 0, 0, 0))
            break
        elif c.lower() in ['e']:
            waypoint_stack.append((0, 0, -0.1, 0, 0, 0))
            break
        elif c.lower() in ['x']:
            break
    
    for waypoint in waypoint_stack:
        robot.speedl(waypoint, 0.1, 0.25)
    return planeMove2()

# planeMove2()
# robot.close()



import threading

def move_and_stop(robot, direction):
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
    robot.speedl(speed_vector, acceleration, time_duration)
    
def convertRad (b):
    
    b = b*3.1416 / 180
    
    return b
def defaultPos():
    
    robot.movej((convertRad(-99.52), convertRad(-92.18), convertRad(-94.63), convertRad(-83.85), convertRad(89.07), convertRad(234.68)), 0.8, 0.80)
    
defaultPos()
move_thread = None

while True:
    c = input_char("")

    # If a move thread is already running, stop it
    if move_thread and move_thread.is_alive():
        move_thread.join()

    if c.lower() in ['w', 's', 'a', 'd', 'q', 'e']:
        # Start a new move thread
        move_thread = threading.Thread(target=move_and_stop, args=(robot, c))
        move_thread.start()

    elif c.lower() == 'x':
        break

# Close the robot connection
robot.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    