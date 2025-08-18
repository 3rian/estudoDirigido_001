"""senha_correta = "python123"

tentativa = ""

while tentativa != senha_correta:
    
 tentativa = input("Digite a senha: ")

print("Acesso liberado!")"""

senha_correta = "python123"
tentativas = 0
limite = 3

while tentativas < limite:
    tentativa = input("Digite a senha: ")
    if tentativa == senha_correta:
        print("Acesso liberado!")
        break
    else:
        print("Senha incorreta.")
        tentativas = tentativas +1

if tentativas == limite:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")
