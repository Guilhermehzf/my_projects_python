Maior_altura = 0
Menor_altura = 3
numero_de_homens = 0
numero_de_mulheres = 0
numero_de_outros = 0
altura_total = 0
print('pressione enter para sair.')
while True:
    genero = input('coloque seu genero(H/M/O): ').lower()
    if genero == '':
        break

    if genero != 'h' and genero != 'm' and genero != 'o':
        print('genoro invalido.')
        continue
    altura = float(input('coloque sua altura: '))
    if 3 < altura < 0:
        print('altura invalida .')
        continue
    if 3 > altura > 0:
        altura_total += altura
    if genero == 'h':
        numero_de_homens += 1
    elif genero == 'm':
        numero_de_mulheres += 1
    elif genero == 'o':
        numero_de_outros += 1
    if altura > Maior_altura:
        Maior_altura = altura
    if altura < Menor_altura:
        Menor_altura = altura
    else:
        print('valor invalido')


total_pessoas = numero_de_mulheres + numero_de_homens + numero_de_outros
media_altura = altura_total/total_pessoas
print(f'''o taltal de pessoas é {total_pessoas} onde
você tem {numero_de_homens} homem(s) 
{numero_de_mulheres} mulher(es)
{Maior_altura} é a maior altura
{Menor_altura} é a menor altura
e a media de altura do grupo é {media_altura}''')