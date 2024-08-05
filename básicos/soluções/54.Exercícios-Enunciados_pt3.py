"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu nome: ")
espaços = nome.count(' ') > 4
espaços2 = nome.count(' ') <= 4
if not nome:
  print("Rodo pa quê então?!😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡")
if espaços:
  print("OU seu nome é muito grande, ou você só digitou espaços FDP!")
if nome and espaços2:
  quantidade_de_espaços = nome.count(' ')
  if len(nome) <= 4 or len(nome) >= 5 and len(nome) <= 6:
    print(f"Seu nome possui {len(nome)} caracteres contando com {quantidade_de_espaços} espaços ")
    print(f"Seu nome possui {len(nome) - quantidade_de_espaços} caracteres sem espaços")
  else:
    print(f"Seu nome possui {len(nome)} caracteres contando com {quantidade_de_espaços} espaços ")
    print(f"Seu nome possui {len(nome) - quantidade_de_espaços} caracteres sem espaços")