import os

lista_de_textos = []

def adc_textos_lista():
    caminho = os.path.join('Backend', 'textos')

    verificacao_existencia_pasta(caminho)

    for texto in os.listdir(caminho):
        if texto.endswith('.txt'):
            lista_de_textos.append(texto)
    
    return lista_de_textos

def verificacao_existencia_pasta(caminho):
    if not os.path.exists(caminho):
        print("Criando pasta Textos")
        os.mkdir(caminho) 