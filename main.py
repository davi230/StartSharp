import tkinter as tk
from ui.base_frame import Base_frame
from config.trata_dados import listaTitulos

janela = tk.Tk()
janela.title("Auxiliar de Produtividade")   
app = Base_frame(janela)
app.set_titulo(listaTitulos[0])
janela.mainloop()