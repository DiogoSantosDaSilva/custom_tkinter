import customtkinter as ctk


janela = ctk.CTk()

# Configurando a janela principal
janela.title('App Teste')
janela.geometry('700x400')
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=True, height=True)
janela.iconify()    # Serve para impedir que a janela abra
janela.deiconify()  # Serve para reabrir a janela

janela.mainloop()
