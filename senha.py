senha = input("Digite sua senha:")

if len(senha) >= 8 and c.isupper() in senha:
    print("Senha válida")
else:
    print("DIGITE UMA SENHA VALIDA")

"""
Ideia do projeto 

Desafio: Validador de Senhas Fortes
Crie um programa em Python que valide se uma senha é forte o suficiente. Uma senha será considerada forte se:

Tiver pelo menos 8 caracteres. ok

Conter pelo menos uma letra maiúscula. ok

Conter pelo menos uma letra minúscula. ok

Conter pelo menos um número.

Conter pelo menos um caractere especial (ex: !@#$%^&*()-+).
"""
