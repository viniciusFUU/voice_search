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
    def pesquisa_por_voz(cls):
        counter.counter.contador_zero()
        caminho_contador = os.path.join('Backend', 'contador.json')

        with open(caminho_contador, 'r', encoding='utf-8') as contador:
            contador = json.load(contador)
        
        texto = cls.autoAudiosWritter()

        nome_arquivo = texto
        print(f"nome do arquivo: {nome_arquivo}")

        caminho_completo = os.path.join('Backend', 'textos', f"{nome_arquivo}.txt")

        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
        
        print("Documento criado com sucesso.")

        with open(caminho_contador, 'w', encoding='utf-8') as arquivo_contador:
            contador['contador']+=1
            json.dump(contador, arquivo_contador, ensure_ascii=False, indent=4)
            print('td certo')

        wiki_pesquisa = Searching.Searching.wikipedia_search(f"{nome_arquivo}.txt")
        wiki_pesquisa = " ".join(wiki_pesquisa)
        audio_player.AudioPlayer.gerar_e_reproduzir_audio(nome_arquivo, wiki_pesquisa)

    @classmethod
    def pesquisa_por_texto(cls, texto):
        counter.counter.contador_zero()
        caminho_contador = os.path.join('Backend', 'contador.json')

        with open(caminho_contador, 'r', encoding='utf-8') as contador:
            contador = json.load(contador)
        
        nome_arquivo = texto
        print(f"nome do arquivo: {nome_arquivo}")

        caminho_completo = os.path.join('Backend', 'textos', f"{nome_arquivo}.txt")

        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
        
        print("Documento criado com sucesso.")

        with open(caminho_contador, 'w', encoding='utf-8') as arquivo_contador:
            contador['contador']+=1
            json.dump(contador, arquivo_contador, ensure_ascii=False, indent=4)
            print('td certo')

        wiki_pesquisa = Searching.Searching.wikipedia_search(f"{nome_arquivo}.txt")
        wiki_pesquisa = " ".join(wiki_pesquisa)
        audio_player.AudioPlayer.gerar_e_reproduzir_audio(nome_arquivo, wiki_pesquisa)