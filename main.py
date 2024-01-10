import sys
sys.path.append('Sql_Alchemy')  # Substitua pelo caminho correto

# Agora suas importações
from Mongodb.pymongo_setup import client
from Sql_Alchemy.models import Cliente
from Sql_Alchemy.sqlalchemy_setup import engine, Session, select

def main():
    # SQLite (SQLAlchemy)
    with Session(engine) as session:
        # Consulta todos os clientes e suas contas
        stmt = select(Cliente)
        for cliente in session.scalars(stmt):
            print(f"Cliente(id={cliente.id}, nome={cliente.nome}, cpf={cliente.cpf}, endereco={cliente.endereco})")
            for conta in cliente.contas:
                saldo_formatado = round(conta.saldo, 2)
                print(f"  - Conta(id={conta.id}, tipo_de_conta={conta.tipo_de_conta}, "
                      f"agencia={conta.agencia}, numero={conta.numero}, saldo={saldo_formatado})")
            print()

    # MongoDB (PyMongo)
    try:
        # Acesso à coleção "clientes"
        clientes = client["bank_db"]["clientes"]

        # Buscar todos os clientes
        todos_clientes = list(clientes.find())

        # Exibir informações de cada cliente e suas contas
        for cliente in todos_clientes:
            print("\nCliente:")
            print(f"  Nome: {cliente['nome']}")
            print(f"  CPF: {cliente['cpf']}")
            print(f"  Endereço: {cliente['endereco']}\n")
            for conta in cliente['contas']:
                print("  Conta:")
                print(f"    Tipo de Conta: {conta['tipo_de_conta']}")
                print(f"    Agência: {conta['agencia']}")
                print(f"    Número: {conta['numero']}")
                print(f"    Saldo: {conta['saldo']}\n")
            print("-" * 40)

    except Exception as e:
        print(f"Erro ao testar consultas MongoDB: {e}")

if __name__ == "__main__":
    main()
