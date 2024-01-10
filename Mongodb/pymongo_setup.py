from pymongo import MongoClient

import os
from dotenv import load_dotenv

load_dotenv()

# URL de conexão ao MongoDB
MONGO_URL = os.environ.get("MONGO_URL")

client = MongoClient(MONGO_URL)

# Criando bancos de dados "bank_db"
db = client["bank_db"]

# Criando a coleção "clientes"
clientes = db["clientes"]

# Documentos para a coleção "clientes"

# Documento para Daniel
daniel_docs = [
    {
        "nome": "Daniel Pereira",
        "cpf": "12345678900",
        "endereco": "Rua A, 123",
        "contas": [
            {
                "tipo_de_conta": "Corrente",
                "agencia": "001",
                "numero": 48392,
                "saldo": 1000.00
            },
            {
                "tipo_de_conta": "Poupança",
                "agencia": "001",
                "numero": 49321,
                "saldo": 5000.00
            }
        ]
    }
]

# Documento para Sofia
sofia_docs = [
    {
        "nome": "Sofia Martins",
        "cpf": "00987654321",
        "endereco": "Rua B, 456",
        "contas": [
            {
                "tipo_de_conta": "Corrente",
                "agencia": "002",
                "numero": 57621,
                "saldo": 2000.00
            }
        ]
    }
]

# Documento para Gabriel
gabriel_docs = [
    {
        "nome": "Gabriel Almeida",
        "cpf": "11223344556",
        "endereco": "Rua C, 789",
        "contas": [
            {
                "tipo_de_conta": "Corrente",
                "agencia": "003",
                "numero": 63947,
                "saldo": 1500.00
            }
        ]
    }
]

# Inserindo documentos na coleção "clientes"
clientes.insert_many(daniel_docs)
clientes.insert_many(sofia_docs)
clientes.insert_many(gabriel_docs)
