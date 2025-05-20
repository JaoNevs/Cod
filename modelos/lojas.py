from modelos.avaliacao import Avaliacao
from modelos.item_vest.item_vestuario import ItemLoja

class Loja:

    lojas = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._itemvestuario = []
        Loja.lojas.append(self)

    def __str__(self):
        return f' {self._nome} | {self.categoria}'
    
    @classmethod
    def listar_lojas(cls): 
        print(f'{'Nome da Loja'.ljust(25)} | {'Categoria da Loja'.ljust(25)} | {'Média de Avaliação'.ljust(25)} | {'Status da Loja'}') 
        for loja in cls.restaurantes:
            print(f'{loja._nome.ljust(25)} | {loja.categoria.ljust(25)} | {str(loja.media_avaliacoes).ljust(25)} | {loja.ativo}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'

    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)


    @property
    def media_avaliacoes (self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    # def add_calca_vest(self,calca):
    #     self._itemvestuario.append(calca)

    # def add_camisa_vest(self,camisa):
    #     self._itemvestuario.append(camisa)


    def add_vestuario(self, item):
        if isinstance(item,ItemLoja):
            self._itemvestuario.append(item)

    @property
    def exibir_vest(self):
        print(f'Vestuário da Loja: {self._nome}\n')
        for i,item in enumerate(self._itemvestuario, start=1):
            if hasattr(item,'_descricao'):
                mensagem_camisa = f'{i}- Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_camisa)
            else: 
                mensagem_calca = f'{i}- Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_calca)