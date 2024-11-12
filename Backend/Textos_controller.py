import os

class Textos_controller:
    lista_de_textos = []

    @classmethod
    def adc_textos_lista(cls):
        caminho = os.path.join('Backend', 'textos')

        for texto in os.listdir(caminho):
            if texto.endswith('.txt'):
                cls.lista_de_textos.append(texto)
        
        return cls.lista_de_textos
