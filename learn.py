"""🟢 Exercício 1 (Fácil)

Crie uma janela com:

Título: Meu Primeiro Programa
Tamanho: 400x200
Fundo branco

Dentro dela:

Um Label escrito "Digite seu nome:"
Uma Entry
Um Button

Quando clicar no botão, imprima no terminal:

Olá Miguel!

(Substitua Miguel pelo que foi digitado.)"""

import tkinter as tk

janela = tk.Tk()

janela.geometry("200x200")
janela.configure(bg="Green")

texto = tk.Label(janela)

texto.configure(bg="Green",
                fg="Brown",
                text="Three:🌳, Digite seu nome: ",
                font=("Arial", 50))

entrada = tk.Entry(janela)
def printacao():
    print(entrada.get())


button = tk.Button(janela)
button.configure(bg="White",
                 fg="Black",
                 text="imprimir",
                 font=("Arial", 50),
                 command=printacao)



texto.pack()
entrada.pack()
button.pack()
janela.mainloop()