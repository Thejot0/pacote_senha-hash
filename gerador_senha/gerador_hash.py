import bcrypt

def cria_hash(senha):
    senha_bytes = senha.encode('utf-8')

    hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt(12))
    print('Senha em hash: ', hash)
    return hash
