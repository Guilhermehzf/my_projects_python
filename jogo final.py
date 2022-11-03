#random
import random
#interface
n = ''
print('mgn0\nGHZ\n\t\t\t\t\033[1;33;40mDRAGON FIGHT\033[0m\t\t\t(beta)\n\t\t\t\t 竜との喧嘩')
input('\t\t pressione ENTER para continuar')
while 1:
    n = input('__________________________________________________________\n\t\t informe o seu nome para continuar: ')
    if len(n) > 20:
        print('__________________________________________________________\nO seu nome não pode ter mais de 20 caracteres.')
        continue
    if len(n) < 2:
        print('__________________________________________________________\nO seu nome deve ter pelo menos dois caracteres')
        continue
    else:
        break
y=1
while 1:
    x = input("\033[1;36mola {}, seja bem vindo ao DRAGON FIGHT, eu sou sua guia espirutual, meu nome é Aqua e vou te ensinar algumas funçoes do jogo,\n vamos para o nosso Tuturial ?\n a-yes b-no\nsua resposta: \033[m".format(n))
    if x== "b":
        input("\033[1;36mhmmm... tudo bem então tchau tchau aventureiro até a sua morte... opa não hahaha... até a proxima.\033[m")
        y=0
        break
    if x=="a":
        break
    elif x!="a"and "b":
        print("oshi ?")
        continue

