
from gerador_senha import senha_aleatoria
from gerador_senha import gerador_hash

def test_geracao_senha():
    senha = senha_aleatoria.senha_simples(10)
    assert len(senha) == 10
    assert isinstance(senha, str)

#
def test_criacao_hash():
    resultado = gerador_hash.cria_hash("senha123")
    assert resultado is not None
    assert len(resultado) > 0

test_geracao_senha()