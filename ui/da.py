
i=0
InfoFrames = dados["tituloFrames"]
listaTitulos = []
for item in InfoFrames:
    textoLabel = item["frame"]
    listaTitulos.append(textoLabel)


resposta_radioBtn = tk.IntVar()
resposta_radioBtn2 = tk.IntVar()
def frame1(div):
    frameA = tk.Frame(div)
    opt_sim = tk.Radiobutton(div, text="Sim", variable=resposta_radioBtn, value=1)
    opt_sim.pack()
    opt_nao = tk.Radiobutton(div, text="Não", variable=resposta_radioBtn, value=0)
    opt_nao.pack()
    return frameA
def frame2(div):
    frameB = tk.Frame(div)
    opt_sim = tk.Radiobutton(div, text="Abrir agora", variable=resposta_radioBtn2, value=1)
    opt_sim.pack()
    opt_nao = tk.Radiobutton(div, text="Tempo de espera", variable=resposta_radioBtn2, value=0)
    opt_nao.pack()
    return frameB





 