import os

def varificacao_pastas(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)