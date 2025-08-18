def cadastrar(lista, item):
    if item in lista:
        print(f"⚠ O item '{item}' já está cadastrado!")
    else:
        lista.append(item)
        print("✔ Item cadastrado!")



    



"""def remover(lista, numero):
    if item in lista:
        lista.remove(item)
        print("✔ Item removido!")
    else:
        print(f"⚠ Item '{item}' não encontrado na lista.")"""
        
def remover(lista, numero):
             indice = numero - 1  # ajustar para índice correto
             if 0 <= indice < len(lista):
              removido = lista.pop(indice)
         
              print(f"❌ Item '{removido}' removido!")
             else:
              print("⚠ Número inválido.")



def listar(lista):
    if not lista:
        print("Lista vazia.")
    else:
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
