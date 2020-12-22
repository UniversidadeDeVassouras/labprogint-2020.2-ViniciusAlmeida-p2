from application import app
from flask import render_template, request, current_app
import json
from application.model.entity.Produtos import Produto

@app.route("/")
def index():
    
    with open ('application\\products.json') as product_file:
        product_list = json.load(product_file)
        print(product_list)

    listar_produtos = []
    for produtos in product_list:
        listar_produtos.append(Produto(produtos['id'], produtos['image'], produtos['name'], produtos['description'], produtos['oldPrice'], produtos['price'], produtos['installments']['count'], produtos['installments']['value']))

    return render_template('index.html', listar_produtos = listar_produtos)
