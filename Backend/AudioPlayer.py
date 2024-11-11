import gtts 
from playsound import playsound
import os

class AudioPlayer:
    @staticmethod
    def reproduzir_audio(nome_arquivo, texto):
        conteudo = gtts.gTTS(texto, lang='pt-br', slow=False)

        conteudo.save(os.path.join('Backend', 'audios',f'{nome_arquivo}.mp3'))
        playsound(os.path.join('Backend', 'audios', f'{nome_arquivo}.mp3'))