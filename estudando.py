import tkinter as tk

janela = tk.Tk()
janela.geometry("500x700")
janela.configure(bg="Orange")
button = tk.Button(janela)

def ola():
    print("Billie Jean")


button.configure(
    bg="Blue",
    fg="Black",
    command=ola,
    text="Clique para exibir Billie Jean no terminal",
    font=("Arial",50)
)

button.pack()
janela.mainloop()