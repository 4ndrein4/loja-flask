from models import Produto
from database import db

class ProdutoRepository:
    def add(self, produto):
        db.session.add(produto)
        db.session.commit()

    def get_all(self):
        return Produto.query.order_by(Produto.nome).all()

    def get_by_id(self, id):
        return Produto.query.get(id)

    def update(self):
        db.session.commit()

    def delete(self, produto):
        db.session.delete(produto)
        db.session.commit()
