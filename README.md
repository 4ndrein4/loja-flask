# Loja Flask - Versão Estilizada

Projeto Flask com SQLite que implementa CRUD para **Produto** e **Categoria**, já estilizado com Bootstrap.

## Como executar

1. Abra o terminal na pasta do projeto
2. Crie e ative o venv:
   - `python -m venv venv`
   - Windows (Prompt): `venv\Scripts\activate.bat`
   - Windows (PowerShell): `venv\Scripts\Activate.ps1` (pode ser preciso alterar ExecutionPolicy)
   - Linux/Mac: `source venv/bin/activate`
3. Instale dependências:
   - `pip install -r requirements.txt`
4. Rode a aplicação:
   - `python app.py`
5. Acesse:
   - `http://127.0.0.1:5000`

## O que foi melhorado

- Layout responsivo com Bootstrap
- Navbar, botões e tabelas estilizadas
- Flash messages para feedback do usuário
- Prevenção de exclusão de categorias com produtos vinculados

## Estrutura
```
loja_flask_stylish/
├── app.py
├── database.py
├── models.py
├── repositories/
├── services/
├── templates/
├── static/
└── requirements.txt
```

