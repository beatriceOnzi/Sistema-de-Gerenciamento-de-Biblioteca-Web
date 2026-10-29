
# Sistema Biblioteca Web | CNEC São Vicente

Sistema web desenvolvido para gerenciar a biblioteca da Escola CNEC São Vicente, com organização dos empréstimos por turma e por semana. O projeto reúne cadastro de alunos e livros, controle de devoluções e histórico de empréstimos em uma interface responsiva.

## Interface

<img width="959" height="440" alt="Tela de seleção de turma" src="https://github.com/user-attachments/assets/8524be85-889e-41e3-8113-5aab18ebbb3b" />

## Funcionalidades

- Cadastro e consulta de alunos e livros.
- Registro e edição de empréstimos.
- Avanço de semana independente por turma.
- Visualização dos empréstimos da semana atual e anterior.
- Identificação de devoluções pendentes.
- Histórico de empréstimos e devoluções.
- Avanço de ano escolar.
- Pesquisa com filtros e autocompletar de livros.

## Tecnologias

- **Backend:** Python, Flask, Flask-SQLAlchemy e Flask-Migrate.
- **Banco de dados:** PostgreSQL 16.
- **Frontend:** HTML, Jinja2, JavaScript, Tailwind CSS e PostCSS.
- **Testes:** Pytest, pytest-flask e pytest-cov.
- **Desenvolvimento:** Docker e Docker Compose.
- **Produção:** Waitress.

## Estrutura do Projeto

```text
bibliotecaApi/
├── src/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── tests/
├── migrations/
├── app.py
├── config.py
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── package.json
└── README.md
```

## Instalação e Execução

### Pré-requisitos

- Docker e Docker Compose.
- Node.js e npm (para compilação do CSS).

Clone o repositório:

```bash
git clone https://github.com/beatriceOnzi/Sistema_Biblioteca_Api.git
cd Sistema_Biblioteca_Api
```

Crie um arquivo `.env` na raiz do projeto:

```dotenv
POSTGRES_USER=biblioteca
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=biblioteca
DATABASE_URL=postgresql+psycopg2://biblioteca:sua_senha@db:5432/biblioteca
SECRET_KEY=sua_chave_secreta
```

Inicie os serviços:

```bash
docker compose up --build -d
```

Acesse a aplicação em:

`http://localhost:5000`

Para encerrar:

```bash
docker compose down
```

Os dados do PostgreSQL são armazenados no volume Docker `pgdata`.

## Desenvolvimento

Comandos disponíveis no `package.json`:

```bash
npm install
npm run dev       # Sincroniza alterações usando Docker Compose Watch
npm run watch     # Compila o CSS durante o desenvolvimento
npm run build     # Gera o CSS minificado
```

### Testes

Instale as dependências Python e execute os testes:

```bash
pip install -r requirements.txt
pytest
```

Os testes utilizam SQLite em memória, enquanto a aplicação principal utiliza PostgreSQL.

## Implantação na Escola

Na Escola CNEC São Vicente, a aplicação é executada localmente, sem Docker, utilizando PostgreSQL e Waitress como servidor WSGI.

Após configurar o ambiente Python, as dependências e o arquivo `.env`, o servidor é iniciado com:

```bash
waitress-serve --listen=127.0.0.1:5000 --call app:create_app
```

O Waitress executa a função `create_app()` definida em `app.py`, responsável pela inicialização do Flask, configuração do banco de dados e registro das rotas.

A aplicação fica disponível em `http://127.0.0.1:5000` no computador que executa o servidor.
