# -*- coding: utf-8 -*- # Boa prática: Adicionar encoding no início

import tkinter as tk
import json
import subprocess
import time
import os # Adicionado para verificar existência do arquivo JSON

# Classe que cria a janela
class App:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Start Sharp")
        # self.janela.geometry("800x600") # Desnecessário se comentado. Remova ou use.
        # Base_frame agora recebe a janela principal (self.janela)
        self.base_frame = Base_frame(self.janela)

    def run(self):
        self.janela.mainloop()

# Classe que importa e trata dados json
class Dados:
    # Melhoria: Definir o nome do arquivo como uma constante ou atributo
    DB_FILENAME = 'db.json'

    def __init__(self):
        # Melhoria: Tratar exceção caso o arquivo não exista ou seja inválido
        self.dados = None
        self.lstProgs = []
        self.vars = {} # Dicionário para guardar as tk.IntVar dos checkboxes

        try:
            # Verificação se o arquivo existe antes de tentar abrir
            if os.path.exists(self.DB_FILENAME):
                with open(self.DB_FILENAME, 'r', encoding='utf-8') as arquivo:
                    self.dados = json.load(arquivo)
                    # Melhoria: Validar se a chave 'programas' existe e é uma lista
                    if isinstance(self.dados.get("programas"), list):
                        self.lstProgs = self.dados["programas"]
                    else:
                        print(f"Aviso: Chave 'programas' não encontrada ou inválida em {self.DB_FILENAME}.")
                        self.dados = {"programas": []} # Define um padrão seguro
            else:
                print(f"Aviso: Arquivo {self.DB_FILENAME} não encontrado. Criando um padrão.")
                self.dados = {"programas": []} # Cria um dicionário padrão se o arquivo não existe
                # Opcional: Salvar o arquivo padrão recém-criado
                # self._salvar_dados()

        except json.JSONDecodeError:
            print(f"Erro: Falha ao decodificar JSON em {self.DB_FILENAME}.")
            # Considerar carregar um padrão ou encerrar
            self.dados = {"programas": []}
        except Exception as e:
            print(f"Erro inesperado ao ler {self.DB_FILENAME}: {e}")
            self.dados = {"programas": []}

        # Pré-popular self.vars baseado nos dados carregados
        # Movido para 'frame_programas' onde as IntVars são criadas.

    # Método privado para encapsular a lógica de salvar
    def _salvar_dados(self):
         # Melhoria: Tratar exceções na escrita do arquivo
        try:
            with open(self.DB_FILENAME, 'w', encoding='utf-8') as arquivo: # 'w' é mais seguro para sobrescrever
                json.dump(self.dados, arquivo, indent=4, ensure_ascii=False) # ensure_ascii=False para UTF-8
        except Exception as e:
            print(f"Erro ao salvar dados em {self.DB_FILENAME}: {e}")

    # Renomeado para refletir a ação (salvar o estado atual das vars no self.dados)
    def preparar_para_salvar(self):
        # Redundância Removida: Não precisa reler o arquivo aqui.
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


# Classe que divide a janela em três blocos
class Base_frame:
    # Simplificação: Se Base_frame só serve para criar os 3 blocos e
    # iniciar Frames, talvez pudesse ser mesclada com App ou Frames.
    # Mas mantendo a estrutura:
    def __init__(self, janelaPrincipal):
        # self.janela = janelaPrincipal # Redundante se só usado para passar adiante
        # Cria os frames diretamente no container passado (janelaPrincipal)
        self.blocoLabel = tk.Frame(janelaPrincipal)
        self.blocoLabel.pack(pady=5) # Adicionar um pouco de espaço vertical
        self.blocoFrames = tk.Frame(janelaPrincipal)
        self.blocoFrames.pack(pady=5, padx=10, fill=tk.BOTH, expand=True) # Permitir expansão
        self.blocoBotoes = tk.Frame(janelaPrincipal)
        self.blocoBotoes.pack(pady=5)

        # Passa os blocos recém-criados para Frames
        # Passa também a janela principal para outras classes que possam precisar dela
        self.frames = Frames(janelaPrincipal, self.blocoLabel, self.blocoFrames, self.blocoBotoes)
        # A inicialização do primeiro frame agora é feita dentro de Frames.__init__


# Classe que cria o label (Título)
class Label_default:
    # Simplificação: Similar a Main_buttons, é uma classe muito específica.
    # Poderia ser um método dentro de Frames ou apenas criado diretamente lá.
    # Mantendo a estrutura:
    def __init__(self, parent_frame): # Renomeado para clareza (parent_frame)
        # self.blocoLabel = parent_frame # Redundante se não usado em outros métodos
        self.label = tk.Label(parent_frame, text="", font=("Arial", 12)) # Texto inicial vazio, fonte maior
        self.label.pack()

    def atualizar_label(self, texto):
        self.label.config(text=texto)

