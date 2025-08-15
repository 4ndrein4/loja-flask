
# Loja Flask

Este projeto é um sistema de **loja virtual simples** desenvolvido em **Flask** com **SQLite**, implementando **CRUD completo** para duas entidades:

* **Produto** (nome, preço, estoque, categoria)
* **Categoria** (nome, descrição)

## Tecnologias utilizadas

* Python 3
* Flask
* SQLite
* Bootstrap 5 (frontend)
* HTML + CSS

## Funcionalidades

* **CRUD de Categorias**: criar, listar, editar e excluir.
* **CRUD de Produtos**: criar, listar, editar e excluir.
* Relacionamento **Produto → Categoria** no banco de dados.
* Organização do código em **repositories** (acesso a dados) e **services** (regras de negócio).

## Estrutura do projeto

```
loja_flask/
│-- app.py
│-- database.py
│-- models.py
│-- requirements.txt
│-- README.md
│-- repositories/
│   ├── produto_repository.py
│   └── categoria_repository.py
│-- services/
│   ├── produto_service.py
│   └── categoria_service.py
│-- templates/
│   ├── base.html
│   ├── produtos.html
│   ├── categorias.html
│   ├── form_produto.html
│   └── form_categoria.html
│-- static/
│   └── css/
│       └── style.css
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/loja-flask.git
cd loja
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
# Windows (Prompt):
venv\Scripts\activate.bat
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️. Executar o sistema

```bash
python app.py
```

Acesse no navegador: **(http://127.0.0.1:5000)**
