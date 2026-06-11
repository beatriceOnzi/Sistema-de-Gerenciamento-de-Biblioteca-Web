# **Sistema Biblioteca Web**

Sistema desenvolvido para auxiliar no gerenciamento de bibliotecas escolares, permitindo o cadastro e controle de alunos, livros, turmas e empréstimos. Direcionado para o gerenciamento da biblioteca da Escola CNEC São Vicente e desenvolvido pensando nos requisitos da escola, porém que pode ser adaptado a outras bibliotecas em ambiente escolar, especialmente para o ensino fundamental, tendo em vista sua organização por turmas e semanas.

## Página da Seleção da Turma

<img width="959" height="440" alt="Captura de tela 2026-05-07 110334" src="https://github.com/user-attachments/assets/8524be85-889e-41e3-8113-5aab18ebbb3b" />

---

## Requisitos

- Python 3.10 ou superior
- Node.js 18 ou superior
- NPM

---

## Tecnologias Utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Tailwind CSS
- JavaScript
- Pytest

---

## Estrutura do Projeto

```
bibliotecaApi/
│
├── models/              # Modelos do banco de dados
├── routes/              # Rotas
├── services/            # Regras de negócio
├── templates/           # Páginas HTML
├── static/              # CSS, JavaScript e imagens
├── tests/               # Testes
│
├── app.py               # Inicialização da aplicação
├── config.py            # Configurações gerais
├── requirements.txt     # Dependências Python
├── package.json         # Dependências frontend
└── README.md
```

---

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Acesse a pasta do projeto:

```bash
cd bibliotecaApi
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

Windows:

```bash
venv\\Scripts\\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
npm install
```

---

## Executando o Projeto

Iniciar o servidor:

```bash
npm start
```

A aplicação estará disponível em:

```
<http://localhost:5000>
```

---

## Compilação do Tailwind CSS

Para atualizar os estilos durante o desenvolvimento:

```bash
npm run watch
```

---

## Testes

Para executar os testes automatizados:

```bash
pytest
```

---

## Funcionalidades

- Cadastro de alunos
- Cadastro de livros
- Registro de empréstimos
- Registro de devoluções
- Controle de livros emprestados
- Histórico de empréstimos
- Organização por turmas
- Interface web responsiva
- Testes automatizados

---

## Arquitetura

O projeto segue uma arquitetura em camadas:

- **Models:** representação das entidades do banco de dados.
- **Routes:** recebimento das requisições da aplicação.
- **Services:** regras de negócio e processamento dos dados.
- **Templates:** interface visual do sistema.
- **Database:** persistência utilizando SQLite e SQLAlchemy.
