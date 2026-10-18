# 🎮 LoL Auto Accept Bot

Um bot simples, eficiente e seguro com interface gráfica desenvolvido em Python para aceitar partidas de **League of Legends** automaticamente.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)

---

## 🚀 Funcionalidades

* **🖥️ Interface Gráfica Prática**: Botão de **LIGAR / DESLIGAR** intuitivo construído com `tkinter`.
* **🔍 Detecção por Visão Computacional**: Localização precisa do botão "ACEITAR!" usando *Template Matching* com OpenCV (`cv2.matchTemplate`).
* **🖱️ Movimentação Humanizada**: Movimento suave do cursor até o botão para simular um clique natural.
* **⏳ Tempo de Espera Configurável**: Aguarda 3 segundos com o ponteiro sobre o botão antes de efetuar o clique.
* **🔄 Vigia Contínua Inteligente**: Se a partida for recusada por outro jogador, o bot identifica o retorno à fila e fica de prontidão automaticamente para a próxima chamada.
* **⚡ Baixo Consumo de Recursos**: Execução otimizada em *thread* separada com capturas de tela ultra rápidas (`mss`).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **OpenCV (`opencv-python`)**: Processamento de imagem e detecção do modelo.
* **MSS (`mss`)**: Captura de tela em alta performance.
* **PyAutoGUI (`pyautogui`)**: Automação e movimentação do mouse.
* **NumPy (`numpy`)**: Manipulação de matrizes de imagem.
* **Tkinter**: Interface gráfica nativa do Python.

---

## 📋 Pré-requisitos

* Sistema Operacional: **Windows** (devido às configurações de escala de tela e coordenadas).
* **Python 3.8** ou superior instalado no sistema.
* Cliente do **League of Legends**.

---

## 🔧 Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/lol-auto-accept.git
   cd lol-auto-accept
   ```

2. **Crie e ative um ambiente virtual (`.venv`)**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install opencv-python mss numpy pyautogui
   ```

---

## 🎯 Como Usar

### Opção 1: Pela Interface do VS Code / Terminal
1. Garanta que a imagem `aceitar.png` está recortada rente ao botão e presente na raiz da pasta do projeto.
2. Execute o arquivo principal:
   ```bash
   python main.py
   ```
3. Clique no botão **LIGAR** na janela que abrir para iniciar o monitoramento.

### Opção 2: Pelo Atalho do Windows (Sem abrir o terminal)
1. Dê 2 cliques no arquivo `Iniciar.bat`.
2. A janela do **LoL Auto Accept** abrirá diretamente sem janelas pretas do CMD ao fundo.

---

## 📁 Estrutura do Projeto

```text
lol-auto-accept/
├── .venv/               # Ambiente virtual Python
├── aceitar.png          # Recorte de referência do botão "ACEITAR!"
├── Iniciar.bat          # Atalho para execução rápida no Windows
├── main.py              # Código fonte principal (GUI + Lógica do Bot)
└── README.md            # Documentação do projeto
```

---

## ⚠️ Observações Importantes

* **Resolução e Escala (DPI)**: A imagem `aceitar.png` deve ser capturada na mesma tela e com a mesma resolução/escala em que o cliente do LoL é executado.
* **Privilégios de Administrador**: Caso o cliente do jogo esteja sendo executado como Administrador, execute a aplicação ou o atalho `.bat` também como Administrador para permitir que os cliques do mouse sejam aceitos pelo jogo.
* **Mover para Cancelar**: O recurso `FAILSAFE` do PyAutoGUI está ativo. Se precisar interromper o movimento do mouse em emergências, mova o cursor rapidamente para o canto superior esquerdo da tela.

---

## 📄 Licença

Este projeto é de código aberto sob a licença [MIT](LICENSE).