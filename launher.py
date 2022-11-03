from graphics import *
resolucaoX = 800
resolucaoY = 600
jan = GraphWin("launcher",800,600)
jan.setBackground("Black")

upline = Line(Point(0, 10), Point(800, 10))
upline.setWidth(10)
upline.setFill("White")
upline.draw(jan)

start = Text(Point(380, 100), "Resolução")
start.setSize(36)
start.setFill("White")
start.draw(jan)

start = Text(Point(380, 200), "1366 x 768")
start.setSize(18)
start.setFill("White")
start.draw(jan)

start = Text(Point(380, 250), "1280 x 768")
start.setSize(18)
start.setFill("White")
start.draw(jan)

start = Text(Point(380, 300), "1280 x 720")
start.setSize(18)
start.setFill("White")
start.draw(jan)

start = Text(Point(380, 350), "1024 x 768")
start.setSize(18)
start.setFill("White")
start.draw(jan)

start = Text(Point(380, 400), "800 x 600")
start.setSize(18)
start.setFill("White")
start.draw(jan)

col = 300
lin = 200
pt = Point(col,lin)
select = Circle(pt,6)
select.setFill("white")
select.draw(jan)

loline = Line(Point(0, 590), Point(800, 590))
loline.setWidth(10)
loline.setFill("White")
loline.draw(jan)
escolher = True
while escolher:
    tecla1 = jan.checkKey()
    if tecla1 == "Up" and lin > 200:
        lin -= 50
        select.undraw()
        select = Circle(Point(300, lin), 6)
        select.setFill("White")
        select.draw(jan)
    if tecla1 == "Down" and lin < 400:
        lin += 50
        select.undraw()
        select = Circle(Point(300, lin), 6)
        select.setFill("White")
        select.draw(jan)
    if tecla1 == "Return":
        jan.close()
        if lin == 200:
            resolucaoX = 1366
            resolucaoY = 768
        elif lin == 250:
            resolucaoX = 1280
            resolucaoY = 768
        elif lin == 300:
            resolucaoX = 1280
            resolucaoY = 720
        elif lin == 350:
            resolucaoX = 1024
            resolucaoY = 768
        elif lin == 400:
            resolucaoX = 800
            resolucaoY = 600
        break
win = GraphWin("Resoluçao",resolucaoX, resolucaoY)
time.sleep(4)
win.close()