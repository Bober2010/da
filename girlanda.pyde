z = 0
x = 255
c = 0
def setup():
    size(600,600)
def draw():
    global z,x,c
    fill(random(z),random(x),random(c))
    ellipse(20,200,50,50)
    fill(random(c),random(z),random(x))
    ellipse(100,200,50,50)
    fill(random(x),random(x),random(c))
    ellipse(180,200,50,50)
    fill(random(z),random(x),random(c))
    ellipse(260,200,50,50)
    fill(random(c),random(z),random(x))
    ellipse(340,200,50,50)
    fill(random(c),random(x),random(z))
    ellipse(420,200,50,50)
    fill(random(x),random(c),random(z))
    ellipse(500,200,50,50)
    fill(random(c),random(x),random(x))
    ellipse(580,200,50,50)
    fill(random(z),random(x),random(c))
    ellipse(20,400,50,50)
    fill(random(c),random(z),random(x))
    ellipse(100,400,50,50)
    fill(random(z),random(x),random(x))
    ellipse(180,400,50,50)
    fill(random(x),random(x),random(z))
    ellipse(260,400,50,50)
    fill(random(z),random(x),random(x))
    ellipse(340,400,50,50)
    fill(random(x),random(z),random(c))
    ellipse(420,400,50,50)
    fill(random(c),random(x),random(z))
    ellipse(500,400,50,50)
    fill(random(z),random(c),random(x))
    ellipse(580,400,50,50)
    line(0,175,600,175)
    line(0,375,600,375)
