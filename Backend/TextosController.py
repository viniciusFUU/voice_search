import os

class TextosController:
    lista_de_textos = []

    @classmethod
    def adc_textos_lista(cls):
        caminho = os.path.join('Backend', 'textos')

        cls.verificacao_existencia_pasta(caminho)

        for texto in os.listdir(caminho):
            if texto.endswith('.txt'):
                cls.lista_de_textos.append(texto)
        
        return cls.lista_de_textos
    
    @classmethod
    def verificacao_existencia_pasta(cls, caminho):
        if not os.path.exists(caminho):
            print("Criando pasta Textos")
            os.mkdir(caminho) 