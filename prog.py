import tkinter as tk
from tkinter import ttk  # Para widgets com melhor aparência
from tkinter import messagebox
import statistics  # Para calcular a média facilmente

class ValueAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador de Valores")
        self.root.geometry("450x500") # Tamanho inicial da janela

        self.values = [] # Lista para armazenar os valores adicionados
        self.description_entries = {} # Dicionário para guardar as Entries de descrição

        # --- Frame de Entrada ---
        input_frame = ttk.Frame(root, padding="10")
        input_frame.pack(pady=10, fill=tk.X)

        ttk.Label(input_frame, text="Valor:").pack(side=tk.LEFT, padx=5)
        self.value_entry = ttk.Entry(input_frame, width=15)
        self.value_entry.pack(side=tk.LEFT, padx=5)
        self.value_entry.bind("<Return>", self.add_value) # Adiciona com Enter

        add_button = ttk.Button(input_frame, text="Adicionar Valor", command=self.add_value)
        add_button.pack(side=tk.LEFT, padx=5)

        # --- Frame de Resultados (Tabela) ---
        # Usaremos um Canvas e um Frame dentro dele para permitir rolagem se muitos valores forem adicionados
        canvas_frame = ttk.Frame(root, padding="5")
        canvas_frame.pack(expand=True, fill=tk.BOTH)

        self.canvas = tk.Canvas(canvas_frame)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        # Frame onde a tabela será realmente desenhada
        self.results_frame = ttk.Frame(self.canvas)

        # Configuração para a rolagem funcionar
        self.results_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.results_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # --- Frame de Sumário e Controles ---
        summary_control_frame = ttk.Frame(root, padding="10")
        summary_control_frame.pack(pady=10, fill=tk.X)

        # Label para mostrar média e menores valores
        self.summary_label = ttk.Label(summary_control_frame, text="Aguardando cálculo...", wraplength=400)
        self.summary_label.pack(pady=5)

        # Botões de controle
        control_buttons_frame = ttk.Frame(summary_control_frame)
        control_buttons_frame.pack(pady=5)

        calculate_button = ttk.Button(control_buttons_frame, text="Calcular e Mostrar Tabela", command=self.calculate_and_display)
        calculate_button.pack(side=tk.LEFT, padx=10)

        clear_button = ttk.Button(control_buttons_frame, text="Limpar Tudo", command=self.clear_all)
        clear_button.pack(side=tk.LEFT, padx=10)


    def add_value(self, event=None): # event=None para funcionar com botão e Enter
        """Adiciona um valor à lista."""
        try:
            value_str = self.value_entry.get().replace(',', '.') # Aceita vírgula como decimal
            value = float(value_str)
            self.values.append(value)
            self.value_entry.delete(0, tk.END) # Limpa o campo de entrada
            print(f"Valor adicionado: {value}. Valores atuais: {self.values}") # Log no console (opcional)
            # Atualiza o label de sumário temporariamente ou deixa para o cálculo final
            # self.summary_label.config(text=f"{len(self.values)} valor(es) adicionado(s).")
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, insira um número válido.")
            self.value_entry.delete(0, tk.END)

    def calculate_and_display(self):
        """Calcula a média, os menores valores e exibe a tabela."""
        # Limpa resultados anteriores (widgets dentro do frame)
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        self.description_entries.clear() # Limpa o dicionário de entries

        if not self.values:
            self.summary_label.config(text="Nenhum valor adicionado para calcular.")
            return

        # --- Cálculos ---
        try:
            average = statistics.mean(self.values)
            average_str = f"{average:.2f}" # Formata com 2 casas decimais
        except statistics.StatisticsError:
            average_str = "N/A" # Caso de lista vazia (já tratado, mas seguro)

        sorted_values = sorted(list(set(self.values))) # Usa set para pegar valores únicos e depois ordena
        lowest1_str = "N/A"
        lowest2_str = "N/A"

        if len(sorted_values) >= 1:
            lowest1_str = f"{sorted_values[0]}"
        if len(sorted_values) >= 2:
            lowest2_str = f"{sorted_values[1]}"

        # --- Atualiza o Sumário ---
        self.summary_label.config(text=f"Média: {average_str} | Menor Valor: {lowest1_str} | 2º Menor Valor: {lowest2_str}")

        # --- Cria a Tabela ---
        # Cabeçalhos
        ttk.Label(self.results_frame, text="Valor", font=('Arial', 10, 'bold'), borderwidth=1, relief="solid", padding=3).grid(row=0, column=0, sticky="nsew", padx=(5,0), pady=(5,0))
        ttk.Label(self.results_frame, text="Descrição (editável)", font=('Arial', 10, 'bold'), borderwidth=1, relief="solid", padding=3).grid(row=0, column=1, sticky="nsew", padx=(0,5), pady=(5,0))

        # Linhas com valores e campos de descrição
        for i, value in enumerate(self.values):
            # Label para o valor
            value_label = ttk.Label(self.results_frame, text=f"{value}", borderwidth=1, relief="solid", padding=3)
            value_label.grid(row=i + 1, column=0, sticky="nsew", padx=(5,0))

            # Entry para a descrição (editável)
            desc_entry = ttk.Entry(self.results_frame, width=30) # Ajuste a largura conforme necessário
            desc_entry.grid(row=i + 1, column=1, sticky="nsew", padx=(0,5))
            # Guarda a referência da Entry para poder ler depois, se precisar
            self.description_entries[i] = desc_entry # Usa o índice como chave

        # Configura o grid do results_frame para expandir as colunas
        self.results_frame.grid_columnconfigure(0, weight=1)
        self.results_frame.grid_columnconfigure(1, weight=3) # Dá mais espaço para descrição

        # Força a atualização do canvas após adicionar widgets
        self.results_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def clear_all(self):
        """Limpa todos os dados e a interface."""
        self.values = []
        self.value_entry.delete(0, tk.END)
        self.summary_label.config(text="Aguardando cálculo...")

        # Limpa a tabela (widgets dentro do frame)
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        self.description_entries.clear()

        # Reseta a região de rolagem do canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        print("Todos os dados foram limpos.")


# --- Inicia a aplicação ---
if __name__ == "__main__":
    main_window = tk.Tk()
    app = ValueAnalyzerApp(main_window)
    main_window.mainloop()