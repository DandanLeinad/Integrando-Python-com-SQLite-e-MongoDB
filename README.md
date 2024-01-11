# Sistema de Gerenciamento de Banco de Dados - MongoDB & SQLAlchemy

## Descrição
Este projeto é um sistema de gerenciamento de banco de dados que integra o MongoDB e SQLAlchemy (SQLite) para realizar operações CRUD em duas diferentes bases de dados. O sistema é capaz de gerenciar informações de clientes e suas contas bancárias, oferecendo uma interface unificada para consultas e manipulação de dados.

## Características
- Integração com MongoDB para gerenciamento de documentos.
- Uso do SQLAlchemy para operações em um banco de dados relacional (SQLite).
- Consulta e manipulação de dados de clientes e contas bancárias.
- Remoção de duplicatas no MongoDB.

## Instalação e Configuração

### Pré-Requisitos
- Python 3.x
- Pip (gerenciador de pacotes Python)
- Acesso a um cluster MongoDB (ex.: MongoDB Atlas)

### Instalação
1. Clone o repositório para a sua máquina local:
git clone https://github.com/DandanLeinad/Integrando-Python-com-SQLite-e-MongoDB
2. Navegue até o diretório do projeto e instale as dependências:
cd [nome do diretório]
pip install -r requirements.txt

### Configuração
1. Crie um arquivo `.env` no diretório raiz do projeto.
2. Adicione a seguinte linha ao arquivo `.env`, substituindo `[Sua URL do MongoDB]` pela URL de conexão ao seu cluster MongoDB:
MONGO_URL="[Sua URL do MongoDB]"

## Uso
Execute o arquivo `main.py` para iniciar o sistema:
python main.pyO sistema realizará consultas nas bases de dados MongoDB e SQLAlchemy e exibirá os resultados.

## Estrutura do Projeto
- `Mongodb/`
  - `pymongo_setup.py`: Configuração e setup do cliente MongoDB.
- `SQL_Alchemy/`
  - `sqlalchemy_setup.py`: Configuração do SQLAlchemy (SQLite).
  - `models.py`: Modelos de dados SQLAlchemy.
- `main.py`: Script principal que executa as operações do sistema.
- `.env`: Arquivo de configuração para variáveis de ambiente.
- `requirements.txt`: Lista de dependências do projeto.

## Contribuição
Contribuições, problemas e solicitações de pull são bem-vindas. Para grandes alterações, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)# Integrando-Python-com-SQLite-e-MongoDB
