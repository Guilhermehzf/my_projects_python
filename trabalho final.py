import random

from graphics import *
resolucaoX = 800
resolucaoY = 600
jan = GraphWin("launcher", 800, 600)
jan.setBackground("Black")

upline = Line(Point(0, 10), Point(800, 10))
upline.setWidth(10)
upline.setFill("White")
upline.draw(jan)

resolucao = Text(Point(380, 100), "Resolução")
resolucao.setSize(36)
resolucao.setFill("White")
resolucao.draw(jan)

resolucao1 = Text(Point(380, 200), "1366 x 768")
resolucao1.setSize(18)
resolucao1.setFill("White")
resolucao1.draw(jan)

resolucao2 = Text(Point(380, 250), "1280 x 768")
resolucao2.setSize(18)
resolucao2.setFill("White")
resolucao2.draw(jan)

resolucao3 = Text(Point(380, 300), "1280 x 720")
resolucao3.setSize(18)
resolucao3.setFill("White")
resolucao3.draw(jan)

resolucao4 = Text(Point(380, 350), "1024 x 768")
resolucao4.setSize(18)
resolucao4.setFill("White")
resolucao4.draw(jan)

resolucao5 = Text(Point(380, 400), "800 x 600")
resolucao5.setSize(18)
resolucao5.setFill("White")
resolucao5.draw(jan)

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
            resolucaoY = 700
        elif lin == 250:
            resolucaoX = 1280
            resolucaoY = 650
        elif lin == 300:
            resolucaoX = 1280
            resolucaoY = 640
        elif lin == 350:
            resolucaoX = 1024
            resolucaoY = 630
        elif lin == 400:
            resolucaoX = 800
            resolucaoY = 600
        break
resolucao_mod1 = 0
resolucao_mod2 = 0
resolucao_abr1 = 0
resolucao_abr2 = 0
resolucao_crl1 = 0
resolucao_crl2 = 0
resolucao_start1 = 0
resolucao_count1 = 0
resolucao_barrax = 0
resolucao_barray = 0
resolucao_barrax1 = 0
if resolucaoX == 1366 and resolucaoY == 700:
    resolucao_mod1 = 670
    resolucao_mod2 = 400
    resolucao_abr1 = 660
    resolucao_abr2 = 100
    resolucao_crl1 = 575
    resolucao_crl2 = 593
    resolucao_start1 = 680
    resolucao_count1 = 680
    resolucao_barrax = 790
    resolucao_barray = 230
if resolucaoX == 1280 and resolucaoY == 650:
    resolucao_mod1 = 600
    resolucao_mod2 = 400
    resolucao_abr1 = 590
    resolucao_abr2 = 100
    resolucao_crl1 = 505
    resolucao_crl2 = 523
    resolucao_start1 = 610
    resolucao_count1 = 610
    resolucao_barrax = 790
    resolucao_barray = 230
if resolucaoX == 1280 and resolucaoY == 640:
    resolucao_mod1 = 600
    resolucao_mod2 = 400
    resolucao_abr1 = 590
    resolucao_abr2 = 100
    resolucao_crl1 = 505
    resolucao_crl2 = 523
    resolucao_start1 = 610
    resolucao_count1 = 610
    resolucao_barrax = 790
    resolucao_barray = 230
if resolucaoX == 1024 and resolucaoY == 630:
    resolucao_mod1 = 500
    resolucao_mod2 = 400
    resolucao_abr1 = 490
    resolucao_abr2 = 100
    resolucao_crl1 = 405
    resolucao_crl2 = 423
    resolucao_start1 = 510
    resolucao_count1 = 510
    resolucao_barrax = 615
    resolucao_barray = 55
    resolucao_barrax1 = 626
if resolucaoX == 800 and resolucaoY == 600:
    resolucao_mod1 = 390
    resolucao_mod2 = 400
    resolucao_abr1 = 380
    resolucao_abr2 = 100
    resolucao_crl1 = 295
    resolucao_crl2 = 313
    resolucao_start1 = 400
    resolucao_count1 = 400
    resolucao_barrax = 580
    resolucao_barray = 20
    resolucao_barrax1 = 591
