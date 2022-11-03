lista = []
def menu():
   while True:
       print('[c] - create')
       print('[r] - Read')
       print('[u] - Update')
       print('[d] - Delete')
       print('[e] - Exit')
       opcao = input('opção: ').lower()
       if opcao != 'c' and opcao != 'r' and opcao != 'u' and opcao != 'd' and opcao != 'e':
           print('opção invalida, tente novamente')
       return opcao
def create():
   nome = input('nome: ')
   lista.append(nome)
def read():
   if len(lista) == 0:
       print('lista vazia.')
   else:
       for c in range(len(lista)):
           print(lista[c])
def Update():
   p = int(input('posição'))
   nome = input('nome: ')
   lista[p] = nome
def Delete():
   if lista != []:
       read()
       try:
           p = int(input('Qual a posição'))
           novo_nome = input('Novo nome:')
           lista[p] = novo_nome
       except IndexError as e:
           print('posição errada')
       except ValueError as e:
           print('erro geral.')
   else:
       print('lista vazia')
   nome = input('nome: ')
   lista.remove(nome)

if __name__ == '__main__':
   while True:
       op = menu()
       if op == 'c':
           create()
       elif op == 'r':
           read()
       elif op == 'u':
           Update()
       elif op == 'd':
           Delete()
       elif op == 'e':
           exit()