if y==1:
    input("\033[1;36mAqua: yaaay!!,vamos la então aventureiro(a) {},vou te explicar como funciona os ataques, a recuperação e o gasto de mana e vida.\033[m".format(n))
    input("\033[1;36mo jogo conta com 5 feitiços, são eles:Bola de Luz, Flechas Mágicas, Espada Mágica, Heal Points e Magia das Trevas.\033[m")
    input("\033[1;36mE ai que entra o gasto de mana, cada feitiço gasta uma certa quantidade de mana.\nestou te entregando uma lista que mostra a quantidade de mana gasta por cada feitiço.")
    input("\033[1;36m\t\t\033[;1m  LISTA\033[m\n|-------------------------|\n|feitiço------------->mana|\n|Bola de Luz------------>4|\n|Flechas Mágicas-------->2|\n|Espada Mágica---------->4|\n|Heal Points------------>4|\n|Magia das Trevas------>10|\n|-------------------------|\n\t\033[;1mRECUPERAÇÃO DE MANA\033[m\n|Heal Mana--->concentração|\n|-------------------------|\033[m")
    print()
    input("\033[1;36mAqua: Bem agora que você conheçe todos os feitiços vou te explicar como usa-los. Para atacar qualquer inimigo basta você falar as inicias do feitiço.\033[m")
    input("\033[1;36mPor exemplo se eu quisesse atacar um inimigo conjurando uma bola de luz, eu teria que falar bdl,porem isso irá me custar 4 de mana e um turno\033[m ")
    input("\033[1;36me para você recupera-la basta eu falar hm, que tem um custo de um torno, pois você tem que se concentrar.\033[m")
    input("\033[1;36mquando você receber o dano de um ataque, dado por um inimigo e quiser regenerar sua vida basta conjurar o feitiço heal points(hp)\033[m")
    input("\033[1;36magora que eu te explique tudo vamos para o campo de treinamento para você aplicar o que eu te ensinei\033[m")
    mana=14
    life_Sorcerer=30

    vida_orc=40
    print("\t\t\033[;1mCAMPO DE TREINAMENTO\033[m")
    input("\033[1;36mAqua: essa aqui é a nossa treinadora de guerreiros, o nome dela é Darkness.\033[m")
    input("\033[1;33mDarkness: Ola aventureiro, eu sou a Darkness e vou te ensinar a atacar seus inimigos. \033[m")
    input("\033[1;33mDarkness: então vamos começar, vai pode me tratar como sua inimiga mortal\ne me lançe seu feitiço mais podereso S2.\033[m")
    input("\033[1;36mAqua: nãoo!, é claro que a Darkness iria fazer isso, ela faz isso com todos os avetureiros que vem aqui para treinar\033[m.")
    dano=input("\033[1;33mDarkness: poxa Aqua eu so queria ajuda-lo, tudo bem então, vamos usar outro alvo, esta vendo aquele orc, experimente lançar uma bola de luz nele\n\033[m")

    while 1:
        dano=input("\033[1;33mdigite seu feitiço: \033[m")
        if dano=="bdl":
            break
        elif dano!="bdl":
            print("oshi")
            continue

    while 1:
        print("\033[1;33mDarkness: boa você acetou ele em cheio tirou 8 de vida dele, porem você perdeu 4 de mana\033[m")
        input("---------------------------------------------------\nsua vida:30\t\t\tvida do orc:32\t\t\tsua mana:10")
        dano2=input("\033[1;33mDarkness: agora que você conseguiu acerta-lo com a bola de luz, tente lançar uma espada magíca\ndigite seu feitiço: \033[m")
        if dano2=="em":
            break
        elif dano2!="em":
            print("oush")
            continue
    while 1:
        input("---------------------------------------------------\nsua vida:20\t\t\tvida do orc:23\t\t\tsua mana:6")
        print("\033[1;33mDarkness: nice bakuretsu, você deu muito dano nele, porem esse orc atacou você tirando-o 10 de vida\033[m")

        break
    while 1:
        cura=input("\033[1;33mtente usar heal points para se curar\ndigite seu feitiço: \033[m")
        if cura=="hp":
            break
        elif cura!="hp":
            print("oush")
            continue

    input("---------------------------------------------------\nsua vida:30\t\t\tvida do orc:23\t\t\tsua mana:2")
    print('\033[1;33mDarkness: boa você conseguiu recuperar toda a sua vida, porem isso da uma brecha para o orc ataca-lo \033[m')
    print("\033[1;33mmas por sorte ele acaba errando o ataque\033[m")
    input("\033[1;33magora é a sua vez de ataca-lo\033[m")

    while 1:

        dano3=input("\033[1;33mtente lançar flechas mágicas\ndigite seu feitiço: \033[m")
        if dano3=="fm":
            break
        elif dano3!="fm":
            print("oush")
            continue

    input("---------------------------------------------------\nsua vida:30\t\t\tvida do orc:19\t\t\tsua mana:0")
    print("\033[1;33mDarkness: boa agora você esta quase la\033[m")
    input("\033[1;33mvocê acabou zerando sua mana, com o ultimo feitiço\033[m")

    while 1:

        recarga=input("\033[1;33magora use Heal Mana para recarregar sua mana\ndigite seu feitiço: \033[m")
        if recarga=="hm":
            break
        elif recarga!="hm":
            print("oush")
            continue

    input("---------------------------------------------------\nsua vida:30\t\t\tvida do orc:19\t\t\tsua mana:10")
    print("\033[1;33mboa você conseguiu recuperar 10 de mana\033[m")

    while 1:

        m=input("\033[1;33magora aproveite para usar magia das trevas\ndigite seu feitiço: \033[m")
        if m=="mdt":
            break
        elif m!="mdt":
            print("oush")
            continue
    print("---------------------------------------------------\nsua vida:20\t\t\tvida do orc:0\t\t\tsua mana:0")
    input("\033[1;33mDarkness:Parabéns {} você conseguiu derrotar o orc,agora vamos para o nosso teste final\nlançe espada magica em mim.\033[m".format(n))
    while 1:
        gnd = input('\033[1;33mBate em mim bem forte, {} S2: \033[m'.format(n))
        if gnd == 'em':
            input("{}: eu conjuro espada má--".format(n))
            input("\033[1;32m Aqua: nãoo!, de novo a Darkness fazendo isso, imagena se eu não chega a tempo\nenfim tchau tchua {}, boa sorte com a sua aventura.\033[m".format(n))
            break
        elif gnd != 'em':
            print('\033[1;33mDarkness: vai la, me bate logo, {}, eu to te esperando...\033[m'.format(n))
            continue