jan = GraphWin("Game Pong", resolucaoX, resolucaoY)
jan.setBackground("Black")

upline = Line(Point(0, 10), Point(resolucaoX, 10))
upline.setWidth(10)
upline.setFill("White")
upline.draw(jan)

loline = Line(Point(0, resolucaoY - 10), Point(resolucaoX, resolucaoY - 10))
loline.setWidth(10)
loline.setFill("White")
loline.draw(jan)
cor = ["White", "Black"]
x = 0
for i in range(0, 28):
    ret1 = i * 20 + 20
    ret = Rectangle(Point(395, ret1), Point(405, ret1 + 20))
    ret.setFill(cor[x])
    ret.draw(jan)
    if x == 0:
        x += 1
    elif x == 1:
        x -= 1
col = 390
lin = 300
raio = 10
cir = Circle(Point(col, lin), raio)
cir.setFill("White")
cir.draw(jan)

colIni = 20
linIni = 260
barra = Line(Point(colIni, linIni), Point(colIni, linIni + 70))
barra.setFill("White")
barra.setWidth(10)
barra.draw(jan)

colIni1 = resolucaoX - 20
linIni1 = resolucaoY/2 - 35
barra1 = Line(Point(colIni1, linIni1), Point(colIni1, linIni1 + 70))
barra1.setFill("White")
barra1.setWidth(10)
barra1.draw(jan)

pts = 0
pontos = Text(Point(300, 100), str(pts))
pontos.setSize(35)
pontos.setFill("White")
pontos.draw(jan)

pts1 = 0
pontos1 = Text(Point(500, 100), str(pts1))
pontos1.setSize(35)
pontos1.setFill("White")
pontos1.draw(jan)

ret3 = Rectangle(Point(0, 0), Point(1366, 768))
ret3.setFill("Black")
ret3.draw(jan)
abertura = "BEM VINDO AO NOSSO JOGO\n\n Selecione o modo de jogo"
abr = Text(Point(resolucao_abr1, resolucao_abr2), abertura)
abr.setSize(16)
abr.setFill("White")
abr.draw(jan)
modo = "Player 1 Vs Computador\n\n Player 1 Vs Player 2"
md1 = Text(Point(resolucao_mod1, resolucao_mod2), modo)
md1.setSize(12)
md1.setFill("White")
md1.draw(jan)

select = Circle(Point(resolucao_crl1, 381), 6)
select.setFill("White")
select.draw(jan)


check = 0
escolher = True
while escolher:
    tecla1 = jan.checkKey()
    if tecla1 == "Up" or tecla1 == "w":
        select.undraw()
        select = Circle(Point(resolucao_crl1 , 381), 6)
        select.setFill("White")
        select.draw(jan)
        check = 0
    if tecla1 == "Down" or tecla1 == "s":
        select.undraw()
        select = Circle(Point(resolucao_crl2, 416), 6)
        select.setFill("White")
        select.draw(jan)
        check = 1
    if tecla1 == "Return" and check == 0:
        abr.undraw()
        select.undraw()
        md1.undraw()
        escolher = False
    if tecla1 == "Return" and check == 1:
        abr.undraw()
        select.undraw()
        md1.undraw()
        escolher = False
    if tecla1 == "Escape":
        escolher = False
        jan.close()
start = Text(Point(resolucao_start1, 270), "START")
start.setSize(28)
start.setFill("White")
start.draw(jan)
for z in range(4, 1, -1):
    ct = z-1
    countdown = Text(Point(resolucao_count1, 310), str(ct))
    countdown.setSize(28)
    countdown.setFill("White")
    countdown.draw(jan)
    time.sleep(1)
    countdown.undraw()
start.undraw()
ret3.undraw()

