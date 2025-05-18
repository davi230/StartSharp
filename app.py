import tkinter as tk
from tkinter import ttk
import json
import subprocess
import os
import sys
from tkinter import filedialog
import estilos
    
# Classe que cria a janela
class App:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Start Sharp")
        # Base_frame agora recebe a janela principal (self.janela)
        self.base_frame = Base_frame(self.janela)
        estilos.Aplica_estilos.janela(self.janela)
       
    def run(self):
        self.janela.mainloop() 

def resource_path(rel_path):
    """Garante o caminho correto para arquivos ao rodar com PyInstaller"""
    try:
        # PyInstaller cria a pasta temporária _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)

# Classe que importa e trata dados json
class Dados:
    DB_PROGRAMAS = resource_path('db.json')
    def __init__(self):
        self.dados = None
        self.lstProgs = []
        self.vars = {} # Dicionário para guardar as tk.IntVar dos Checkbuttons (Frames.frame_programas)
        self.programa_to_add = {}
        self.entry_var = tk.StringVar()
        self.caminho_var = tk.StringVar()
        
        try:
            # Verificação se o arquivo existe antes de tentar abrir
            if os.path.exists(self.DB_PROGRAMAS):
                with open(self.DB_PROGRAMAS, 'r', encoding='utf-8') as arquivo:
                    self.dados = json.load(arquivo)
                    # Validar se a chave 'programas' existe e é uma lista
                    if isinstance(self.dados.get('programas'), list):
                        self.lstProgs = self.dados['programas']
                    else:
                        print(f"Aviso: Chave 'programas' não encontrada ou inválida em {self.DB_PROGRAMAS}.")
                        self.dados = {'programas': []}
            else:
                print(f"Aviso: Arquivo {self.DB_PROGRAMAS} não encontrado. Criando um padrão.")
                self.dados = {"programas": []} # Cria um dicionário padrão se o arquivo não existe
                # Opcional: Salvar o arquivo padrão recém-criado
                # self._salvar_dados()
        except json.JSONDecodeError:
            print(f"Erro: Falha ao decodificar JSON em {self.DB_PROGRAMAS}.")
            # Considerar carregar um padrão ou encerrar
            self.dados = {"programas": []}
        except Exception as e:
            print(f"Erro inesperado ao ler {self.DB_PROGRAMAS}: {e}")
            self.dados = {"programas": []}
    
    def _salvar_dados(self):
        try:
            with open(self.DB_PROGRAMAS, 'w', encoding='utf-8') as arquivo:
                json.dump(self.dados, arquivo, indent=4, ensure_ascii=False) # ensure_ascii=False para UTF-8
        except Exception as e:
            print(f"Erro ao salvar dados em {self.DB_PROGRAMAS}: {e}")

    def preparar_para_salvar(self):
        # Não precisa reler o arquivo aqui.
        # Modifica diretamente self.dados que já foi carregado no __init__.
        if self.dados and 'programas' in self.dados:
            for programa in self.dados['programas']:
                # Atualiza o dicionário interno 'abrir' com base no valor da IntVar correspondente
                if programa["nome"] in self.vars:
                    programa['abrir'] = self.vars[programa["nome"]].get()
    
    # Método explícito para salvar, chamado quando necessário (ex: ao fechar ou avançar)
    def salvar_estado_atual(self):
        self.preparar_para_salvar() # Garante que self.dados está atualizado com as vars
        self._salvar_dados()      # Salva o self.dados no arquivo

    def adicionar_programa(self):
        nome = self.entry_var.get()
        caminho = self.caminho_var
        
        self.programa_to_add = {
            "nome": nome,
            "caminho": caminho,
            "abrir": 0
        }
        self.dados["programas"].append(self.programa_to_add)
        self.salvar_estado_atual()    
        self.atualizar_lista_interna()
        print(f"add prog {self.dados["programas"]}")
    
    def atualizar_lista_interna(self):
        """Atualiza lstProgs com base em self.dados após exclusão ou adição."""
        self.lstProgs = self.dados.get("programas", [])
        self.vars.clear()

        
    def excluir_programa(self):
        self.salvar_estado_atual()
        self.dados["programas"] = [
            prog for prog in self.dados["programas"]
                if prog["abrir"] == 0
    ]
        self.salvar_estado_atual()
        self.atualizar_lista_interna()
        print(f"Nova db sem progs excluidos: {self.dados["programas"]}")
        