#variaveis
x = 0
dragon = 150
vida = 100
mana = 40
dragon_total = 100
a = 1
resultado = 0
na = 'Narrador: '
bdl = 0
#gameplay

print('_________________\n\t\t\tlista de ataques:\n\n\t\t\t -Bola de Luz{4}\n\t\t\t -Flechas Mágicas{2}\n\t\t\t -Espada Mágica{6}\n\t\t\t -Heal Mana{concentração}\n\t\t\t -Heal Points{4}\n\t\t\t -Magia das Trevas{10}\n\t\t\t-Master Heal Points{20}\n\t\t\tOBS: para conjurar magia, digite as iniciais do encantamento')
while vida > 0 and dragon > 0:
    a = 1
    b = 0
    t = random.randint(1, 30)
    print('_______________\n\n',n+'-HP: {}\t\t\t\t{}-mana: {}\t\t\t\t\t\tdragon-HP: {}'.format(vida,n,mana,dragon,))
    a = input('\n\nescolha o seu ataque: ')
    if a != 'bdl' and a != 'fm' and a != 'em' and a != 'hm' and a != 'hp' and a != 'mdt' and a != 'mhp':
        a = 0
        print('{}{}, isto não é um encantamento válido, tente novamente'.format(na,n))
        continue
    if mana <= 0 and a != 'hm':
        print('{}Sem mana o sufuciente'.format(na))
    b = random.randint(1, 30)
    if b == 30:
        print('|--------------------|\n|---\033[0;32mACERTO CRÍTICO\033[m---|')
    if b == 1:
        print('|--------------------|\n|----\033[1;31mERRO CRITICO\033[m----|')
    if mana > 0 and a != 0:
        print('|--------------------|\n|ROLAGEM DE DADOS: {}\n|--------------------|'.format(b))
    if mana < 0 and a == 'hm':
        print('|--------------------|\n|ROLAGEM DE DADOS: {}\n|--------------------|'.format(b))
#Master Heal Points
    if a == 'mhp' and mana > 0 and b > 3:
        mana -= 20
        vida += 20
        print('narrador: você se lembra de uma lenda antiga que diz que você pode trocar sua força mágica por força vital. \nApós muito se consentrar, você enfraquece o seu esnírito para fortalecer o seu corpo.')
    if a == 'mhp' and mana > 0 and b <= 3:
        mana -= 10
        print('narrador: Você tenta transformar sua força espiritual em força vital\n no entanto, tudo o que você ganha com isso é fraquesa nas suas magículas\n a final, esse tipo de feitiço é muito instavel')
#Bola de Luz command
    if a == 'bdl'and b <= 10 and b != 1 and mana > 0:
        dragon -= 4
        mana -= 4
        print('{}Um pequeno feixe de luz surge de suas mãos, e se forma em direção do dragão. \n O ataque certamente surte eleito, porém parece ser longe do suficiente para derrota-lo'.format(na))
    if a == 'bdl' and b > 10 and b <= 20 and mana > 0:
        dragon -= 6
        mana -= 4
        print('{}Diante de suas mãos, uma fonte ardente de energia se forma;\n seu tamanho é semelhante a uma bola de boliche, e o calor emanado por ela se asemelha ao de uma fogueira.\n Esse golpe se manifesta em direção ao dragão, que parece ferido'.format(na))
    if a == 'bdl' and b > 20 and b <= 29 and mana > 0:
        dragon -= 8
        mana -= 4
        print(('{}Uma grande quantidade de energia se acumula em suas mãos.\n Um calor ofuscante surge, e por um momento tudo fica branco.\n Quando sua visão retorna, você ve diante de suas mãos uma bola luminosa gigante, que se aproxima em direção ao dragão, que fica visivelmente ferido'.format(na)))
    if a == 'bdl' and b == 30 and mana > 0:
        dragon -= 20
        mana -= 4
        print('{}Uma bola colossal de luz se forma em suas mãos.\n Por um momento, o espaço e o tempo parecem parar. \n O ataque se movimenta em grande velocidade até o dragâo, que parece consideravelmente derifo.\n Fumaça surge de sua pala quando ele se prepara para o seu próximo ataque'.format(na))
    if a == 'bdl' and b == 1 and mana > 0:
        mana -= mana/2
        print('{}você tenta lançar sua magia para o alvo, porém nada acontece.\n Com isso, sua visão embaça e, desorientado, percebe que uma boa parte da sua mana se foi'.format(na))

