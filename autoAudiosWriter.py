import speech_recognition as sr
import pyaudio as pa
import json
import os
import Counter as counter
import Searching

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

        with open('contador.json', 'r') as contador:
            contador = json.load(contador)
        
        nome_arquivo = f"arquivo{contador['contador']}.txt"
        texto = cls.autoAudiosWritter()

        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
        
        print("Documento criado com sucesso.")

        contador['contador']+=1

        with open('contador.json', 'w') as arquivo_contador:
            json.dump(contador, arquivo_contador, ensure_ascii=False, indent=4)

        print(Searching.Searching.wikipedia_search(nome_arquivo))

AutoAudiosWriter.criar_bloco_de_notas()