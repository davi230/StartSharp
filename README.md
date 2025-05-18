# Gerenciador de Rotina de Trabalho/Estudo

Um programa simples e pessoal para ajudar a iniciar e gerenciar sua rotina diária de trabalho ou estudo, promovendo o equilíbrio e combatendo a procrastinação.

## Sobre o Projeto

Este programa foi desenvolvido com o objetivo de enfrentar a dificuldade inicial de começar uma rotina de trabalho ou estudo, mesmo quando se gosta da atividade. Ele age como um "porteiro" digital, apresentando a decisão de trabalhar logo ao iniciar o computador. Ao mesmo tempo, oferece controle sobre quais programas serão utilizados e em qual momento, facilitando tanto o foco no trabalho quanto a decisão consciente por um dia de lazer.

A ideia é minimizar a procrastinação ao colocar o usuário cara a cara com seu objetivo diário e, simultaneamente, ajudar a evitar o excesso de trabalho, permitindo uma decisão clara sobre ter um dia de folga.

## Funcionalidades

* **Decisão Diária:** Ao iniciar, pergunta se você pretende trabalhar/estudar no dia.
* **Gerenciamento de Programas:** Permite adicionar, visualizar e excluir programas que fazem parte da sua rotina.
* **Seleção de Programas:** Escolha quais programas serão abertos.
* **Agendamento de Abertura:** Opção para abrir os programas selecionados imediatamente ou agendar a abertura para daqui a alguns minutos.
* **Reset de Seleção:** Possibilidade de reiniciar o processo de seleção de programas e agendamento.

## Como Usar

### Pré-requisitos

* Certifique-se de ter o **Python 3** instalado no seu computador.
* Execute o `Preparativo.bat` para instalar Python e as bibliotecas necessárias.
* Aguarde a instalação finalizar.

### Instalação e Execução

1.  Faça o download do diretório completo do projeto para o seu computador.
2.  Navegue até a pasta baixada.
3.  Execute o script `StartSharp.bat` (basta dar um duplo clique).

### Fluxo do Programa

1.  Ao executar o `StartSharp.bat`, uma janela será exibida perguntando: **"Você vai trabalhar hoje?"**
2.  **Se você clicar em "Não"**: O programa será encerrado.
3.  **Se você clicar em "Sim"**: Você será direcionado para a tela de seleção de programas.

#### Tela de Seleção de Programas

* **Adicionar Programas:** Para adicionar um novo programa à sua lista:
    * Digite um nome para o programa no campo de texto.
    * Clique no botão **"Caminho"** e selecione o arquivo executável (`.exe`) do programa desejado.
    * Clique no botão **"Adicionar"**. Repita este processo para todos os programas que você costuma usar.
* **Selecionar para a Sessão:** Os programas adicionados aparecerão em uma lista com caixas de seleção. Marque as caixas dos programas que você deseja abrir.
* **Excluir Programas:** Para remover programas salvos da sua lista permanente:
    * Selecione os programas a serem excluídos na lista (clicando neles até ficar azul).
    * Clique no botão **"Excluir"**.
* Após selecionar os programas para a sessão, clique em **"Proximo"**.

#### Tela de Agendamento de Abertura

* **Abrir Imediatamente:** Clique no botão **"Abrir Agora"** para que os programas selecionados sejam abertos imediatamente. *Clicar neste botão zera qualquer tempo agendado anteriormente.*
* **Agendar Abertura:** Use os botões de adicionar minutos para definir um tempo de espera (ex: +5 min, +10 min, etc.). O tempo total será exibido.
* Após definir o tempo (ou se clicou em "Abrir Agora"), clique em **"Proximo"**. Os programas serão abertos no tempo especificado ou imediatamente.

#### Botão Reset

* Em qualquer momento nas telas de seleção de programas ou agendamento, você pode clicar em **"Reset"** para voltar ao início do processo.

### Execução Automática ao Ligar o Windows

Para que a pergunta "Você vai trabalhar hoje?" apareça automaticamente toda vez que você ligar o computador:
Você simplesmente dar dois cliques em `InicializarComWindows.bat` para que seja feito automaticamente, ou fazer manualmente:

1.  Localize o arquivo `StartSharp.bat` no diretório do projeto.
2.  Copie este arquivo (`Ctrl+C`).
3.  Abra o Executar do Windows (pressione `Win + R`).
4.  Digite `shell:startup` e pressione Enter. Isso abrirá a pasta de Inicialização do Windows.
5.  Cole o arquivo `StartSharp.bat` nesta pasta (`Ctrl+V`).

Agora, o script será executado automaticamente toda vez que o Windows iniciar, apresentando a pergunta e permitindo que você decida sobre sua rotina diária.

## Planos Futuros

Penso em implementar uma pequena tabela ou histórico simples que mostre quantos dias você clicou em "Sim" e quantos clicou em "Não" ao longo da semana. Isso poderá fornecer uma visualização simples do seu equilíbrio entre dias de trabalho/estudo e dias de folga, ajudando a identificar se há um excesso em qualquer um dos lados.

## Motivação

Este projeto nasceu da minha própria necessidade de criar um ritual de início de trabalho que me ajudasse a superar a inércia inicial e a procrastinação, ao mesmo tempo em que me desse a liberdade e a consciência de tirar um dia de folga sem culpa. A decisão explícita diária se tornou uma ferramenta poderosa para manter o foco e o equilíbrio na rotina.

---
