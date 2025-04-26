# Imports ------------------
from tkinter import *
import time
import subprocess

# Abre escopo da janela -----------------
janela = Tk()

# Titulo da janela ---------------------
janela.title("Auxiliar de Produtiviade")

# Variáveis -------------------
solidworks_ = IntVar()
blender_ = IntVar()
chrome_ = IntVar()
photoshop_ = IntVar()
illustrator_ = IntVar()
vscode_ = IntVar()
opcao = BooleanVar()
tempo_total = 0
frame1 = Frame(janela)
frame2 = Frame(janela)
frame3 = Frame(janela)
frame4 = Frame(janela)
contador = 0
resposta_radioBtn = StringVar(value="")
progs_para_abrir = []
progs = [
    {'programa':'solidworks', 'caminho':r'C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\SLDWORKS.exe', 'abrir':solidworks_},
    {'programa':'photoshop', 'caminho':r'C:\Program Files\Adobe\Adobe Photoshop 2025\Photosho.exe', 'abrir':photoshop_},
    {'programa':'illustrator', 'caminho':r'C:\Program Files\Adobe\Adobe Illustrator 2025\Support Files\Contents\Windows\Illustrator.exe', 'abrir':illustrator_},
    {'programa':'blender', 'caminho':r'C:\Program Files\Blender Foundation\Blender 3.3\blender.exe', 'abrir':blender_},
    {'programa':'chrome', 'caminho':r'C:\Program Files\Google\Chrome\Application\chrome.exe', 'abrir':chrome_},
    {'programa':'vscode', 'caminho':r'C:\Users\mamut\AppData\Local\Programs\Microsoft VS Code\Code.exe', 'abrir':vscode_}
]

# Funções ----------------------
def troca_frame():
    global contador
    if (contador == 0) :
        contador += 1
        frame1.pack_forget()
        frame2.pack()
    elif (contador == 1) :
        contador += 1
        frame2.pack_forget()
        frame3.pack()
    elif (contador == 2) :
        contador += 1
        frame3.pack_forget()
        frame4.pack()
    else : 
        print("Fim!")
        janela.destroy()

def fecha_janela() :
    janela.destroy()
    
def verifica_resposta ():
    if (resposta_radioBtn.get() == "sim"):
        troca_frame()
    else:
        janela.destroy() 
        
def desabilita_tempo() :
    if opcao.get() == 1:
        Btn_add_tempo1.config(state=DISABLED)
        Btn_add_tempo5.config(state=DISABLED)
        Btn_add_tempo10.config(state=DISABLED)
        Btn_add_tempo30.config(state=DISABLED)
    else:
        Btn_add_tempo1.config(state=NORMAL)
        Btn_add_tempo5.config(state=NORMAL)
        Btn_add_tempo10.config(state=NORMAL)
        Btn_add_tempo30.config(state=NORMAL)

def somar_tempo(num):
    global tempo_total
    tempo_total = num + tempo_total
    return tempo_total
    
def executa():  
    if opcao.get() == 0:  
        time.sleep(tempo_total*60)
        for caminho in progs_para_abrir:
            print(caminho)
            subprocess.Popen(caminho)
    elif opcao.get() == 1: 
       for caminho in progs_para_abrir:
            print(caminho)
            subprocess.Popen(caminho)
    troca_frame()

#Parâmetros verifica_selecao. progs_para_abrir, progs . Lembrar de colocar também no botão
def verifica_selecao ():
    for prog in progs:
        if (prog['abrir'].get() == 1):
            progs_para_abrir.append(prog['caminho'])
        else: 
            print(progs_para_abrir)
    troca_frame()
    
    
#Frame 1 - Vai trabalhar Hoje?
Label(frame1, text="Você vai trabalhar hoje?").pack()
Radiobutton(frame1, text="Sim",variable=resposta_radioBtn, value="sim").pack()
Radiobutton(frame1, text="Não",variable=resposta_radioBtn, value="nao").pack()
Button(frame1, text="Próximo", command=verifica_resposta).pack()
Button(frame1, text="Cancelar", command=fecha_janela).pack()

#Frame 2 - Quais programas abrir?
Label(frame2, text="Quais programas abrir?").pack()
Checkbutton(frame2, text="Solidworks",variable=solidworks_, onvalue=1, offvalue=0).pack()
Checkbutton(frame2, text="Blender",variable=blender_, onvalue=1, offvalue=0).pack()
Checkbutton(frame2, text="Photoshop",variable=photoshop_, onvalue=1, offvalue=0).pack()
Checkbutton(frame2, text="Illustrator",variable=illustrator_, onvalue=1, offvalue=0).pack()
Checkbutton(frame2, text="Chrome",variable=chrome_, onvalue=1, offvalue=0).pack()
Checkbutton(frame2, text="VSCode",variable=vscode_, onvalue=1, offvalue=0).pack()
Button(frame2, text="Próximo", command=verifica_selecao).pack()
Button(frame2, text="Cancelar", command=fecha_janela).pack()

#Frame 3 - Quando abrir?
Label(frame3, text="Quando abrir?").pack()
abrir_agora_sim = Radiobutton(frame3, text="Abrir agora",variable=opcao, value=1, command=desabilita_tempo).pack()
abrir_agora_nao = Radiobutton(frame3, text="Tempo",variable=opcao, value=0, command=desabilita_tempo).pack()
Btn_add_tempo1 = Button(frame3, text="+1 min", command=lambda : somar_tempo(1), state=DISABLED)
Btn_add_tempo1.pack()
Btn_add_tempo5 = Button(frame3, text="+5 min", command=lambda : somar_tempo(5), state=DISABLED)
Btn_add_tempo5.pack()
Btn_add_tempo10 = Button(frame3, text="+10 min", command=lambda : somar_tempo(10), state=DISABLED)
Btn_add_tempo10.pack()
Btn_add_tempo30 = Button(frame3, text="+30 min", command=lambda : somar_tempo(30), state=DISABLED)
Btn_add_tempo30.pack()
Button(frame3, text="Próximo", command=executa).pack()
Button(frame3, text="Cancelar", command=fecha_janela).pack()

#Frame 4 - Espera
Label(frame4, text="Aguarde Mestre!").pack()
Button(frame4, text="Cancelar", command=fecha_janela).pack()

frame1.pack()

janela.mainloop()