usuario_correto = "admin"
senha_correta = "python123"
tentativas = 0
def verificarAutenticacao(usuario,senha):

 resultado = usuario == usuario_correto and senha == senha_correta
 return resultado

while tentativas < 3:
    usuario = input("digite seu login: ")
    senha = input("digite sua senha: ")


    if verificarAutenticacao(usuario,senha):
        print("Acesso autorizado!")
        break
    else:
        tentativas += 1
        tentativas_restantes = 3 - tentativas
        if usuario != usuario_correto: print("Login incorreto!") 
        
        else: print("Senha incorreta!")
    if tentativas_restantes > 1:
        print("Restam", tentativas_restantes, "tentativas.")
        
    elif tentativas_restantes == 1:
        print("ultima tentativa")
        

    if tentativas == 3:
     print("acesso bloqueado")
