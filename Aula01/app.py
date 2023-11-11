import customtkinter as ctk#Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela

#janela._set_appearance_mode("dark")

btn = ctk.CTkButton(janela, text="Ola", fg_color="#900090", hover_color="#611f61")
btn.pack()

janela.mainloop()