# Classe que divide a janela em três blocos
class Base_frame:
    '''
    Se Base_frame só serve para criar os 3 blocos e
    iniciar Frames, talvez pudesse ser mesclada com App ou Frames.
    Mas mantendo a estrutura:
    '''
    def __init__(self, janelaPrincipal):
        
        self.blocoLabel = tk.Frame(janelaPrincipal)
        self.blocoLabel.pack()
        self.blocoFrames = tk.Frame(janelaPrincipal)
        self.blocoFrames.pack()
        self.blocoBotoes = tk.Frame(janelaPrincipal)
        self.blocoBotoes.pack()
        estilos.Aplica_estilos.lbBlock(self.blocoLabel)
        estilos.Aplica_estilos.frBlock(self.blocoFrames)
        estilos.Aplica_estilos.btnBlock(self.blocoBotoes)
    
        # Passa os blocos recém-criados para Frames
        # Passa também a janela principal para outras classes que possam precisar dela
        self.frames = Frames(janelaPrincipal, self.blocoLabel, self.blocoFrames, self.blocoBotoes)
        # A inicialização do primeiro frame agora é feita dentro de Frames.__init__
        
# Classe que cria o label (Título)
class Label_default:
    '''
    Simplificação: Similar a Main_buttons, é uma classe muito específica.
    Poderia ser um método dentro de Frames ou apenas criado diretamente lá.
    Mantendo a estrutura:
    '''
    def __init__(self, parent_frame): # Renomeado para clareza (parent_frame)
        self.label = tk.Label(parent_frame, text="") # Texto inicial vazio
        self.label.pack()
        self.label.pack_configure()
        estilos.Aplica_estilos.label(self.label)
        
    def atualizar_label(self, texto):
        self.label.config(text=texto)
   