# Classe que cria btn "Próximo" e "Cancelar"
class Main_buttons():
    # Simplificação: Mesma observação de Label_default.
    # Mantendo a estrutura:
    def __init__(self, janelaPrincipal, parent_frame): # Renomeado para clareza
        self.janela = janelaPrincipal # Necessário para o botão Cancelar
        # self.blocoBotoes = parent_frame # Redundante

        # Melhoria: Usar side=tk.LEFT ou tk.RIGHT para colocar botões lado a lado
        self.btn_proximo = tk.Button(parent_frame, text="Próximo")
        self.btn_proximo.pack(side=tk.RIGHT, padx=5) # Botão próximo à direita
        self.btn_cancelar = tk.Button(parent_frame, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.pack(side=tk.RIGHT, padx=5) # Botão cancelar à esquerda do próximo

    # Renomeado para clareza: set_next_action
    def set_next_action(self, acao):
        self.btn_proximo.config(command=acao)

    def cancelar(self):
        # Ação de cancelar pode precisar salvar o estado antes de fechar
        # Ex: self.dados_ref.salvar_estado_atual() # Precisaria da referência a Dados
        print("Ação cancelada.") # Feedback
        self.janela.destroy()

# Classe que abre programas
class Open_progs:
    # Melhoria: Receber a lista de programas e a janela principal
    def __init__(self, janela, programas_para_abrir):
        self.janela = janela # Necessário para usar o 'after'
        self.programas = programas_para_abrir # Recebe a lista filtrada
        # self.opt = frames.frm4_opt # Não mais necessário, decisão feita antes
        # self.tempos = frames.tempo_total # Não mais necessário, delay calculado antes

    # Melhoria: Separar lógica de abrir do cálculo de delay
    def _abrir_executaveis(self):
        print(f"Abrindo {len(self.programas)} programas selecionados...")
        for prog in self.programas:
            # Melhoria: Adicionar tratamento de erro para Popen
            try:
                print(f"  -> Abrindo: {prog['nome']} (Caminho: {prog['caminho']})")
                subprocess.Popen(prog['caminho'])
            except FileNotFoundError:
                print(f"Erro: Caminho não encontrado para {prog['nome']}: {prog['caminho']}")
            except Exception as e:
                print(f"Erro ao abrir {prog['nome']}: {e}")
        # Após abrir (ou tentar abrir) os programas, pode fechar a janela de configuração
        # Opcional: Adicionar um pequeno delay antes de fechar para o usuário ver a mensagem
        self.janela.after(1500, self.janela.destroy) # Fecha após 1.5 segundos

    # Renomeado: schedule_opening
    def schedule_opening(self, delay_segundos=0):
        if delay_segundos > 0:
            print(f"Programas serão abertos em {delay_segundos} segundos.")
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
    # Simplificação: Esta classe é essencialmente um controlador de fluxo.
    # Poderia ser métodos dentro da classe Frames, que gerencia os próprios frames.
    # Mantendo a estrutura:
    def __init__(self, frames_manager): # Recebe a instância de Frames
        self.frames_manager = frames_manager # Referência ao gerenciador de frames (classe Frames)
        # self.janela = janelaPrincipal # Obtido via frames_manager se necessário
        # self.blocoLabel = Label_block # Gerenciado por Frames
        # self.blocoFrames = Frames_block # Gerenciado por Frames
        # self.blocoBotoes = buttons_block # Gerenciado por Frames
        # self.open = Open_progs(frames) # Instância de Open_progs criada em Frames

    # Ações chamadas pelo botão "Próximo" em cada etapa

    # Etapa 1 -> 2: Decidiu trabalhar
    def ir_para_selecao_programas(self):
        # print("Indo para seleção de programas") # Debug, remover
        self.frames_manager.frame_programas()

    # Etapa 2 -> 3: Selecionou programas
    def ir_para_definir_tempo(self):
        # print("Indo para definir tempo") # Debug, remover
        # Antes de ir para a próxima tela, salva o estado dos checkboxes
        self.frames_manager.progs_db.salvar_estado_atual()
        self.frames_manager.frame_tempo()

    # Etapa 3 -> 4: Definiu tempo e confirma abertura
    def iniciar_abertura(self):
        # print("Iniciando processo de abertura") # Debug, remover
        self.frames_manager.confirmar_e_abrir() # Chama método em Frames para finalizar

    # Etapa 1 -> Fim: Decidiu NÃO trabalhar
    def fechar_aplicacao(self):
        # print("Fechando aplicação (não vai trabalhar)") # Debug, remover
        self.frames_manager.janela.destroy()


# Classe que cria os frames (Gerenciador de UI/Fluxo)
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

        opt = tk.IntVar(value=1) # 1 para Sim, 0 para Não
        radio1 = tk.Radiobutton(self.blocoFrames, text="Sim", variable=opt, value=1)
        radio1.pack(anchor=tk.W) # Alinhar à esquerda (West)
        radio2 = tk.Radiobutton(self.blocoFrames, text="Não", variable=opt, value=0)
        radio2.pack(anchor=tk.W)

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

        # Itera sobre a lista de programas carregada pela instância Dados
        if not self.progs_db.lstProgs:
             tk.Label(self.blocoFrames, text="Nenhum programa configurado em db.json").pack()

        for item in self.progs_db.lstProgs:
            nome_prog = item['nome']
            # Cria a tk.IntVar e a armazena no dicionário 'vars' da instância Dados
            # Usa o valor 'abrir' do JSON como valor inicial
            var = tk.IntVar(value=item.get('abrir', 0)) # Pega 'abrir', default 0 se não existir
            self.progs_db.vars[nome_prog] = var

            chk_btn = tk.Checkbutton(
                self.blocoFrames,
                text=nome_prog,
                variable=var, # Usa a variável recém-criada
                onvalue=1,
                offvalue=0
                # Removido: command=self.progs_db.atualiza_dados
                # A atualização agora é feita de uma vez antes de salvar ou avançar
            )
            chk_btn.pack(anchor=tk.W) # Alinha checkboxes à esquerda

        # Configura o botão Próximo para ir para a definição de tempo
        self.btns.set_next_action(self.btn_commands.ir_para_definir_tempo)


    def frame_tempo(self):
        self.limpar_frame()
        self.titulo.atualizar_label("Abrir agora ou definir um tempo de espera?")

        # Container para os botões de tempo, para melhor layout
        tempo_frame = tk.Frame(self.blocoFrames)

        # Função para habilitar/desabilitar botões de tempo
        def muda_estado_botoes_tempo():
            estado = "disabled" if self.frm4_opt.get() == 1 else "normal"
            for btn in self._tempos_buttons_widgets:
                btn.config(state=estado)
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
        radio1.pack(anchor=tk.W)
        radio2 = tk.Radiobutton(self.blocoFrames, text="Esperar:", variable=self.frm4_opt, value=0, command=muda_estado_botoes_tempo)
        radio2.pack(anchor=tk.W)

        # Coloca o frame de botões de tempo abaixo do RadioButton "Esperar:"
        tempo_frame.pack(anchor=tk.W, padx=20) # Indentado

        # Label para mostrar o tempo total acumulado
        self.label_tempo_total = tk.Label(tempo_frame, text="Tempo total: 0 segundos")
        self.label_tempo_total.pack(side=tk.BOTTOM, pady=5)

        # Botões para adicionar tempo (+1 min, +5 min, etc.)
        tempos_minutos = [1, 5, 10, 30]
        for minutos in tempos_minutos:
            segundos = minutos * 60
            btn = tk.Button(tempo_frame, text=f"+ {minutos} min", command=lambda s=segundos: add_tempo(s))
            btn.pack(side=tk.LEFT, padx=2) # Lado a lado
            self._tempos_buttons_widgets.append(btn) # Guarda referência para ativar/desativar

        # Garante que o estado inicial dos botões de tempo está correto
        muda_estado_botoes_tempo()

        # Configura o botão Próximo para iniciar a abertura
        self.btns.set_next_action(self.btn_commands.iniciar_abertura)

    # Método auxiliar para atualizar o label de tempo
    def atualizar_label_tempo_total(self):
        if hasattr(self, 'label_tempo_total'): # Verifica se o label existe
             total_min = self.tempo_total_segundos // 60
             total_sec = self.tempo_total_segundos % 60
             self.label_tempo_total.config(text=f"Tempo total: {total_min} min {total_sec} seg")


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
        tk.Label(self.blocoBotoes, text="Processando...").pack()


        # Chama o método para agendar ou iniciar a abertura
        opener.schedule_opening(delay)

        # Não chama mais frame_espera, a lógica de espera/fechamento
        # está agora dentro de Open_progs usando 'after'.


# --- Inicialização da Aplicação ---
if __name__ == "__main__": # Boa prática: proteger execução do script
    app = App()
    app.run()