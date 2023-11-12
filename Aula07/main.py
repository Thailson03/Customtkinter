import customtkinter as ctk

janela = ctk.CTk()

#configurando a janela principal
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=600)
janela.minsize(width=500, height=250)
janela.resizable(width=False, height=False)

#Aula 07 = TextBox (Caixa de texto no Customtkinter)
textbox = ctk.CTkTextbox(janela, width=300, height=350)
textbox.pack()

textbox.insert("0.0", "Título do seu texto\n\n" + "Ola dev, estou aqui programando interfaces graficas com customtkinter no canal set-escola de programacao e esta sendo uma boa.\n\n"*20)

janela.mainloop()