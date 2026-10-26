senha_correta="python123"
tentativas = 0

while tentativas < 3:
    senha = input("text your password: ")
    

    if (senha) == (senha_correta):
        print("Acesso autorizado!")
        break
    else: 
        tentativas += 1
        tentativas_restantes = 3 - tentativas 
        print("senha incorreta")
    if tentativas_restantes > 1:
         print("Restam", tentativas_restantes, "tentativas.")
    elif tentativas_restantes == 1:
         print("ultima tentativa")  

if tentativas == 3:
        print("acesso bloqueado")