#Espada de Magía

    if a == 'em' and b <= 10 and b != 1 and mana > 0:
        dragon -= 6
        mana -= 6
        print('{}Uma espada mágica aparece de suas mãos; ela brilha constantemente com um brilho azul claro.\n Ao direcionar o ataque ao dragão, ele surte efeito, porêm nem tanto'.format(na))
    if a == 'em' and b > 10 and b <= 20 and mana > 0:
        dragon -= 9
        mana -= 6
        print('{}Diante das suas mãos, surge um brilho verde; então subtamente, uma grande quantidade de energia se forma no formato de uma espada.\n você tenta deferir um ataque ao dragão que o deixa ferido'.format(na))
    if a == 'em' and b > 20 and b <= 29 and mana > 0:
        dragon -= 12
        mana -= 6
        print('{}Uma energia vermelha se forma a partir de sua mana;\n a partir disso, uma espada de energia se forma, e voa em direção ao dragão'.format(na))
    if a == 'em' and b == 30 and mana > 0:
        dragon -= 28
        mana -= 6
        print('{}Você fecha os olhos, e ao abrir, uma espada gigante de energia vermelha se forma diante do dragão, que se machuca consideravelmente.\n A energia vívida forma uma explosão de poder mágico diante dos seus olhos'.format(na))
    if a == 'em' and b == 1 and mana > 0:
        mana -= mana/2
        print('{}você tenta lançar sua magia para o alvo, porém nada acontece.\n Com isso, sua visão embaça e, desorientado, percebe que uma boa parte da sua mana se foi'.format(na))

#comando Flechas Mágicas
    if a == 'fm' and b <= 10 and b != 1 and mana > 0:
        dragon -= 2
        mana -= 2
        print('{}Umaa flecha de luz surge em suas mãos e é lançada em direção ao dragão; \n por mais que o ataque tenha sido bem sucedido, mal parece que ele tomou um arranhão'.format(na))
    if a == 'fm'and b > 10 and b <= 20 and mana > 0:
        dragon -= 4
        mana -= 2
        print('{}Duas flechas de mana se lançam em direção ao dragão;\n cada uma delas atinge uma estremidade de seu corpo e as penetra'.format(na))
    if a == 'fm'and b > 20 and b <= 29 and mana > 0:
        dragon -= 8
        mana -= 2
        print('{}Três flechas de mana são geradas de seus dedos.\n Elas se lançam em direção ao dragão e perfuram sua barriga.\n Sangue negro pinga no chão e evapora, logo em seguida'.format(na))
    if a == 'fm' and b == 30 and mana > 0:
        dragon -= 16
        mana -= 2
        print('{}Uma saraivada de flechas luminosas surgem ao redor do dragão. \n Ele se grita e se contorce, tentando expulsa-las de seu corpo. \n notoriamente ele está ferido'.format(na))
    if a == 'fm' and b == 1 and mana > 0:
        mana -= mana/2
        print('{}você tenta lançar sua magia para o alvo, porém nada acontece.\n Com isso, sua visão embaça e, desorientado, percebe que uma boa parte da sua mana se foi'.format(na))

