"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ")

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except:
    print("Digite um numero inteiro!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite que horas são: ")

try:
    horaDividida = hora.split(":")

    if int(horaDividida[0]) < 12:
        print("Bom dia!")
    elif int(horaDividida[0]) < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
except:
    print("Digite uma hora!")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome:")

try:
    int(nome)
    print("Digite um nome válido!")
except:
    if len(nome) <= 4:
        print("Seu nome é curto.")
    elif len(nome) <= 6:
        print("Seu nome é normal.")
    elif len(nome) > 6:
        print("Seu nome é muito grande.")