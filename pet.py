import tkinter
from tkinter import messagebox

def gravarPet():
    nomeTutor = entryNomeTutor.get()
    nomePet   = entryNomePet.get()
    messagebox.showinfo("Atenção"," O pet "+nomePet+" é do(a) "+nomeTutor)


janela = tkinter.Tk("Cadastro de Cliente")
janela.geometry("800x600")
janela.title("Cadastro de Pet")

labelNomeTutor = tkinter.Label(janela,text="Nome do Tutor")
labelNomeTutor.pack(padx=5,pady=5)
entryNomeTutor = tkinter.Entry(janela,width=40)
entryNomeTutor.pack(padx=5,pady=5)

labelNomePet = tkinter.Label(janela,text="Nome do Pet")
labelNomePet.pack(padx=5,pady=5)
entryNomePet = tkinter.Entry(janela,width=25)
entryNomePet.pack(padx=5,pady=5)

buttonGravar = tkinter.Button(janela,text="Gravar",width=20,command=gravarPet)           
buttonGravar.pack(padx=5,pady=100)

janela.mainloop()