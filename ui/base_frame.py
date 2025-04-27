import tkinter as tk
class Base_frame:
    def __init__(self, janela):
        self.bloco1 = tk.Frame(janela)
        self.bloco1.pack()
        self.bloco2 = tk.Frame(janela, width=200, height=200, bg="blue")
        self.bloco2.pack()
        self.bloco3 = tk.Frame(janela, width=200, height=200, bg="green")
        self.bloco3.pack()
        
    def set_titulo(self, text):
        # Só coloca o título
        titulo = tk.Label(self.bloco1, text=text)
        titulo.pack()
        #tk.Label(self.bloco1, text="Bloco 1").pack()
        #tk.Label(self.bloco2, text="Bloco 2").pack()
        #tk.Label(self.bloco3, text="Bloco 3").pack()