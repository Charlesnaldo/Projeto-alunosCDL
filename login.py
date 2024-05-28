import customtkinter as ctk

# Configuração do tema e cores
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

# Função para efetuar o login (placeholder para adicionar lógica de login)
def login():
    print("Botão de login clicado")

#janela principal
root = ctk.CTk()
root.title("DevinTinder - Login")
root.geometry("400x300")

#título da aplicação
title_label = ctk.CTkLabel(master=root, text="DevinTinder", text_color="red", font=("Helvetica", 24, "bold"))
title_label.pack(pady=20)

#campo de entrada para o login
login_label = ctk.CTkLabel(master=root, text="Login", text_color="white")
login_label.pack(pady=5)
login_entry = ctk.CTkEntry(master=root, width=200)
login_entry.pack(pady=5)

#campo de entrada para a senha
senha_label = ctk.CTkLabel(master=root, text="Senha", text_color="white")
senha_label.pack(pady=5)
senha_entry = ctk.CTkEntry(master=root, width=200, show='*')
senha_entry.pack(pady=5)

#botão para efetuar o login
login_button = ctk.CTkButton(master=root, text="Login", command=login,text_color='red')
login_button.pack(pady=20)

#loop principal da interface gráfica
root.mainloop()
