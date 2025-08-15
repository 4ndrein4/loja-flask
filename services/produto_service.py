from repositories.produto_repository import ProdutoRepository

class ProdutoService:
    def __init__(self):
        self.repo = ProdutoRepository()

    def criar_produto(self, produto):
        self.repo.add(produto)

    def listar_produtos(self):
        return self.repo.get_all()

    def buscar_produto(self, id):
        return self.repo.get_by_id(id)

    def atualizar_produto(self):
        self.repo.update()

    def deletar_produto(self, produto):
        self.repo.delete(produto)
