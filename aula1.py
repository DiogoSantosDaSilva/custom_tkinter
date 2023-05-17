import customtkinter as ctk    # Importando a biblioteca

janela = ctk.CTk()    # Criando a nossa janela


btn = ctk.CTkButton(janela, text='Olá')
btn.pack()

janela.mainloop()   # Rodando nossa janela
