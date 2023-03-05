x = 0
z = 0
def setup():
    size(600,600)
def draw():
    global x,z
    background(100)
    ellipse(z,x,50,50)
    x += 30
    z += 30
    if x >= 600:
        x = 0
        z = 0
