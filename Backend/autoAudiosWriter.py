import speech_recognition as sr
import json
import FolderVerification
import Searching
import AudioPlayer as audio_player
import os

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

def pesquisa_por_voz():    
    texto = autoAudiosWritter()

    nome_arquivo = texto
    print(f"nome do arquivo: {nome_arquivo}")

    caminho_completo = os.path.join('Backend', 'textos', f"{nome_arquivo}.txt")

    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)
    
    print("Documento criado com sucesso.")

    wiki_pesquisa = Searching.wikipedia_search(f"{nome_arquivo}.txt")
    wiki_pesquisa = " ".join(wiki_pesquisa)
    audio_player.gerar_e_reproduzir_audio(nome_arquivo, wiki_pesquisa)

def pesquisa_por_texto(texto):    
    nome_arquivo = texto

    caminho_pasta = os.path.join('Backend', 'Textos')
    FolderVerification.varificacao_pastas(caminho_pasta)

    caminho_completo = os.path.join('Backend', 'textos', f"{nome_arquivo}.txt")

    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)
    
    print("Documento criado com sucesso.")

    wiki_pesquisa = Searching.wikipedia_search(f"{nome_arquivo}.txt")
    wiki_pesquisa = " ".join(wiki_pesquisa)
    audio_player.gerar_e_reproduzir_audio(nome_arquivo, wiki_pesquisa)