idade = int(input("Qual a sua idade? "))
cidade = (input("Qual a sua cidade? "))

if idade >= 60:
    print("Você é idoso. Sua cidade é ",cidade)
  
elif idade >= 18:
  print("Você é adulto. Sua cidade é",cidade)
  
else:
  print("Você é menor de idade. Sua cidade é", cidade)