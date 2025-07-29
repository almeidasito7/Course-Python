import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expressao = ""

        # Tela de exibição
        self.entrada_texto = tk.StringVar()
        entrada = tk.Entry(root, textvariable=self.entrada_texto, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        entrada.grid(row=0, column=0, columnspan=4)

        # Layout dos botões
        botoes = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
        ]

        for (texto, linha, coluna) in botoes:
            self._criar_botao(texto, linha, coluna)

    def _criar_botao(self, texto, linha, coluna):
        botao = tk.Button(self.root, text=texto, padx=20, pady=20, font=("Arial", 18),
                          command=lambda: self._clicar(texto))
        botao.grid(row=linha, column=coluna, sticky="nsew")

    def _clicar(self, item):
        if item == 'C':
            self.expressao = ""
        elif item == '=':
            try:
                self.expressao = str(eval(self.expressao))
            except Exception:
                self.expressao = "Erro"
        else:
            self.expressao += str(item)
        self.entrada_texto.set(self.expressao)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
