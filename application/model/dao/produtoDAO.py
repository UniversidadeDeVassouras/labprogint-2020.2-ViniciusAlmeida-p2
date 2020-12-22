import json
from application.model.entity.Produtos import Produto

with open ('application\\products.json') as product_file:
        product_list = json.load(product_file)

class produtoDAO:
    def __init__(self):
        self._listar_produtos = []

        for produtos in product_list:
             self._listar_produtos.append(Produto(produtos['id'], produtos['image'], produtos['name'], produtos['description'], produtos['oldPrice'], produtos['price'], produtos['installments']['count'], produtos['installments']['value']))

    def get_listar_produtos(self):
        return self._listar_produtos



