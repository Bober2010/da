z = 0
x = 0
c = 0
def setup():
    size(600,600)
def draw():
    global z,x,c
    fill(x,z,c)
    ellipse(300,300,150,150)
    z += 2
    x += 2
    c += 2
    if x >= 255:
        x = 0
        z = 0
        c = 0
