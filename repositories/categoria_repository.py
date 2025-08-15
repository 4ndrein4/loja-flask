from models import Categoria
from database import db

class CategoriaRepository:
    def add(self, categoria):
        db.session.add(categoria)
        db.session.commit()

    def get_all(self):
        return Categoria.query.order_by(Categoria.nome).all()

    def get_by_id(self, id):
        return Categoria.query.get(id)

    def update(self):
        db.session.commit()

    def delete(self, categoria):
        db.session.delete(categoria)
        db.session.commit()
