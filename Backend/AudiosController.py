import os
import FolderVerification


def adc_audios_lista():
    lista_de_audios = []
    pasta_audios = os.path.join('Backend','audios')

    FolderVerification.varificacao_pastas(pasta_audios)
    
    for audio in os.listdir(pasta_audios):
        if audio.endswith('.mp3'):
            lista_de_audios.append(audio)
    
    return lista_de_audios