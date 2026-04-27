# tests/test_gerador.py
from gerador_senha import senha_aleatoria

def test_geracao_senha():
    senha = senha_aleatoria.senha_simples(10)
    assert len(senha) == 10
    assert isinstance(senha, str)

#
# def test_criacao_hash():
#     # Supondo que sua função receba um texto e retorne o hash
#     resultado = cria_hash("senha123")
#     assert resultado is not None
#     assert len(resultado) > 0

test_geracao_senha()