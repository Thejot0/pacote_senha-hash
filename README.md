# 🚀 senha-hash

    Gerador de senha hash/gerador de senha aleatoria com tamanho e complexibilidade com base na escolha do usuário

### 📋 Sobre o Projeto

Gerador de senha:

- Gerador de senha simples onde gera apenas senha com numeros
- Gerador de senha com letra e número onde
- Gerador de senha com número, letras[A/a] e caracteres

Gerador de senha hash

- Gera um hash de acorco com a senha passada dentro da função

###  🛠️ Tecnologias Utilizadas

    Python 3.12.3
    Bcrypt
    string
    secrets

### ⚙️ Como Instalar

Siga os passos abaixo para configurar o ambiente localmente:

    Clone o repositório:
    Bash

    git clone https://github.com/Thejot0/pacote_senha-hash.git

    Crie e ative o ambiente virtual:
    Bash

    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python -m venv venv
    source venv/bin/activate

    Instale o pacote (e suas dependências):

      pip install gerador_senha
    
    Pacote criado em .toml por tanto, é possivel baixar em modo editável:

      pip install -e .

### 🚀 Como Usar


from gerador_senha import gerador_hash, senha_aleatoria
### Exemplo de uso
resultado = senha_aleatoria.senha_simples(tamanho_caractere = 10)


senha = 'exemplo_senha'

hash = gerador_hash.cria_hash(senha)

### 📂 Estrutura do Repositório
Plaintext

    .
    ├── gerador_senha
    │   ├── gerador_hash.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── gerador_hash.cpython-312.pyc
    │   │   ├── __init__.cpython-312.pyc
    │   │   └── senha_aleatoria.cpython-312.pyc
    │   └── senha_aleatoria.py
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    └── tests
        ├── __pycache__
        │   └── test_gerador.cpython-312-pytest-7.4.4.pyc
        └── test_gerador.py

## ✒️ Autor
###  [GitHub](https://github.com/Thejot0)
