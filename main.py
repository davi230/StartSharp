import tkinter as tk
from ui.base_frame import Base_frame
from ui.frames import listFrames
from config.trata_dados import listaTitulos
from controllers.frame_manager import index

janela = tk.Tk()
janela.title("Auxiliar de Produtividade") 
  
# cria a janela principal
app = Base_frame(janela)

# define o texto do título
app.set_titulo(listaTitulos[index])

# define o frame a ser exibido
frame = listFrames[index](app.bloco2)
app.set_frame(frame)


janela.mainloop()