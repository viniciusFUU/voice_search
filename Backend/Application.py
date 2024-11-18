import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk, messagebox
import PesquisasController, AudiosController, AudioPlayer, AutoAudiosWriter

root = tk.Tk()

class Application:
    def __init__(self):
        self.tela()
        root.mainloop()

    def tela(self):
        root.title('1st version')
        root.config(background='#003f69')

        largura = 400
        altura = 400

        posicao_x = (root.winfo_screenwidth() - largura) // 2
        posicao_y = (root.winfo_screenheight() - altura) // 2

        root.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

        self.combo_box_textos()
        self.combo_box_audios()
        self.funcao_principal_do_projeto_por_audio()
        self.funcao_principal_do_projeto_por_texto()

    def combo_box_textos(self):
        
        ttk.Label(
                root, 
                text = "Pesquisas",
                anchor= 'center',  
                background = '#157a8c', 
                foreground ="white",  
                font = ("Times New Roman", 15)
                ).grid(row = 1, column = 1, padx=(130,0), pady=(10, 0), ipadx=31) 
        
        opcoes = PesquisasController.listar_arquivos()

        combobox = ttk.Combobox(root, values=opcoes)
        combobox.set("Escolha uma opção")
        combobox.grid(row=2, column=1, padx=(130,0), pady=5)

        def abrir_texto():
            valor_escolhido = combobox.get()  
            if valor_escolhido != "Escolha uma opção":
                messagebox.showinfo('Conteudo encontrado',PesquisasController.busca_pesquisa(valor_escolhido))
            else:
                messagebox.showinfo('Erro: ', "Nenhum elemento selecionado")            

        tk.Button(root, text="Abrir texto", command=abrir_texto).grid(row=3, column=1, padx=(130,0), pady=(0,5), ipadx=38)

    def combo_box_audios(self):
        ttk.Label(
                root, 
                text = "Audios",
                anchor= 'center',  
                background = '#157a8c', 
                foreground ="white",  
                font = ("Times New Roman", 15)
                ).grid(row = 4, column = 1, padx=(130,0), pady=(5, 0), ipadx=41) 
        
        opcoes = AudiosController.adc_audios_lista()

        combobox = ttk.Combobox(root, values=opcoes)
        combobox.set("Escolha uma opção")
        combobox.grid(row=5, column=1, padx=(130,0), pady=5)

        def abrir_audio():
            valor_escolhido = combobox.get()
            if valor_escolhido != "Escolha uma opção":
                print(valor_escolhido)
                AudioPlayer.reproduzir_audio(valor_escolhido)
            else:
                messagebox.showinfo("Erro: ", "Nenhum elemento selecionado")

        tk.Button(root, text="Clique e escute o audio", command=abrir_audio).grid(row=6, column=1, padx=(130,0), pady=(0,5), ipadx=5)

    def funcao_principal_do_projeto_por_audio(self):
        ttk.Label(
                root,
                text="Busca por Audio",
                anchor='center',
                background='#157a8c',
                foreground='white',
                font=("Times New Roman", 15)
            ).grid(row=7, column=1, padx=(130,0), pady=(10, 0), ipadx=4)

        tk.Button(root, text="Clique e fale", command=AutoAudiosWriter.pesquisa_por_voz).grid(row=8, column=1, padx=(130,0), pady=(5,5), ipadx=35)

    def funcao_principal_do_projeto_por_texto(self):
        ttk.Label(
                root,
                text="Busca por Texto",
                anchor='center',
                background='#157a8c',
                foreground='white',
                font=("Times New Roman", 15)
            ).grid(row=9, column=1, padx=(130,0), pady=(10, 0), ipadx=6)
        
        entrada = tk.Entry()
        entrada.grid(row=10, column=1, padx=(130,0), ipadx=10, pady=(2,0))

        def busca_por_entrada():
            texto = entrada.get()
            AutoAudiosWriter.pesquisa_por_texto(texto)

        tk.Button(root, text="Clique e busque", command=busca_por_entrada).grid(row=11, column=1, padx=(130,0), pady=(5,5), ipadx=24)

Application()