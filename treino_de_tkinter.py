"""🟢 Desafio 1 (fácil) – Saudação

Faça um programa que:

tenha um Entry
um botão
quando clicar, apareça oque vc escrever no entry


Mas não no terminal! Em um Label na própria janela."""

import tkinter as tk

janela1 = tk.Tk()
janela1.geometry("500x500")




entrada = tk.Entry(janela1)
entrada.configure(font=("Arial", 30))



def texto_aparecer():
    escrito = entrada.get()
    if escrito:
        texto_label.configure(text=escrito)
        texto_label.pack()

texto_label = tk.Label(janela1)
texto_label.configure(bg="White",
                 fg="Green",
                 font=("Arial", 50))

button = tk.Button(janela1)
button.configure(bg="White",
                 fg="Green",
                 text="Clique aqui para exibir o texto do entry em outra janela!",
                 font=("Arial", 30),
                 command=texto_aparecer)

entrada.pack()
button.pack()
janela1.mainloop()