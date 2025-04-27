import tkinter as tk
# import json
# with open('programas.json', 'r', encoding='utf-8') as file:
#     dados = json.load(file)

class Base_frame:
    def __init__(self, janela):
        # Cria os frames principais da janela
        self.bloco1 = tk.Frame(janela)
        self.bloco1.pack()
        self.bloco2 = tk.Frame(janela)
        self.bloco2.pack()
        self.bloco3 = tk.Frame(janela)
        self.bloco3.pack()
        
    def label_frame(self, text):
        # Cria um label dentro do bloco1 e o adiciona ao frame
        titulo = tk.Label(self.bloco1, text=text)
        titulo.pack()
        return titulo
    
    def frame_block(self, frame_name):
        # Exibe o frame atual no bloco 2
        # O frame_name é o frame que você quer exibir
        self.frame = frame_name(self.bloco2)
        # Aqui você pode adicionar o frame_name ao bloco2
        
        
    
    def close_frame(self, janela):
        # Fecha a janela
        self.janela = janela.destroy()
        
    def next_frame(self):
        # Troca para o próximo frame
        self.bloco2.pack_forget()
        # Aqui você pode adicionar a lógica para o próximo frame
        # Exemplo: self.bloco4.pack() ou chamar outra função para criar o próximo frame
    
    def button(self, janela):
        # Cria um botão dentro do bloco3 e o adiciona ao frame
        btn_proximo = tk.Button(self.bloco3, text="Próximo", command=lambda: self.next_frame)
        btn_proximo.pack()
        btn_cancelar = tk.Button(self.bloco3, text="Cancelar", command=lambda: self.close_frame(janela))
        btn_cancelar.pack()
        return btn_proximo, btn_cancelar
    
    