#comando Heal Mana
    if a == 'hm' and b <= 10 and b != 1:
        mana += 2
        print('{}Você foca a sua energia vital.\n com isso, o Universo lhe concede mais poder mágico. \n um pouco da sua força retorna '.format(na))
    if a == 'hm' and b > 10 and b <= 20:
        mana += 4
        print('{}Você foca sua vontade na criação do Universo\n uma leve briza bate em seu rosto e recarrega as suas energias'.format(na))
    if a == 'hm' and b > 20 and b <= 29:
        mana += 10
        print('{}Com um estrondo, súbito em seu peito, você sente as energias vindas da terra entrando pelos seus pés e indo até seu coração\n As suas forças retornam a você, a luta te chama.'.format(na))
    if a == 'hm' and b == 30:
        mana += 30
        print('{}Você se concentra com todas as suas forças em sua natureza mágica;\n Por conta de todo o seu esforço, o Universo lhe retribui com uma biza suave, e as suas forças retornam quase completamente.\n Você levanta o seu rosto novamente, pronto para mais uma luta'.format(na))
    if a == 'hm' and b == 1:
        mana -= mana/2
        print('{}Sua visão embaça. Desorientado, percebe que uma boa parte da sua mana se foi.\nO Universo, com quem você tanto contava, falhou com você'.format(na))

#comando Heal Points
    if a == 'hp' and b <= 10 and b != 1 and mana > 0:
        vida += 6
        mana -= 4
        print('{}uma pequena onda de cura te faz sentir um alívio sob sua dor.\n com isso, você consegue continuar lutando'.format(na))
    if a == 'hp' and b > 10 and b <= 20 and mana > 0:
        vida += 8
        mana -= 4
        print('{} Uma onda reconfortante de cura te toca;\n O alívio, suave como o beijo de uma musa, te envolve e te da forças para continuar'.format(na))
    if a == 'hp' and b > 20 and b <= 29 and mana > 0:
        vida += 10
        mana -= 4
        print('{} As forças de cura repousam sobre você\n você sente as bençãos das musas ressoando pelo seu corpo'.format(na))
    if a == 'hp' and b == 30 and mana > 0:
        vida += 60
        mana -= 4
        print('{}Você sente uma onda gigantesca de vigor. derrepente, uma luz brilha no interior de seu peito\n a voz de uma musa ecoa dentro de seu coração, e ela te chama: \n musa:',n+', ',n+'! Eu lhe entrego o poder para a vida. Levante-se e lute!' .format(na,n,n))
    if a == 'hp'  and b == 1  and mana > 0:
        vida -= vida/2
        print(na,'você tenta conjurar magia de cura, no entanto o inesperado acontece.\n o que deveria ser uma benção, se torna uma maldição, e a cura se transforma em veneno nas suas veias.\n você sente que boa parte da sua força vital se foi')

#comando da Magnia das Trevas
    if a =='mdt' and b <= 10 and b != 1 and mana > 0:
        dragon -= 10
        mana -= 10
        vida -= 5
        print('{}Uma onda negra surge de seus braços e se move em direção ao dragão\n a força é suficiente para lhe causar um dano perceptivel'.format(na))
    if a == 'mdt' and b > 10 and b <= 20 and mana > 0:
        dragon -= 20
        mana -= 10
        vida -= 10
        print('{}Uma fumaça escura se manifesta no ar e infesta todo o ambiente;\n com violência, essa fumaça invade o interior do dragão e faz com que ele se contorça de dor.\n ele está visivelmente ferido'.format(na))
    if a == 'mdt' and b > 20 and b <= 29 and mana > 0:
        dragon -= 30
        mana -= 10
        vida -= 10
        print('{} Uma onda escura toma conta do corpo do dragão e começa a sair por suas enormes narinas;\n essa onda começa a perfura-lo por dentro e drenar a sua vida.\n a medida que ele se contorce, o ambiente fica cada vez mais escuro, até que a escuridão passa e tudo retorna ao normal '.format(na))
    if a == 'mdt' and b == 30 and mana > 0:
        dragon -= 50
        mana -= 10
        print('{}Tudo fica escuro\n o ambiente se torna tenebroso e macabro\n uma voz desconhecida te chama, dizendo: \n -lorde {}, agradeço a você por ter me invocado. Vou consumir com alegria o banquete que o senhor me presenteou\n\n o sorriso macabro se transforma em um show de violênica e de terror.\n o dragão se contorce enquanto o lorde das trevas devora a sua alma e tira boa parte de sua força vital'.format(na,n))
    if a == 'mdt' and b == 1 and mana > 0:
        vida -= vida/2
        dragon -= vida/2
        print('{}Você se sente confuso por um momento;\n uma onda de fumaça negra surge de dentro de você e te consome de maneira brutal\n no entanto, você vê que o dragão também está sendo consumido pelo mesmo mal\n no fim, lietalmente o feitiço se voltou contra o feiticeiro.\n mesmo fraco, você ainda levanta e continua a luta'.format(na))
