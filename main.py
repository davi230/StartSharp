import tkinter as tk
from ui.base_frame import Base_frame
from ui.frames import listFrames
from config.trata_dados import listaTitulos

janela = tk.Tk()
janela.title("Auxiliar de Produtividade") 
  
# cria a janela principal
app = Base_frame(janela)

# define o texto do título
app.set_titulo(listaTitulos[0])

# define o frame a ser exibido
frame = listFrames[0](app.bloco2)
app.set_frame(frame)


janela.mainloop()