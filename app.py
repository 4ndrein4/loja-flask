from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
from models import Produto, Categoria
from services.produto_service import ProdutoService
from services.categoria_service import CategoriaService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key'
db.init_app(app)

produto_service = ProdutoService()
categoria_service = CategoriaService()

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('listar_produtos'))

@app.route('/categorias')
def listar_categorias():
    categorias = categoria_service.listar_categorias()
    return render_template('categoria_list.html', categorias=categorias)

@app.route('/categorias/criar', methods=['GET', 'POST'])
def criar_categoria():
    if request.method == 'POST':
        nome = request.form.get('nome','').strip()
        descricao = request.form.get('descricao','').strip()
        if not nome:
            flash('Nome é obrigatório','danger')
            return redirect(url_for('criar_categoria'))
        categoria = Categoria(nome=nome, descricao=descricao)
        categoria_service.criar_categoria(categoria)
        flash('Categoria criada com sucesso','success')
        return redirect(url_for('listar_categorias'))
    return render_template('categoria_form.html')

@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = categoria_service.buscar_categoria(id)
    if not categoria:
        flash('Categoria não encontrada','warning')
        return redirect(url_for('listar_categorias'))
    if request.method == 'POST':
        categoria.nome = request.form.get('nome','').strip()
        categoria.descricao = request.form.get('descricao','').strip()
        categoria_service.atualizar_categoria()
        flash('Categoria atualizada','success')
        return redirect(url_for('listar_categorias'))
    return render_template('categoria_form.html', categoria=categoria)

@app.route('/categorias/deletar/<int:id>', methods=['POST'])
def deletar_categoria(id):
    categoria = categoria_service.buscar_categoria(id)
    if not categoria:
        flash('Categoria não encontrada','warning')
    else:
        if categoria.produtos:
            flash('Não é possível deletar categoria com produtos vinculados','danger')
        else:
            categoria_service.deletar_categoria(categoria)
            flash('Categoria deletada','success')
    return redirect(url_for('listar_categorias'))

@app.route('/produtos')
def listar_produtos():
    produtos = produto_service.listar_produtos()
    return render_template('produto_list.html', produtos=produtos)

@app.route('/produtos/criar', methods=['GET', 'POST'])
def criar_produto():
    categorias = categoria_service.listar_categorias()
    if request.method == 'POST':
        nome = request.form.get('nome','').strip()
        preco = request.form.get('preco','0').replace(',','.')
        estoque = request.form.get('estoque','0')
        categoria_id = request.form.get('categoria_id')
        if not nome or not preco or not estoque or not categoria_id:
            flash('Preencha todos os campos','danger')
            return redirect(url_for('criar_produto'))
        try:
            preco_val = float(preco)
            estoque_val = int(estoque)
        except ValueError:
            flash('Preço ou estoque inválido','danger')
            return redirect(url_for('criar_produto'))
        produto = Produto(nome=nome, preco=preco_val, estoque=estoque_val, categoria_id=int(categoria_id))
        produto_service.criar_produto(produto)
        flash('Produto criado com sucesso','success')
        return redirect(url_for('listar_produtos'))
    return render_template('produto_form.html', categorias=categorias)

@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = produto_service.buscar_produto(id)
    categorias = categoria_service.listar_categorias()
    if not produto:
        flash('Produto não encontrado','warning')
        return redirect(url_for('listar_produtos'))
    if request.method == 'POST':
        produto.nome = request.form.get('nome','').strip()
        preco = request.form.get('preco','0').replace(',','.')
        produto.estoque = int(request.form.get('estoque','0'))
        produto.preco = float(preco)
        produto.categoria_id = int(request.form.get('categoria_id'))
        produto_service.atualizar_produto()
        flash('Produto atualizado','success')
        return redirect(url_for('listar_produtos'))
    return render_template('produto_form.html', produto=produto, categorias=categorias)

@app.route('/produtos/deletar/<int:id>', methods=['POST'])
def deletar_produto(id):
    produto = produto_service.buscar_produto(id)
    if produto:
        produto_service.deletar_produto(produto)
        flash('Produto deletado','success')
    else:
        flash('Produto não encontrado','warning')
    return redirect(url_for('listar_produtos'))

if __name__ == '__main__':
    app.run(debug=True)
