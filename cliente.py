import tkinter

janela = tkinter.Tk('Cadastro de Cliente')
janela.geometry('800x600')
janela.title('Cadastro de Cliente')

labelNomeCliente = tkinter.Label(janela,text='Nome do Cliente')
labelNomeCliente.pack(padx=5,pady=5)

entryNomeCliente = tkinter.Entry(janela,width=100)
entryNomeCliente.pack(padx=5,pady=5)

labelNomeCliente = tkinter.Label(janela,text='CPF do Cliente')
labelNomeCliente.pack(padx=5,pady=5)

entryNomeCliente = tkinter.Entry(janela,width=60)
entryNomeCliente.pack(padx=5,pady=5)

labelNomeCliente = tkinter.Label(janela,text='Data de Nacimento')
labelNomeCliente.pack(padx=5,pady=5)

entryNomeCliente = tkinter.Entry(janela,width=40)
entryNomeCliente.pack(padx=5,pady=5)

labelNomeCliente = tkinter.Label(janela,text='E-mail do Cliente')
labelNomeCliente.pack(padx=5,pady=5)

entryNomeCliente = tkinter.Entry(janela,width=60)
entryNomeCliente.pack(padx=5,pady=5)

labelNomeCliente = tkinter.Label(janela,text='Celular do Cliente')
labelNomeCliente.pack(padx=5,pady=5)

entryNomeCliente = tkinter.Entry(janela,width=40)
entryNomeCliente.pack(padx=5,pady=5)

buttonGravar = tkinter.Button(janela,text='Gravar',width=20)
buttonGravar.pack(padx=5,pady=100)


janela.mainloop()







 