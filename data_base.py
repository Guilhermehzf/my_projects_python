class Funcionario():
    def __init__(self, cpf, nome, salario = 1212.00):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario

    #gets
    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario

    #sets
    def set_cpf(self, cpf):
        self.cpf = cpf
    def set_nome(self, nome):
        self.nome = nome
    def set_salario(self,salario):
        if salario < 1212.00:
            self.salario = '''esse salario é menor que o minimo, portanto é ilegal.'''
        elif salario <=0:
            self.salario = 'salario invalido.'
        else:
            self.salario = salario

    def __str__(self):
        nome_e_cpf = f'{self.nome}, {self.cpf}'
        return nome_e_cpf

#class gerente
class Gerente(Funcionario):
    def __init__(self, cpf, nome, salario, senha, quant_de_func):
        super().__init__(cpf, nome, salario)
        self.senha = senha
        self.quant_de_func = quant_de_func
    #gets (gerente)
    def get_senha(self):
        return self.senha
    def get_quant_de_func(self):
        return self.quant_de_func

    #sets (gerente)
    def set_senha(self, senha):
        self.senha = senha
    def set_quant_de_func(self, quant_de_func):
        self.quant_de_func = quant_de_func

    #metodos
    def autenticao(self):
        altenticador_nome = input('coloque seu login fdp: ')
        altenticador_senha = int(input('coloque sua senha fdp: '))

        if altenticador_nome == self.nome and altenticador_senha == self.senha:
            print('acesso liberado.')
        else:
            print('seu nome ou senha está errado')

if __name__ == '__main__':

    #Legenda
    print('|' + ('-' * 30) + '|')
    print('|' f'{"Legenda":^30}''|')
    print('|' + ('-' * 30) + '|')
    print(f'|{"CPF":^30}|')
    print(f'|{"Nome_do_funcionario":^30}|')
    print('|'f'{"Salario/Mês":^30}|')
    print('|' + ('-' * 30) + '|')
    print('\n')

    #funcionario 1
    f1 = Funcionario('053.818.751-42', 'Guilherme', 956.45)
    print('|' + ('-' * 30) + '|')
    print('|' f'{"Funcionario 1":^30}''|')
    print('|' + ('-' * 30) + '|')
    print(f'|{f1.get_cpf():^30}|')
    print(f'|{f1.get_nome():^30}|')
    print('|'f'{f1.get_salario():^30}|')
    print('|'f'{f1.__str__():^30}|')
    print('|' + ('-' * 30) + '|')

    #seperador
    print("|"f'{"nova pessoa":^30}'"|")

    #funcionario 2
    f2 = Funcionario('060.297.351-55', 'Lucas', 100.00)
    print('|' + ('-' * 30) + '|')
    print('|' f'{"Funcionario 2":^30}''|')
    print('|' + ('-' * 30) + '|')
    print(f'|{f2.get_cpf():^30}|')
    print(f'|{f2.get_nome():^30}|')
    print('|'f'{f2.get_salario():^30}|')
    print('|'f'{f2.__str__():^30}|')
    print('|' + ('-' * 30) + '|')
    print('\n')

    # Legenda (gerente)
    print('\033[033m|' + ('-' * 30) + '|')
    print('|' f'{"Legenda":^30}''|')
    print('|' + ('-' * 30) + '|')
    print(f'|{"CPF":^30}|')
    print(f'|{"Nome_do_gerente":^30}|')
    print('|'f'{"Salario/Mês":^30}|')
    print('|'f'{"Senha_Gerente":^30}|')
    print('|'f'{"qunatidade de funcinarios":^30}|')
    print('|' + ('-' * 30) + '|\033[m')
    print('\n')

    #gerente 1
    g1 = Gerente('400.289.220-69', 'Raul', 8200.00, 1234, 1400)
    print('\033[033m|' + ('-' * 30) + '|')
    print('|' f'{"Gerente 1":^30}''|')
    print('|' + ('-' * 30) + '|')
    print(f'|{g1.get_cpf():^30}|')
    print(f'|{g1.get_nome():^30}|')
    print('|'f'{g1.get_salario():^30}|')
    print('|'f'{g1.get_senha():^30}|')
    print('|'f'{g1.get_quant_de_func():^30}|')
    print('|' + ('-' * 30) + '|\033[m')
    print('\n')
    print(g1.autenticao())

    #gerente 2
    g2 = Gerente('693.509.290-66', 'Guilherme', 15700.00, 2110, 4200)
    print('\033[033m|' + ('-' * 30) + '|')
    print('|' f'{"Gerente 2":^30}''|')
    print('|' + ('-' * 30) + '|')
    print(f'|{g2.get_cpf():^30}|')
    print(f'|{g2.get_nome():^30}|')
    print('|'f'{g2.get_salario():^30}|')
    print('|'f'{g2.get_senha():^30}|')
    print('|'f'{g2.get_quant_de_func():^30}|')
    print('|' + ('-' * 30) + '|\033[m')
    print('\n')
    print(g2.autenticao())