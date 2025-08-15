from repositories.categoria_repository import CategoriaRepository

class CategoriaService:
    def __init__(self):
        self.repo = CategoriaRepository()

    def criar_categoria(self, categoria):
        self.repo.add(categoria)

    def listar_categorias(self):
        return self.repo.get_all()

    def buscar_categoria(self, id):
        return self.repo.get_by_id(id)

    def atualizar_categoria(self):
        self.repo.update()

    def deletar_categoria(self, categoria):
        self.repo.delete(categoria)
