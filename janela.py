import tkinter as tk
from tkinter import messagebox

def mostraFrase():
    nome = entryNome.get()
    messagebox.showinfo( 'Saudações', 'Bom dia' + nome)

janela = tk.Tk()
janela.geometry('980x740')
janela.title('Curso Pythom Senai')

frase = tk.Label(janela,text='Meu primeiro progama grafico',bg='magenta',fg='black',font=('Areal',25))
frase.pack(padx=5,pady=10)

labelNome = tk.Label(janela,text='Qual o seu nome?',font=('Arel',15))
labelNome.pack(padx=5,pady=10)

entryNome = tk.Entry(janela,font=('Areal',12))
entryNome.pack(padx=5,pady=10)

buttonFrase = tk.Button(janela,text='Clique-me',command=mostraFrase)
buttonFrase.pack(padx=5,pady=10)

janela.mainloop()


