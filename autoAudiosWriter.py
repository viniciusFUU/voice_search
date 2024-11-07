import speech_recognition as sr
import pyaudio as pa
import json
import os

class primeiro_projeto_pessoal:
    @staticmethod
    def autoAudiosWritter(): 
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data, language='pt-br')
            return f"Você falou: {text}"
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("API unavailable")

    @classmethod
    def criar_bloco_de_notas(cls):
        cls.contador_zero()

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

    @classmethod
    def contador_zero(cls):
        contador_arquivos = 0
        
        with open('contador.json', 'r') as contador:
            contador = json.load(contador)

        for arquivo in os.listdir():
            if arquivo.endswith('.txt'):
                contador_arquivos+=1

        if contador_arquivos == 0:
            contador['contador'] = 0

        with open('contador.json', 'w') as arquivo_contador:
            json.dump(contador, arquivo_contador, ensure_ascii=False, indent=4)
        
        if contador_arquivos > 0:
            print(f"Existe {contador_arquivos} arquivos .txt.")

primeiro_projeto_pessoal.criar_bloco_de_notas()