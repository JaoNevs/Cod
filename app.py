from modelos.lojas import Loja
from modelos.item_vest.camisa import Camisas
from modelos.item_vest.calcas import Calcas

loja_um = Loja('Um', 'Roupas')
calca_masc = Calcas ('Cargo', 200.00, 44)
calca_masc.aplicar_desconto()
camisa_masc = Camisas ('Oversized', 150.00, 'Mais larga que o comum')
camisa_masc.aplicar_desconto()
loja_um.add_vestuario(calca_masc)
loja_um.add_vestuario(camisa_masc)

# loja_um.receber_avaliacao('Gui',10)
# loja_um.receber_avaliacao('Julia', 8)
# loja_um.receber_avaliacao('Emy', 6)





def main():
    loja_um.exibir_vest
    
if __name__ == '__main__':
    main()