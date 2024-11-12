import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk, messagebox, Message
from Backend import Audios_controller, Textos_controller, Pesquisas_controller, AudioPlayer

root = tk.Tk()

class Application:
    def __init__(self):
        self.tela()
        root.mainloop()

    def tela(self):
        root.title('programa')
        root.config(background='#260d33')

        largura = 1000
        altura = 650

        posicao_x = (root.winfo_screenwidth() - largura) // 2
        posicao_y = (root.winfo_screenheight() - altura) // 2

        root.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

        self.combo_box_textos()
        self.combo_box_audios()

    def combo_box_textos(self):
        
        ttk.Label(
                root, 
                text = "Pesquisas",
                anchor= 'center',  
                background = '#157a8c', 
                foreground ="white",  
                font = ("Times New Roman", 15)
                ).grid(row = 1, column = 1, pady=(10, 0), ipadx=31) 
        
        opcoes = Pesquisas_controller.Pesquisas_controller.listar_arquivos()

        combobox = ttk.Combobox(root, values=opcoes)
        combobox.set("Escolha uma opção")
        combobox.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(root, text="Abrir texto").grid(row=3, column=1, pady=(0,5), ipadx=38)

        def abrir_texto():
            valor_escolhido = combobox.get()  
            if valor_escolhido != "Escolha uma opção":
                messagebox.showinfo('Conteudo encontrado',Pesquisas_controller.Pesquisas_controller.busca_pesquisa(valor_escolhido))
            else:
                messagebox.showinfo('Erro: ', "Nenhum elemento selecionado")            

        tk.Button(root, text="Abrir texto", command=abrir_texto).grid(row=3, column=1, pady=(0,5), ipadx=38)

    def combo_box_audios(self):
        ttk.Label(
                root, 
                text = "Audios",
                anchor= 'center',  
                background = '#157a8c', 
                foreground ="white",  
                font = ("Times New Roman", 15)
                ).grid(row = 4, column = 1, pady=(5, 0), ipadx=41) 
        
        opcoes = Audios_controller.Audios_controller.adc_audios_lista()

        combobox = ttk.Combobox(root, values=opcoes)
        combobox.set("Escolha uma opção")
        combobox.grid(row=5, column=1, padx=10, pady=5)

        def abrir_audio():
            valor_escolhido = combobox.get()
            if valor_escolhido != "Escolha uma opção":
                print(valor_escolhido)
                AudioPlayer.AudioPlayer.reproduzir_audio(valor_escolhido)
            else:
                messagebox.showinfo("Erro: ", "Nenhum elemento selecionado")

        tk.Button(root, text="Escutar audio", command=abrir_audio).grid(row=6, column=1, pady=(0,5), ipadx=31)

Application()