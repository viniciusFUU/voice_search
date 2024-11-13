import os
import AudioPlayer

class AudiosController:
    lista_de_audios = []

    @classmethod
    def adc_audios_lista(cls):
        pasta_audios = os.path.join('Backend','audios')

        AudioPlayer.AudioPlayer.verificacao_pasta_audios(pasta_audios)
        
        for audio in os.listdir(pasta_audios):
            if audio.endswith('.mp3'):
                cls.lista_de_audios.append(audio)
        
        return cls.lista_de_audios