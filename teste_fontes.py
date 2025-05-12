import tkinter as tk
import estilos

lista_de_fontes = ["Arial", "Times New Roman", "Courier New", "Verdana", "Tahoma", "Segoe UI", "Trebuchet MS", "Lucida Console", "Georgia", "Comic Sans MS"]
fontes_inspiradoras = ["Century Gothic", "Impact", "Palatino Linotype", "Book Antiqua", "Franklin Gothic Medium", "Baskerville Old Face", "Garamond", "Brush Script MT", "Copperplate Gothic Light", "Stencil"]

#474448, #2d232e, #e0ddcf, #ec4e20, #2081c3


janela = tk.Tk()
blocoEsquerda = tk.Frame(janela, bg="gray")
blocoEsquerda.pack(side="left")
blocoDireita = tk.Frame(janela)
blocoDireita.pack(side="right")

for font1, font2 in zip(lista_de_fontes, fontes_inspiradoras):
    t = tk.Button(blocoEsquerda, text=f"Este é um exemplo da fonte {font1}")
    estilos.Aplica_estilos.t1(t, font1)
    t.pack()
    t2 = tk.Button(blocoDireita, text=f"Este é um exemplo da fonte {font2}")
    estilos.Aplica_estilos.t2(t2, font2)
    t2.pack()

janela.mainloop()