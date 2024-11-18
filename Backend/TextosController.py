import os
import FolderVerification

lista_de_textos = []

def adc_textos_lista():
    caminho = os.path.join('Backend', 'textos')

    FolderVerification.varificacao_pastas(caminho)

    for texto in os.listdir(caminho):
        if texto.endswith('.txt'):
            lista_de_textos.append(texto)
    
    return lista_de_textos