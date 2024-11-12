import os

class Audios_controller:
    lista_de_audios = []

    @classmethod
    def adc_audios_lista(cls):
        pasta_audios = os.path.join('Backend','audios')
        
        for audio in os.listdir(pasta_audios):
            if audio.endswith('.mp3'):
                cls.lista_de_audios.append(audio)
        
        return cls.lista_de_audios