#Simule login (usuário = admin, senha = 1234)

usuário = "admin"
senha = "1234"

usuário = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuário == "admin" and senha == "1234":
    print("Login realizado com sucesso! Bem vindo, admin!")
else:   
    print("Login falhou! Usuário ou senha incorretos.") 