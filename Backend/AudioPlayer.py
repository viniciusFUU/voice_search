import gtts 
from playsound import playsound
import os

class AudioPlayer:
    @staticmethod
    def gerar_e_reproduzir_audio(nome_arquivo, texto):
        conteudo = gtts.gTTS(texto, lang='pt-br', slow=False)

        conteudo.save(os.path.join('Backend', 'audios',f'{nome_arquivo}.mp3'))
        playsound(os.path.join('Backend', 'audios', f'{nome_arquivo}.mp3'))

    @staticmethod
    def reproduzir_audio(nome_arquivo):
        playsound(os.path.join('Backend', 'audios', nome_arquivo))

    def verificacao_pasta_audios(caminho):
        if not os.path.exists(caminho):
            os.mkdir(caminho)