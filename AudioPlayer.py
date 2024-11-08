import gtts 
from playsound import playsound

class AudioPlayer:
    @staticmethod
    def reproduzir_audio(nome_arquivo, texto):
        conteudo = gtts.gTTS(texto, lang='pt-br', slow=False)

        conteudo.save(f'{nome_arquivo}.mp3')
        playsound(f'{nome_arquivo}.mp3')