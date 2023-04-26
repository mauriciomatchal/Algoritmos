class ControleRemoto:  # -> É um objeto

    #Feita para atribuir características e atributos a um objeto

    def __init__(self, cor, altura, profundidade, largura) -> None:
        self.cor = cor #self cria a caracteristica
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

        # essas são as características, elas vão dentro do init

    def passarCanal(self, botao):

        if botao == '+':
            print('Aumentar o Canal')
        elif botao == '-':
            print('Diminuir o Canal')
        else:
            print('Esse botão não está disponível para essa função')


    # métodos do controle remoto:
    #   - passar de canal
    #   - mexer no volume
    #   - abrir a netflix
    #   - desligar a tv
    

controleRemoto = ControleRemoto('preto', '10cm', '2cm', '2cm') #possui todas as caracteristicas

controleRemoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm') #possui todas as caracteristicas padrão da classe mas é diferente

print(controleRemoto2.cor) #-> imprime cinza

print(controleRemoto.altura) #-> imprime 10cm

controleRemoto.passarCanal('+')

