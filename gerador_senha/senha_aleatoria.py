import secrets
import string

def senha_simples(qauntidade_caractere):
    if qauntidade_caractere < 4:
        raise ValueError("Digite uma quantidade maior ou igual a 4")

    numeros = string.digits

    senha = ''.join(secrets.choice(numeros) for _ in range(qauntidade_caractere))
    print('Sua senha:', senha)
    return senha

def numero_letra(qauntidade_caractere):
    if qauntidade_caractere < 4:
        raise ValueError("Digite uma quantidade maior ou igual a 4")

    caracteres = string.digits + string.ascii_letters

    senha = ''.join(secrets.choice(caracteres) for _ in range(qauntidade_caractere))
    print('Sua senha: ', senha)
    return senha


def misto(quantidade_caractere):
    if quantidade_caractere < 4:
        raise ValueError("Digite uma quantidade maior ou igual a 4")

    caractere = string.digits + string.ascii_letters + string.punctuation
    senha = ''.join(secrets.choice(caractere) for _ in range(quantidade_caractere))
    print('Sua senha: ', senha)
    return senha
