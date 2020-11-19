ox, oy = 0, 0
step_x, step_y = 2.5, 5.5
g = 9.81
t, dy = 0.00, 0.00
v = 1
dim = 50.0
check = 1

import time
def setup():
    size(500, 500)
    noStroke()
    time.gmtime(0)
    time.time()
    time.sleep(5)


def draw():
    background(0);
    
    global ox, oy, step_x, step_y, g, t, dy, check
    t = t+0.0005
    ox = ox + step_x

    #v = step_y+g*t
        
    
    if ox > width-35: 
        step_x = -step_x
    if oy > height-35: 
        step_y = -step_y
        dy=-dy;
    if oy > 475: 
        t=0
        dy=0
        check=0
    if ox < 0-15: 
        step_x = -step_x
    if oy < 0-15: 
        step_y = -step_y
        dy=-dy;
        
        
    dy = dy+0.5*g*sq(t)
    oy = oy+check*step_y*t+check*dy
    print(dy, oy)
    
    translate(ox, oy)
    fill(255,255,0)
    ellipse(0+dim/2, dim/2, dim/2, dim/2)

    


    
        #ellipse(ox, 250, 80, 80)
