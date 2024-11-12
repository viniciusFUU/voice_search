import speech_recognition as sr
import json
import Counter as counter
import Searching
import AudioPlayer as audio_player
import os

class AutoAudiosWriter:
    @staticmethod
    def autoAudiosWritter(): 
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Escutando audio")
            audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data, language='pt-br')
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("API unavailable")

    @classmethod
    def criar_bloco_de_notas(cls):
        counter.counter.contador_zero()
        caminho_contador = os.path.join('Backend', 'contador.json')

        with open(caminho_contador, 'r') as contador:
            contador = json.load(contador)
        
        nome_arquivo = f"arquivo{contador['contador']}"
        print(nome_arquivo)
        # texto = cls.autoAudiosWritter()
        texto = "egito"

        caminho_completo = os.path.join('Backend', 'textos', f"{nome_arquivo}.txt")

        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
        
        print("Documento criado com sucesso.")

        with open(caminho_contador, 'w') as arquivo_contador:
            print(contador)
            contador['contador']+=1
            print(contador)
            json.dump(contador, arquivo_contador, ensure_ascii=False, indent=4)

        wiki_pesquisa = Searching.Searching.wikipedia_search(f"{nome_arquivo}.txt")
        wiki_pesquisa = " ".join(wiki_pesquisa)
        audio_player.AudioPlayer.reproduzir_audio(nome_arquivo, wiki_pesquisa)

AutoAudiosWriter.criar_bloco_de_notas()