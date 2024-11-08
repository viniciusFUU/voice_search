import json
import os

class counter:
    @classmethod
    def contador_zero(cls):
        contador_arquivos = 0
        lista_de_textos = os.path.join('textos')
        
        with open('contador.json', 'r') as contador:
            contador = json.load(contador)

        for arquivo in os.listdir(lista_de_textos):
            if arquivo.endswith('.txt'):
                contador_arquivos+=1

        if contador_arquivos == 0:
            contador['contador'] = 0

        with open('contador.json', 'w') as arquivo_contador:
            json.dump(contador, arquivo_contador, ensure_ascii=False, indent=4)
        
        if contador_arquivos > 0:
            print(f"Existe {contador_arquivos} arquivos .txt.")
