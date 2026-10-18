import threading
import time
import tkinter as tk
from tkinter import messagebox

import cv2
import mss
import numpy as np
import pyautogui

# Previne travamentos ao mover o mouse rapidamente para um dos cantos da tela
pyautogui.FAILSAFE = True

IMAGEM_ALVO = "aceitar.png"
CONFIANCA_MINIMA = 0.88
INTERVALO = 0.25
DURACAO_MOVIMENTO = 0.8   # Tempo para a animação do mouse
TEMPO_ESPERA_CLIQUE = 3.0  # Tempo de espera em cima do botão


class AutoAcceptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LoL Auto Accept")
        self.root.geometry("320x200")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.rodando = False
        self.thread = None

        # Rótulo de Status
        self.lbl_status = tk.Label(
            root,
            text="STATUS: DESLIGADO",
            font=("Segoe UI", 12, "bold"),
            fg="#ff5555",
            bg="#1e1e1e",
        )
        self.lbl_status.pack(pady=(25, 10))

        # Botão Ligar / Desligar
        self.btn_toggle = tk.Button(
            root,
            text="LIGAR",
            font=("Segoe UI", 11, "bold"),
            bg="#28a745",
            fg="white",
            activebackground="#218838",
            activeforeground="white",
            width=14,
            height=1,
            relief="flat",
            cursor="hand2",
            command=self.alternar_bot,
        )
        self.btn_toggle.pack(pady=10)

        # Mensagem Informativa
        self.lbl_info = tk.Label(
            root,
            text="Clique em LIGAR para iniciar a vigia",
            font=("Segoe UI", 9),
            fg="#888888",
            bg="#1e1e1e",
        )
        self.lbl_info.pack(side="bottom", pady=15)

    def alternar_bot(self):
        if not self.rodando:
            self.rodando = True
            self.lbl_status.config(text="STATUS: LIGADO (VIGIA)", fg="#50fa7b")
            self.btn_toggle.config(text="DESLIGAR", bg="#dc3545", activebackground="#c82333")
            self.lbl_info.config(text="Monitorando a tela do jogo...")

            # Roda o monitoramento numa thread separada para não travar a janela
            self.thread = threading.Thread(target=self.loop_monitoramento, daemon=True)
            self.thread.start()
        else:
            self.parar_bot()

    def parar_bot(self):
        self.rodando = False
        self.lbl_status.config(text="STATUS: DESLIGADO", fg="#ff5555")
        self.btn_toggle.config(text="LIGAR", bg="#28a745", activebackground="#218838")
        self.lbl_info.config(text="Bot pausado pelo usuário.")

    def loop_monitoramento(self):
        alvo = cv2.imread(IMAGEM_ALVO)
        if alvo is None:
            self.root.after(0, lambda: messagebox.showerror("Erro", f"Não encontrei {IMAGEM_ALVO} na pasta."))
            self.root.after(0, self.parar_bot)
            return

        altura, largura = alvo.shape[:2]

        with mss.MSS() as captura:
            monitor = captura.monitors[1]

            while self.rodando:
                frame = np.array(captura.grab(monitor))
                tela = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

                if altura <= tela.shape[0] and largura <= tela.shape[1]:
                    resultado = cv2.matchTemplate(tela, alvo, cv2.TM_CCOEFF_NORMED)
                    _, confianca, _, posicao = cv2.minMaxLoc(resultado)

                    if confianca >= CONFIANCA_MINIMA:
                        self.root.after(0, lambda: self.lbl_info.config(text="Partida encontrada! Clicando..."))

                        centro_x = monitor["left"] + posicao[0] + largura // 2
                        centro_y = monitor["top"] + posicao[1] + altura // 2

                        pyautogui.moveTo(centro_x, centro_y, duration=DURACAO_MOVIMENTO)
                        time.sleep(TEMPO_ESPERA_CLIQUE)
                        pyautogui.click()

                        self.root.after(0, lambda: self.lbl_info.config(text="Clique feito! Aguardando janela fechar..."))

                        # Espera a janela de aceitar fechar antes de voltar a vigiar
                        while self.rodando:
                            time.sleep(1)
                            frame_atual = np.array(captura.grab(monitor))
                            tela_atual = cv2.cvtColor(frame_atual, cv2.COLOR_BGRA2BGR)
                            res_atual = cv2.matchTemplate(tela_atual, alvo, cv2.TM_CCOEFF_NORMED)
                            _, conf_atual, _, _ = cv2.minMaxLoc(res_atual)

                            if conf_atual < CONFIANCA_MINIMA:
                                self.root.after(0, lambda: self.lbl_info.config(text="Monitorando a tela do jogo..."))
                                break

                time.sleep(INTERVALO)


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoAcceptApp(root)
    root.mainloop()