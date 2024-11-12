import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from Backend import Audios_controller, Textos_controller

root = tk.Tk()

class Application:
    def __init__(self):
        self.tela()
        root.mainloop()

    def tela(self):
        root.title('programa')
        
        largura = 1000
        altura = 650

        posicao_x = (root.winfo_screenwidth() - largura) // 2
        posicao_y = (root.winfo_screenheight() - altura) // 2

        root.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

        self.combo_box_textos()
        self.combo_box_audios()

    def combo_box_textos(self):
        ttk.Label(root, text = "   Textos   ",  
          background = 'red', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
        
        opcoes = Textos_controller.Textos_controller.adc_textos_lista()

        combobox = ttk.Combobox(root, values=opcoes)
        combobox.set("Escolha uma opção")
        combobox.grid(row=1, column=1, padx=10, pady=10)

    def combo_box_audios(self):
        ttk.Label(root, text = "   Audios   ",  
          background = 'red', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 2) 
        
        opcoes = Audios_controller.Audios_controller.adc_audios_lista()

        print(opcoes)

        combobox = ttk.Combobox(root, values=opcoes)
        combobox.set("Escolha uma opção")
        combobox.grid(row=1, column=2, padx=10, pady=10)

Application()