from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import Session

# Minhas importaçôes
from models import Base, Cliente, Conta


# Configurando o Banco de dados
engine = create_engine("sqlite://")  # Criando um motor de banco de dados que se conecta ao SQLite
Base.metadata.create_all(engine)  # Criando as tabelas no banco de dados com base nas classes


# Verificar se a tabela "user_client" e "account" existe no banco de dados.
inspector_engine = inspect(engine)  # Criando uma instância de um objeto Inspector para o banco de dados
print(f"\nTabela 'user_client' existe: {inspector_engine.has_table('user_client')}")
print(f"Tabela 'account' existe: {inspector_engine.has_table('account')}")
print(f"Nomes das tabelas: {inspector_engine.get_table_names()}\n") # Exibindo os nomes das tabelas


# Criando uma sessão para interagir com o banco de dados
with Session(engine) as session:
    # Criando instâncias de clientes
    daniel = Cliente(nome="Daniel Pereira", cpf="12345678900", endereco="Rua A, 123")
    sofia = Cliente(nome="Sofia Martins", cpf="00987654321", endereco="Rua B, 456")
    gabriel = Cliente(nome="Gabriel Almeida", cpf="11223344550", endereco="Rua C, 789")

    # Adicionando os clientes à sessão e efetuando o commit das alterações
    session.add_all([daniel, sofia, gabriel])
    session.commit()

    # Criando instâncias de contas associadas aos clientes
    daniel.contas = [
        Conta(tipo_de_conta="Corrente", agencia="001", numero=48392, saldo=1000.00),
        Conta(tipo_de_conta="Poupança", agencia="001", numero=49321, saldo=5000.00)
    ]

    sofia.contas = [Conta(tipo_de_conta="Corrente", agencia="002", numero=57621, saldo=2000.00)]
    gabriel.contas = [Conta(tipo_de_conta="Corrente", agencia="003", numero=63947, saldo=1500.00)]

    # Adicionando as contas à sessão e efetuando o commit das alterações
    session.add_all([daniel, sofia, gabriel])
    session.commit()