defi = True
continuar = True
updown = 0
count = 0
passo = 10
ciclos = 0
while continuar:
    pontos.undraw()
    pontos = Text(Point(300, 100), str(pts))
    pontos.setSize(35)
    pontos.setFill("White")
    pontos.draw(jan)
    pontos1.undraw()
    pontos1 = Text(Point(500, 100), str(pts1))
    pontos1.setSize(35)
    pontos1.setFill("White")
    pontos1.draw(jan)


    if defi:
        passo = 10
        updown = random.randint(0, 1)
        if updown < 0.5:
            updown = 5
        else:
            updown = -5
        defi = False

    if passo > 20:
        count = 0
        passo = 20
    if count == 700:








        passo = passo*1.5
        count = 0
        ciclos += 1

    col -= passo
    lin += updown
    cir.undraw()
    cir = Circle(Point(col, lin), raio)
    cir.setFill("White")
    cir.draw(jan)

    if (lin - raio) <= resolucao_barray:
        updown = -updown

    if (lin + raio) >= resolucao_barrax:
        updown = -updown

    if col <= colIni + 20 and (lin + raio) >= linIni and (lin + raio) <= (linIni + 70):
        passo = -passo
    if col >= colIni1 - 20 and (lin + raio) >= linIni1 and (lin + raio) <= (linIni1 + 70):
        passo = -passo

    if col - raio <= 0:
        pts1 += 1
        col = 390
        lin = 300
        ret2 = Rectangle(Point(370, 200), Point(490, 390))
        ret2.setFill("Black")
        ret2.draw(jan)
        after = Text(Point(390, 300), '''         Pressione Enter para continuar
       Pressione ESC para finalizar''')
        after.setSize(16)
        after.setFill("White")
        after.draw(jan)
        tecla2 = jan.getKey()
        if tecla2 == "Return":
            defi = True
            after.undraw()
            ret2.undraw()
            continuar = True
            continue
        elif tecla2 == "Escape":
            continuar = False
    if col + raio >= 800:
        pts += 1
        col = 390
        lin = 300
        ret2 = Rectangle(Point(370, 200), Point(490, 390))
        ret2.setFill("Black")
        ret2.draw(jan)
        after = Text(Point(390, 300), '''         Pressione Enter para continuar
             Pressione ESC para finalizar''')
        after.setSize(16)
        after.setFill("White")
        after.draw(jan)
        tecla2 = jan.getKey()
        if tecla2 == "Return":
            defi = True
            after.undraw()
            ret2.undraw()
            continue
        elif tecla2 == "Escape":
            break
    tecla = jan.checkKey()

    if tecla == "Escape":
        continuar = False
        continue
    if tecla == "Up":
        if (linIni1 - 20) > 9:
            linIni1 -= 20

        barra1.undraw()
        barra1 = Line(Point(colIni1, linIni1), Point(colIni1, linIni1 + 70))
        barra1.setFill("White")
        barra1.setWidth(10)
        barra1.draw(jan)

    if tecla == "Down":
        if (linIni1 + 20 + 70) < resolucao_barrax1:
            linIni1 += 20
        elif (linIni1 + 20 + 70) >= resolucao_barrax1:
            linIni1 = resolucao_barrax1 - 20 - 70

        barra1.undraw()
        barra1 = Line(Point(colIni1, linIni1), Point(colIni1, linIni1 + 70))
        barra1.setFill("White")
        barra1.setWidth(10)
        barra1.draw(jan)
    if check == 1:
        if tecla == "w":
            if (linIni - 20) > 9:
                linIni -= 20

            barra.undraw()
            barra = Line(Point(20, linIni), Point(20, linIni + 70))
            barra.setFill("White")
            barra.setWidth(10)
            barra.draw(jan)

        if tecla == "s":
            if (linIni + 20 + 70) < resolucao_barrax1:
                linIni += 20
            elif (linIni + 20 + 70) >= resolucao_barrax1:
                linIni = resolucao_barrax1 - 20 - 70

            barra.undraw()
            barra = Line(Point(20, linIni), Point(20, linIni + 70))
            barra.setFill("White")
            barra.setWidth(10)
            barra.draw(jan)
    else:
        linIni = lin
        barra.undraw()
        barra = Line(Point(20, linIni - 30), Point(20, linIni + 70 - 30))
        barra.setFill("White")
        barra.setWidth(10)
        barra.draw(jan)
    count += 1

    time.sleep(0.07)
jan.close()
print(count)
print(ciclos)
print(passo)