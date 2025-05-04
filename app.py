import tkinter as tk
import json
import subprocess
import time
import os

# Classe que cria a janela
class App:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Start Sharp")
        #self.janela.geometry("800x600")
        self.base_frame = Base_frame(self.janela)
       
    def run(self):
        self.janela.mainloop() 

# Classe que importa e trata dados json
class Dados:
    DB_PROGRAMAS = 'db.json'
    
    def __init__(self):
        with open(self.DB_PROGRAMAS, 'r', encoding='utf-8') as arquivo:
            self.dados = json.load(arquivo)
        self.lstProgs = self.dados["programas"]
        self.vars = {}

        
    def atualiza_dados(self):
        with open(self.DB_PROGRAMAS, 'r+', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for programa in dados['programas']:
                if programa["nome"] in self.vars:
                    programa['abrir'] = self.vars[programa["nome"]].get()
            arquivo.seek(0)
            json.dump(dados, arquivo, indent=4)
            arquivo.truncate()
    

        
# Classe que divide a janela em três blocos
class Base_frame:
    def __init__(self, janelaPrincipal):
        self.janela = janelaPrincipal
        self.blocoLabel = tk.Frame(self.janela)
        self.blocoLabel.pack()
        self.blocoFrames = tk.Frame(self.janela)
        self.blocoFrames.pack()
        self.blocoBotoes = tk.Frame(self.janela)
        self.blocoBotoes.pack()
        self.frames = Frames(self.janela, self.blocoLabel, self.blocoFrames, self.blocoBotoes)
        self.frames.frame_trabalho()

# Classe que cria o label
class Label_default:
    def __init__(self, Label_block):
        self.blocoLabel = Label_block
        self.label = tk.Label(self.blocoLabel)
        self.label.pack()
        
    def atualizar_label(self, texto):
        self.label.config(text=texto)
   
# Classe que cria btn "Próximo" e "Cancelar"
class Main_buttons():
    def __init__(self, janelaPrincipal, buttons_block):
        self.janela = janelaPrincipal
        self.blocoBotoes = buttons_block
        self.btn_proximo = tk.Button(self.blocoBotoes, text="Próximo")
        self.btn_proximo.pack()
        self.btn_cancelar = tk.Button(self.blocoBotoes, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.pack()
    
    def acao_btn_prox(self, acao):
        self.btn_proximo.config(command=acao)
    
    def cancelar(self):
        self.janela.destroy()

# Classe que abre programas
class Open_progs:
    def __init__(self, frames):
        self.tempo_total = 0
        self.programas = Dados().lstProgs
        self.opt = frames.frm4_opt
        self.tempos = frames.tempo_total
    
    def abre_progs(self):
        if self.opt == 1:
            for prog in self.programas:
                if prog['abrir'] == 1:
                    subprocess.Popen(prog['caminho'])
        else:
            time.sleep(sum(self.tempos)*60)  
            for prog in self.programas:
                if prog['abrir'] == 1:
                    subprocess.Popen(prog['caminho']) 

# Classe que define a ação do btn "Próximo"
class Btn_Commands:
    def __init__(self, frames, janelaPrincipal, Label_block, Frames_block, buttons_block):
        self.janela = janelaPrincipal
        self.blocoLabel = Label_block
        self.blocoFrames = Frames_block
        self.blocoBotoes = buttons_block
        self.frames = frames
        self.open = Open_progs(frames)
                
    def verifica_s_ou_n(self):
        print("verifica s ou n")
        self.frames.frame_programas()
    
    def quais_prog_abrir(self):
        print("verifica quais prog abrir")
        self.frames.frame_tempo()

    def abrir_agora_ou_depois(self):
        self.frames.frame_espera()
        self.open.abre_progs()
            
    def fecha_janela(self):
        self.janela.destroy()

# Classe que cria o frame 
class Frames:
    def __init__(self, janelaPrincipal, Label_block, Frames_block, buttons_block):
        self.janela = janelaPrincipal
        self.blocoLabel = Label_block
        self.blocoFrames = Frames_block
        self.blocoBotoes = buttons_block
        
        self.frm4_opt = tk.IntVar(value=0)
        self._tempos_buttons = []
        self.tempo_total = []
        self.progs_db = Dados()
        self.progs_lst = self.progs_db.lstProgs
        
        self.titulo = Label_default(self.blocoLabel)
        self.btns = Main_buttons(self.janela, self.blocoBotoes)
        self.btn_commands = Btn_Commands(self, self.janela, self.blocoLabel, self.blocoFrames, self.blocoBotoes)
        self.open = Open_progs(self)
        
            
            
    def limpar_frame(self):
        for widget in self.blocoFrames.winfo_children():
            widget.destroy()

        
    def frame_trabalho(self):
        self.titulo.atualizar_label("Você vai trabalhar hoje?")
        opt = tk.IntVar(value=0)
        radio1 = tk.Radiobutton(self.blocoFrames, text="Sim", variable=opt, value=1)
        radio1.pack()
        radio2 = tk.Radiobutton(self.blocoFrames, text="Não", variable=opt, value=0)
        radio2.pack()
        def ao_clicar_proximo():
            if opt.get() == 1:
                self.btn_commands.verifica_s_ou_n()
            else:
                self.btn_commands.fecha_janela()
        self.btns.acao_btn_prox(ao_clicar_proximo)
   
    def frame_programas(self):
        self.limpar_frame()
        for item in self.progs_lst:
            self.progs_db.vars[item['nome']] = tk.IntVar(value=item['abrir'])
            chk_btn = tk.Checkbutton(
                self.blocoFrames, 
                text=item['nome'], 
                variable=self.progs_db.vars[item['nome']], 
                onvalue=1, 
                offvalue=0,
                command=self.progs_db.atualiza_dados
            )
            chk_btn.pack()
        self.btns.acao_btn_prox(self.btn_commands.quais_prog_abrir)
    
    def frame_tempo(self):
        self.limpar_frame()
        self.titulo.atualizar_label("Abrir agora ou depois?")
        tempos = [1, 5, 10, 30]
        self._tempos_buttons = {}
        def muda_estado():
            novo_estado = "disabled" if self.frm4_opt.get() == 1 else "normal"
            for btn_tempo in self._tempos_buttons:
                btn_tempo.config(state=novo_estado)
        def add_tempo(num):
            self.tempo_total.append(num)
        radio1 = tk.Radiobutton(self.blocoFrames, text="Abrir agora", variable=self.frm4_opt, value=1, command=muda_estado)
        radio1.pack()
        radio2 = tk.Radiobutton(self.blocoFrames, text="Tempo de espera", variable=self.frm4_opt, value=0, command=muda_estado)
        radio2.pack()
        for n in tempos:
            btn = tk.Button(self.blocoFrames, text=f"+ {n} minutos", command=lambda tempo = n:add_tempo(tempo))
            self._tempos_buttons[btn] = n
            btn.pack()
        self.btns.acao_btn_prox(self.btn_commands.abrir_agora_ou_depois)
    
    ''' 
    Agora é só fazer com que o radio1 desative os botões de tempo, e que o radio2 atíve-os.
    A ação dos botões de tempo é bem simples. Você pode só ir add o valor, aí quando
    você clicar em proximo você excuta o subprocess.Popen com o tempo total*60. Simples!
    
    '''
    def frame_espera(self):
        self.limpar_frame()
        self.titulo.atualizar_label("Aguarde Mestre!")
        self.btns.acao_btn_prox(self.btn_commands.fecha_janela)

    
app = App()
app.run()  

# COMENTÁRIOS NADA SENSACIONAIS DO CAPITÃO CAVERNA
'''
Depois podemos pensar em um botão "Anterior"

dd armazena a chamada da classe Dados
dd2 armazena uma lista de dados sobre os programas (nome, caminho, etc)

dd = Dados()
dd2 = dd.X()
for item in dd2:
    print(item['nome'])
    
Class AlgumaCoisa:    
    self.var = x
    
ou seja, ele_mesmo.var = ?, = x
print(AlgumaCoisa.var)
>> x


O dicionário self.vars na classe Dados serve para armazenar as variáveis IntVar() 
de cada programa do JSON. A chave do dicionário é o nome do programa, e o valor é 
a variável IntVar() que representa se o programa deve ser aberto (1) ou não (0). 
Quando um Checkbutton é criado, ele usa essa variável vinculada ao programa 
correspondente. Assim, ao marcar ou desmarcar um Checkbutton, o valor de IntVar()
muda, e ao chamar atualizar_json(), ele percorre os programas, pega o valor
atualizado de self.vars e salva no db.json, garantindo que a interface gráfica e 
o arquivo JSON estejam sempre sincronizados.
'''
