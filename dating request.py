from graphics import *

win = GraphWin("Quer namorar cmg", 900, 500)
win.setBackground(color_rgb(214, 64, 179))
texto_pergunta1 = 'Quer namorar comigo?🌹'
texto_pergunta = Text(Point(448, 140), texto_pergunta1)
texto_pergunta.setSize(30)
texto_pergunta.draw(win)

#parte do sim
#{
retangulo_sim = Rectangle(Point(350, 280), Point(150, 340))
retangulo_sim.setFill("white")
retangulo_sim.setOutline("black")
retangulo_sim.draw(win)

texto_sim = Text(Point(247, 313), 'SIM❤')
texto_sim.setSize(20)
texto_sim.draw(win)
#}
#fim do sim

#parte do não
#{
x = 750
x2 = x - 200
y = 340
y2 = y - 60
retangulo_nao = Rectangle(Point(x, y2), Point(x2, y))
retangulo_nao.setFill("white")
retangulo_nao.setOutline("black")
retangulo_nao.draw(win)

texto_nao = Text(Point(657, 313), 'NÃO😢')
texto_nao.setSize(20)
texto_nao.draw(win)
#}
#fim do não




while True:
    ponto = win.getMouse()



    if ponto.getY() > 280 and ponto.getY() < 340 and ponto.getX() < 350 and ponto.getX() > 150:
        win2 = GraphWin("Outros", 900, 500)
        win2.setBackground(color_rgb(247, 136, 236))


        #texto aceito
        texto_aceito = Text(Point(440, 250), 'QUE ISSO LEK TMJ <3.')
        texto_aceito.setFill("black")
        texto_aceito.setSize(36)
        texto_aceito.draw(win2)
        #fim do texto aceito

        # texto rosa
        texto_rosa  = Text(Point(163, 275), '🌹\n'*1)
        texto_rosa.setFill("red")
        texto_rosa.setSize(36)
        texto_rosa.draw(win2)

        texto_rosa2 = Text(Point(718, 275), '🌹\n' * 1)
        texto_rosa2.setFill("red")
        texto_rosa2.setSize(36)
        texto_rosa2.draw(win2)

        texto_rosa3 = Text(Point(441, 301.1), '🌹' * 16)
        texto_rosa3.setFill("red")
        texto_rosa3.setSize(36)
        texto_rosa3.draw(win2)

        texto_rosa4 = Text(Point(441, 200), '🌹' * 16)
        texto_rosa4.setFill("red")
        texto_rosa4.setSize(36)
        texto_rosa4.draw(win2)
        while True:
            z = 24
            texto_sla1 = Text(Point(440, 150), '❤')
            texto_sla1.setFill("red")
            texto_sla1.setSize(z)
            texto_sla1.draw(win2)
            time.sleep(0.5)
            texto_sla1.undraw()

            texto_sla1 = Text(Point(440, 150), '❤')
            texto_sla1.setFill("red")
            texto_sla1.setSize(z+12)
            texto_sla1.draw(win2)
            time.sleep(0.5)
            texto_sla1.undraw()
            h = win2.checkMouse()
            if h != None:
                win2.close()
                win.close()


        # fim texto rosa
    if ponto.getY() > 280 and ponto.getY() < 340 and ponto.getX() < 750 and ponto.getX() > 550:
        from graphics import *
        import random

        win = GraphWin("Outros", 900, 500)
        win.setBackground(color_rgb(214, 64, 179))

        texto_pergunta = Text(Point(448, 140), texto_pergunta1)
        texto_pergunta.setSize(30)
        texto_pergunta.draw(win)

        # parte do sim
        # {
        retangulo_sim = Rectangle(Point(350, 280), Point(150, 340))
        retangulo_sim.setFill("white")
        retangulo_sim.setOutline("black")
        retangulo_sim.draw(win)

        texto_sim = Text(Point(247, 313), 'SIM❤')
        texto_sim.setSize(20)
        texto_sim.draw(win)
        # }
        # fim do sim

        # parte do não
        # {
        x = 750
        x2 = x - 200
        y = 340
        y2 = y - 60
        retangulo_nao = Rectangle(Point(x, y2), Point(x2, y))
        retangulo_nao.setFill("white")
        retangulo_nao.setOutline("black")
        retangulo_nao.draw(win)

        texto_nao = Text(Point(657, 313), 'NÃO😢')
        texto_nao.setSize(20)
        texto_nao.draw(win)
        # }
        # fim do não
        continue