#continue
    input('__________________\ncontinue ')
    print('__________________')
    t = random.randint(1,30)
    ba = 0
#Ataques do dragão
    if dragon <= dragon_total/2:
        ba = random.randint(1, 4)

#Heal HP dragon
    if ba == 3 and dragon > 0 and mana > 0:
        t = 0
        dragon += random.randint(3,20)
        print('{}O dragão foca a suas magículas para regenerar vida'.format(na))
        continue
#Rajada Cortante
    if t > 3 and t <= 14 and a != 0 and dragon > 0 and mana > 0:
        vida -= 4
        print(random.choice(['narrador: O dragão bate suas asas colossais, e o vento que surge delas bate em você rasgando sua carne','narrador: As asas do dragão se movimentam, gerando lâminas de vento que lançam-se em sua direção','narrador: Por meio do movimento de suas asas grandiosas, o dragão invoca o vento para rasgar sua carne.\n o ferimento arde e sua pele sangra']))
        continue

#Garras de dragão
    if t > 14 and t <= 22 and a != 0 and dragon > 0 and mana > 0:
        vida -= 6
        print(random.choice(['narrador: O dragão levanta as suas garras, afiadas como aço, e defere um ataque contra você, cortando sua carne','narrador: As multiplas garras do dragão, grandes e afiadas como facas, se lançam em direção a você\n sangue quente escorre de sua barriga','narrador: As garras grandiosas do dragão cortam sua barriga.\n seu corpo inteiro arde em dor e agonia. O ataque te fere consideravelmente']))
        continue

#Cuspe flamejante
    if t > 22 and t <= 28 and a != 0 and dragon > 0 and mana > 0:
        vida -= 12
        print(random.choice(['narrador: Diante de seus olhos, uma enorme rajada de fogo se lança em direção a você.\n o calor e a dor são tamanhos que chegam a ser desnorteantes\n no entanto, uma vez que sua consciencia retorna, é possível ver que esse raio surgiu a partir do dragão', 'narrador: Um enorme raio de fogo surge a partir da boca do dragão.\n Esse fogo é lançado em sua direção em forma de raio, e faz arder a seu corpo.', 'uma bola de fogo surge na boca do dragão\n o calor envolve todo o ambiente. Você sente todo o seu corpo sendo envolvido pelas chnamas, e por mais que você tente defender com magia, o dano ainda é grande']))
        continue
#Erro crítico do dragâo
    if t <= 3 and a != 0 and dragon > 0 and mana > 0:
        print(na,'O dragão não se mexe, ele parece estar destraído por algum acaso. \nMesmo tendo tudo em vista parece que o sua ação anterior destraíu ele.\n Você aproveita a oportunidade para recuperar um pouco de mana e tomar sua próxima ação')
        mana += 6
        continue
#Ancestrais Draconicos
    if t == 29 and a != 0 and dragon > 0 and mana > 0:
        vida -= 24
        mana -= 5
        print('{}Uma enorme luz rochoa se forma sob todo o ambiente;\n essa mesma luz brilha nos olhos do dragão, que pronuncia as seguintes palavras:\n Dragão Ancestral: {}, criança tola.... Não consegue enxergar a nossa diferença de poder? Vou faze-lo se arrepender por ter ousado me desafiar\n\n {}O dragão dirige um feixxe de luz mágica que rasga em pedaços a sua resistencia mágica e física.\n você está consideravelmente cansado e ferido'.format(na,n,na))
        continue

    #Rei do terror
    if t == 30 and a != 0 and dragon > 0 and mana > 0:
        vida -= 30
        mana -= mana/3
        print('narrador: Uma tempestade de fogo se forma.\n de dentro da boca da criatura colossal, uma rajada de fogo cria vida e se envolve ao seu redor\n diante de seus olhos, você enxerga todas as pessoas que ja foram mortas, vilas que ja foram queimadas e reinos que ja foram decastados pelo dragão\n com isso, o terror e a dor se tornam cada vez mais marcantes no âmago do seu ser.\n o dragão, em meio a sua dança cruel lhe pronuncia as seguintes palavras:\n dragão: Eu, aquele que a tudo sabe e a todos conhece, digo para você, {}, que a sua alma se rompa\n {}Assim, o fogo atravessa o seu corpo e a sua alma, o que faz com que você tenha grande parte da sua vida e mana drenadas. '.format(na,n,na))
        continue
