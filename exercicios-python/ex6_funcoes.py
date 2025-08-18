"""def saudacao(nome):
    
 return f"Olá, {nome}!"

usuario = input("Digite seu nome: ")

print(saudacao(usuario))"""

"""def idade_para_100(idade):
    return

idade = input("Digite sua idade: ")
restante = 100 - int(idade)


print ("Faltam",restante,"anos para 100.")"""


def idade_para_100(idade):
    """Calcula quantos anos faltam para a pessoa chegar aos 100"""
    return 100 - idade

idade = int(input("Digite sua idade: "))   # conversão direto para int
restante = idade_para_100(idade)           # chamamos a função

print(f"Faltam {restante} anos para 100.")
