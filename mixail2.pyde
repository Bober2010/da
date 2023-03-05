x = 0
def setup():
    size(600,600)
def draw():
    global x
    background(100)
    ellipse(300,400,350,400)
    ellipse(300,100,300,300)
    ellipse(300,150,200,100)
    ellipse(250,70,50,50)
    ellipse(350,70,50,50)
    ellipse(100,250,100,x)
    ellipse(300,120,50,50)
    x += 5
    if x >= 300:
        x = 0
    
    