#comandos do fim
if vida <= 0:
    print('__________________________________________________________________________________\n')
    print(random.choice(['narrador: Mesmo diante de tanto esforço, o dragão, com este último golpe te subjulga\n seus musculos, cansados, ja não mais obedecem ao seu comando.\n Este ficara sendo o dia em que o lord: {} foi derrotado pelo grandioso dragão'.format(n),'narrador: Ao Deferir último golpe, o dragão destroi toda a sua força vital\n por mais que você tente mexer seus músculos, o seu esforço não resulta em nada\n pouco a pouco, sua visão fica turva, e sua consciencia é apagada.']))
    print('\n\t\t\t\t\t\t\t\033[1;31m GAME OVER')
    print("\033[0;32m\ \,_____\033[m\n       \033[0;32m___`\ \033[m \n       \033[0;32m\ \033[m(\033[1;33m*\033[m)\033[0;32m-__\033[m\n         \033[0;32m~      ~~~--__\033[m            \033[1;31m**\033[m              \033[1;31m***\033[m\n               \033[0;32m______  (@\ \033[m   \033[1;31m*******  ****    *******    ******\033[m\n              \033[0;32m/\033[m \033[1;31m******~~~~**************************************\033[m\n      \033[0;32m\       `--____\033[m \033[1;31m********************\033[1;33;40mDRAGON FIGHT\033[0m\033[1;31m**********************\033[m\n     \033[0;32m/ ~~~--_____    ~~~/\033[m  \033[1;31m***************************************\033[m\n                 \033[0;32m`~~~~~\033[m         \033[1;31m******************************\033[m\n                                      \033[1;31m****    **************\033[m\n                                        \033[1;31m***       ***********\033[m\n                                                        \033[1;31m********\033[m")
if dragon <= 0:
    print('__________________________________________________________________________________\n')
    print(random.choice(['narrador: Com este último golpe, o dragão esgota a sua energia e força vital, o que faz com que ele caia, ferido no chão ', 'narrador: mesmo com tudo, o dragão se esgota completamente e cai morto no chão.\n Você, {}, sai vitorioso nesta batalha'.format(n)]))
    print('\n\t\t\t\t\t\t\t\033[32m VOCÊ VENCEU')
    print("\033[0;32m\ \,_____\033[m\n       \033[0;32m___`\ \033[m \n       \033[0;32m\ \033[m(\033[1;33m*\033[m)\033[0;32m-__\033[m\n         \033[0;32m~      ~~~--__\033[m            \033[1;31m**\033[m              \033[1;31m***\033[m\n               \033[0;32m______  (@\ \033[m   \033[1;31m*******  ****    *******    ******\033[m\n              \033[0;32m/\033[m \033[1;31m******~~~~**************************************\033[m\n      \033[0;32m\       `--____\033[m \033[1;31m********************\033[1;33;40mDRAGON FIGHT\033[0m\033[1;31m**********************\033[m\n     \033[0;32m/ ~~~--_____    ~~~/\033[m  \033[1;31m***************************************\033[m\n                 \033[0;32m`~~~~~\033[m         \033[1;31m******************************\033[m\n                                      \033[1;31m****    **************\033[m\n                                        \033[1;31m***       ***********\033[m\n                                                        \033[1;31m********\033[m")