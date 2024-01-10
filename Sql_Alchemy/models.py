from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL

# Declarando a base para as classes de modelo
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "user_client"
    
    # Atributos do Cliente
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String, unique=True)
    endereco = Column(String, unique=True)

    # Relacionamento com a classe Conta (um cliente pode ter várias contas)
    contas = relationship("Conta", back_populates="cliente")

    # Representação textual
    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(Base):
    __tablename__ = "account"
    
    # Atributos da Conta
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_de_conta = Column(String)
    agencia = Column(String)
    numero = Column(Integer, unique=True)
    id_cliente = Column(Integer, ForeignKey("user_client.id"))
    saldo = Column(DECIMAL)

    # Relacionamento com a classe Cliente (uma conta é associada a um cliente)
    cliente = relationship("Cliente", back_populates="contas")

    # Representação textual
    def __repr__(self):
        return f"Conta(id={self.id}, tipo_de_conta={self.tipo_de_conta}, agencia={self.agencia}, numero={self.numero}, saldo={self.saldo})"