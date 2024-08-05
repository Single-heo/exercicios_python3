"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""



"""
Não tente entender via códigos, leia os comentários de cima para baixo, fica MUITO mais 
simples de enteder o que esse treco faz
"""

script1 = input("Quer ver o 1º script? (yes or not): ") # Ver 1º script sim ou não?
if not script1:  # Se o usuário não digitou nada
    print("Digite uma das 2 opções!")
elif script1 == "yes":  # Se o usuário digitou "yes"
    try:
        numero = input("Digite um número: ")  # Pede para digitar um número
        numero = int(numero)  # Converte o input para inteiro
        PAR = numero % 2  # Testa se o número é par
        if PAR == 0:  # Se o resto da divisão por 2 é 0, é par
            print(f"{numero} é par!")
        else:  # Caso contrário, é ímpar
            print(f"{numero} é ímpar!")
    except ValueError:  # Captura erro de conversão de tipo
        print("Isso não é um número")
elif script1 == "not":  # Se o usuário digitou "not"
    print("Ok, vai embora 😡!")
else:  # Se o usuário digitou algo diferente de "yes" ou "not"
    print("Digite uma das 2 opções 😡!")
