import os
import AudioPlayer

lista_de_audios = []

def adc_audios_lista():
    pasta_audios = os.path.join('Backend','audios')

    AudioPlayer.verificacao_pasta_audios(pasta_audios)
    
    for audio in os.listdir(pasta_audios):
        if audio.endswith('.mp3'):
            lista_de_audios.append(audio)
    
    return lista_de_audios