# Classe que cria btn "Próximo" e "Cancelar"
class Main_buttons():
    
    def __init__(self, janelaPrincipal, parent_frame):
        self.janela = janelaPrincipal
        
        self.btn_reset = tk.Button(parent_frame, text="Reset")
        self.btn_reset.pack()
        self.btn_proximo = tk.Button(parent_frame, text="Próximo")
        self.btn_proximo.pack()
        self.btn_cancelar = tk.Button(parent_frame, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.pack()
        # estilos.Aplica_estilos.button(self.btn_reset, self.btn_proximo, self.btn_cancelar)
        
        
    # Renomeado para clareza: set_next_action
    def set_next_action(self, acao):
        self.btn_proximo.config(command=acao)
    
    def cancelar(self):
        # Ação de cancelar pode precisar salvar o estado antes de fechar
        # Ex: self.dados_ref.salvar_estado_atual() # Precisaria da referência a Dados
        print("Ação cancelada.") # Feedback
        self.janela.destroy()
        
    def reset(self, acao):
        print("Voltando ao primeiro frame")
        self.btn_reset.config(command=acao)
        
    
        
# Classe que abre programas
class Open_progs:
    # Receber a lista de programas e a janela principal
    def __init__(self, janela, programas_para_abrir):
        
        self.janela = janela # Necessário para usar o 'after'
        self.programas = programas_para_abrir # Recebe a lista filtrada
    
    def _abrir_executaveis(self):
        print(f"Abrindo {len(self.programas)} programas selecionados...")
        for prog in self.programas:
            try:
                print(f"  -> Abrindo: {prog['nome']} (Caminho: {prog['caminho']})")
                subprocess.Popen(prog['caminho'])
            except FileNotFoundError:
                print(f"Erro: Caminho Não encontrado para o programa {prog['nome']}: {prog['caminho']}")
            except Exception as e:
                print(f"Erro ao abrir {prog['nome']}: {e}")
        # Após abrir (ou tentar abrir) os programas, pode fechar a janela de configuração
        # Opcional: Adicionar um pequeno delay antes de fechar para o usuário ver a mensagem
        self.janela.after(1500, self.janela.destroy) # Fecha após 1.5 segundos   
        
    def schedule_opening(self, delay_segundos=0):
        if delay_segundos > 0:
            print(f"Os programas serão abertos em {delay_segundos} segundos.")
            # Boa Prática: Usar 'after' para não bloquear a GUI
            delay_ms = delay_segundos * 1000
            # Atualiza label para indicar espera (precisaria da referência ao label)
            # self.label_ref.atualizar_label(f"Aguarde {delay_segundos}s...")
            self.janela.after(delay_ms, self._abrir_executaveis)
        else:
            print("Abrindo programas agora.")
            self._abrir_executaveis() # Abre imediatamente
                
# Classe que define a ação do btn "Próximo" (Controlador de Fluxo)
class Btn_Commands:
    '''
    Esta classe é essencialmente um controlador de fluxo.
    Poderia ser métodos dentro da classe Frames, 
    que gerencia os próprios frames.
    '''
    def __init__(self, frames_manager):
        self.frames_manager = frames_manager
    
    # Ações chamadas pelo botão "Próximo" em cada etapa
    
    # Etapa 1 -> 2: Decidiu trabalhar           
    def ir_para_selecao_programas(self):
        self.frames_manager.frame_programas()
    
    # Etapa 2 -> 3: Selecionou programas
    def ir_para_definir_tempo(self):
        # Antes de ir para a próxima tela, salva o estado dos checkboxes
        self.frames_manager.progs_db.salvar_estado_atual()
        self.frames_manager.frame_tempo()

    # Etapa 3 -> 4: Definiu tempo e confirma abertura
    def iniciar_abertura(self):
        self.frames_manager.confirmar_e_abrir() # Chama método em Frames para finalizar

    # Etapa 1 -> Fim: Decidiu NÃO trabalhar        
    def fechar_aplicacao(self):
        self.frames_manager.janela.destroy()
        
    def reset(self):
        self.frames_manager.frame_trabalho()
        
    

# Classe que cria o frame (Gerenciador de UI/Fluxo)
class Frames:
    def __init__(self, janelaPrincipal, label_block, frames_block, buttons_block):
        
        self.janela = janelaPrincipal
        # Blocos de layout
        self.blocoLabel = label_block
        self.blocoFrames = frames_block
        self.blocoBotoes = buttons_block
        
        # Componentes de UI reutilizáveis
        self.titulo = Label_default(self.blocoLabel)
        self.btns = Main_buttons(self.janela, self.blocoBotoes)
        self.btns.btn_reset.config(command=lambda:self.btns.reset(self.btn_commands.reset()))
        
        #self.lb_process = tk.Label(self.blocoBotoes, text="Processando...")
        
        # Gerenciamento de dados
        self.progs_db = Dados() # Instância única para dados
        
        # Estado da UI
        self.frm4_opt = tk.IntVar(value=1) # Padrão é "Abrir agora"
        self._tempos_buttons_widgets = [] # Lista para guardar os botões de tempo
        self.tempo_total_segundos = 0 # Acumulador para o tempo de espera
        
        # Controlador de fluxo (ações do botão Próximo)
        self.btn_commands = Btn_Commands(self) # Passa a si mesma (Frames)
        
        # Inicia o primeiro frame
        self.frame_trabalho()
            
    def limpar_frame(self):
        # Limpa apenas o bloco central onde o conteúdo dinâmico aparece
        for widget in self.blocoFrames.winfo_children():
            widget.destroy()
        # Limpa também a lista de botões de tempo, se aplicável
        self._tempos_buttons_widgets = []

    # --- Definições dos Frames ---
        
    def frame_trabalho(self):
        self.limpar_frame()
        self.titulo.atualizar_label("Você vai trabalhar hoje?")
        self.btns.btn_reset.config(state="disabled")
        self.btns.btn_proximo.pack()
        self.btns.btn_cancelar.pack()
        self.tempo_total_segundos = 0
        estilos.Aplica_estilos.button(self.btns.btn_reset, self.btns.btn_proximo, self.btns.btn_cancelar)
        #self.lb_process.destroy()
        
        opt = tk.IntVar(value=1) # 1 para Sim, 0 para Não
        radio1 = tk.Radiobutton(self.blocoFrames, text="Sim", variable=opt, value=1)
        radio1.pack()
        radio2 = tk.Radiobutton(self.blocoFrames, text="Não", variable=opt, value=0)
        radio2.pack()
        estilos.Aplica_estilos.rdbutton(radio1, radio2)
        
        def ao_clicar_proximo():
            if opt.get() == 1:
                # Chama a ação do controlador para ir para a próxima etapa
                self.btn_commands.ir_para_selecao_programas()
            else:
                # Chama a ação do controlador para fechar
                self.btn_commands.fechar_aplicacao()
                
        self.btns.set_next_action(ao_clicar_proximo)
        
   
    def frame_programas(self):
        self.limpar_frame()
        self.titulo.atualizar_label("Quais programas você quer abrir?")
        self.btns.btn_reset.config(state="normal")
        
        div_progs = tk.Frame(self.blocoFrames)
        div_progs.pack()
        div_add_progs = tk.Frame(self.blocoFrames)
        div_add_progs.pack()
        div_div_add1 = tk.Frame(div_add_progs)
        div_div_add1.pack()
        div_div_add2 = tk.Frame(div_add_progs)
        div_div_add2.pack()
        
        div_add1_midle = tk.Frame(div_div_add1)
        div_add1_midle.pack()
        div_add1_bottom = tk.Frame(div_div_add1)
        div_add1_bottom.pack()
        estilos.Aplica_estilos.div_left_right(div_progs, div_add_progs)
        estilos.Aplica_estilos.div_top_bottom(div_div_add1, div_add1_bottom, div_div_add2)
        
        # Itera sobre a lista de programas carregada pela instância Dados
        if not self.progs_db.lstProgs:
            tk.Label( div_progs, text="Nenhum programa configurado em db.json").pack()
        
        for item in self.progs_db.lstProgs:
            nome_prog = item['nome']
            # Cria a tk.IntVar e a armazena no dicionário 'vars' da instância Dados
            # Usa o valor 'abrir' do JSON como valor inicial
            var = tk.IntVar(value=item.get('abrir', 0)) # Pega 'abrir', default 0 se não existir
            self.progs_db.vars[nome_prog] = var
            
            chk_btn = tk.Checkbutton(
                div_progs, 
                text=nome_prog, 
                variable=var,  # Usa a variável recém-criada
                onvalue=1, 
                offvalue=0
            )
            chk_btn.pack()
            estilos.Aplica_estilos.chkbutton(chk_btn)
        
        def busca_caminho():
            self.progs_db.caminho_var = filedialog.askopenfilename(filetypes=[("Executáveis", "*.exe")])
            if not self.progs_db.caminho_var:
                return  # Se o usuário cancelar
        
        def add():
            self.progs_db.adicionar_programa()
            self.frame_programas()
        
        def exc():
            self.progs_db.excluir_programa()
            self.frame_programas()
            
        # Botões para adicionar ou vemover programas 
        titulo_add_prog = tk.Label(div_add1_midle, text="Adicionar Programa") 
        titulo_add_prog.pack()
        label_info_nome = tk.Label(div_add1_bottom, text="Nome:")
        label_info_nome.pack()
        entry_nome = tk.Entry(div_add1_bottom, textvariable=self.progs_db.entry_var)
        entry_nome.pack()
        btn_caminho = tk.Button(div_add1_bottom, text="Caminho", command=busca_caminho)
        btn_caminho.pack()
        btn_add_progs = tk.Button(div_div_add1, text="Adicionar", command=add) 
        btn_add_progs.pack()  
         
        btn_exc_progs = tk.Button(div_div_add2, text="Excluir Programa", command=exc) 
        btn_exc_progs.pack()  
        info = tk.Label(div_div_add2, text="Ao apertar em 'Excluir Programa', serão \nexcluídos os programas selecionados, \nentão, cuidado! Certifique-se de selecionar \nos programas a serem EXCLUÍDOS.") 
        info.pack()
        estilos.Aplica_estilos.widgets_progs_manager(titulo_add_prog, label_info_nome, entry_nome, btn_caminho, btn_add_progs, btn_exc_progs, info)
         
        # Configura o botão Próximo para ir para a definição de tempo    
        self.btns.set_next_action(self.btn_commands.ir_para_definir_tempo)
    
    def frame_tempo(self):
        self.limpar_frame()
        self.titulo.atualizar_label("Abrir agora ou depois?")
        
        # Container para os botões de tempo, para melhor layout
        tempo_frame = tk.Frame(self.blocoFrames)
        estilos.Aplica_estilos.divTempo(tempo_frame)
        # Função para habilitar/desabilitar botões de tempo
        def muda_estado_botoes_tempo():
            estado = "disabled" if self.frm4_opt.get() == 1 else "normal"
            for btn in self._tempos_buttons_widgets:
                btn.config(state=estado)
            self.label_tempo_total.config(state=estado)
        # Reseta o tempo acumulado se "Abrir agora" for selecionado
            if self.frm4_opt.get() == 1:
                self.tempo_total_segundos = 0
                # Atualizar label de tempo (se existir)
                self.atualizar_label_tempo_total()
        
        # Função para adicionar tempo (em segundos)        
        def add_tempo(segundos):
            self.tempo_total_segundos += segundos
            # print(f"Tempo total acumulado: {self.tempo_total_segundos} segundos") # Debug
            # Atualiza um label que mostra o tempo total
            self.atualizar_label_tempo_total()
        
        # Radio buttons para escolher "Agora" ou "Esperar"    
        radio1 = tk.Radiobutton(self.blocoFrames, text="Abrir agora", variable=self.frm4_opt, value=1, command=muda_estado_botoes_tempo)
        radio1.pack()
        radio2 = tk.Radiobutton(self.blocoFrames, text="Esperar: ", variable=self.frm4_opt, value=0, command=muda_estado_botoes_tempo)
        radio2.pack()
        estilos.Aplica_estilos.rdbutton(radio1, radio2)
        # Label para mostrar o tempo total acumulado
        self.label_tempo_total = tk.Label(tempo_frame, text="Tempo total: 0 segundos")
        self.label_tempo_total.pack()
        estilos.Aplica_estilos.label2(self.label_tempo_total)

        # Botões para adicionar tempo (+1 min, +5 min, etc.)
        tempos_minutos = [1, 5, 10, 30]
        for minutos in tempos_minutos:
            segundos = minutos * 60
            btn = tk.Button(tempo_frame, text=f"+{minutos} min", command=lambda s=segundos: add_tempo(s))
            btn.pack()
            estilos.Aplica_estilos.btns(btn)
            self._tempos_buttons_widgets.append(btn) # Guarda referência para ativar/desativar
        
        # Garante que o estado inicial dos botões de tempo está correto
        muda_estado_botoes_tempo()
        
        # Configura o botão Próximo para iniciar a abertura    
        self.btns.set_next_action(self.btn_commands.iniciar_abertura)
        
        tempo_frame.pack()
        
    # Método auxiliar para atualizar o label de tempo
    def atualizar_label_tempo_total(self):
        if hasattr(self, 'label_tempo_total'): # Verifica se o label existe
             total_min = self.tempo_total_segundos // 60
             total_sec = self.tempo_total_segundos % 60
             self.label_tempo_total.config(text=f"Tempo total: {total_min} min {total_sec} seg")
             estilos.Aplica_estilos.label2(self.label_tempo_total)
    
    def confirmar_e_abrir(self):
        self.limpar_frame() # Limpa os controles de tempo
        # Atualiza self.dados com os valores atuais das IntVars antes de filtrar
        self.progs_db.preparar_para_salvar()

        # Filtra a lista de programas que realmente devem ser abertos
        programas_selecionados = [
            prog for prog in self.progs_db.lstProgs if prog.get('abrir', 0) == 1
        ]

        if not programas_selecionados:
            self.titulo.atualizar_label("Nenhum programa foi selecionado para abrir.")
            # Esconde ou desabilita botão Próximo/Cancelar? Ou deixa cancelar?
            self.btns.btn_proximo.pack_forget() # Esconde Próximo
            self.btns.btn_cancelar.config(text="Fechar", command=self.janela.destroy) # Muda Cancelar para Fechar
            return # Não há mais nada a fazer

        # Cria a instância de Open_progs com a lista filtrada
        opener = Open_progs(self.janela, programas_selecionados)

        # Define o delay
        delay = 0
        if self.frm4_opt.get() == 0: # Se escolheu esperar
            delay = self.tempo_total_segundos

        # Atualiza o título para indicar o que vai acontecer
        if delay > 0:
             total_min = delay // 60
             total_sec = delay % 60
             self.titulo.atualizar_label(f"Programas abrirão em {total_min} min {total_sec} seg...")
        else:
             self.titulo.atualizar_label("Abrindo programas...")

        # Desabilita/Esconde botões enquanto espera ou abre
        self.btns.btn_proximo.pack_forget()
        self.btns.btn_cancelar.pack_forget()
        # Adiciona um label informativo no bloco de botões
        #self.lb_process.pack()
        #estilos.Aplica_estilos.processando(self.lb_process)


        # Chama o método para agendar ou iniciar a abertura
        opener.schedule_opening(delay)

        # Não chama mais frame_espera, a lógica de espera/fechamento
        # está agora dentro de Open_progs usando 'after'.


# --- Inicialização da Aplicação ---
if __name__ == "__main__": # Boa prática: proteger execução do script
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
