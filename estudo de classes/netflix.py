# vamos criar uma classe para Clientes da Netflix

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.listaPlanos = ['basic', 'premium']
    
        if plano in self.listaPlanos:
            self.plano = plano
        else:
            print('Plano inválido')

    def mudarPlano(self, novoPlano):
        if novoPlano in self.listaPlanos:
            self.plano = novoPlano
        else:
            print('Plano inválido')
    

    def verFilme(self, filme, planoFilme):
        if self.plano == planoFilme:
            print(f'Ver Filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver Filme {filme}')
        elif self.plano == 'basic' and planoFilme == 'premium':
            print('Faça upgrade para premium para ver esse filme')
        else:
            print('Plano Inválido')            





cliente = Cliente("Lira", "lira@gmail.com", "basic")

print(cliente.plano)
cliente.verFilme('HP1', 'premium')

#--------------------#

cliente.mudarPlano('premium') 
print(cliente.plano)
cliente.verFilme('HP1', 'premium') 

