from application import app
from flask import render_template, request, current_app
import json
from application.model.entity.Produtos import Produto
from application.model.dao.produtoDAO import produtoDAO

@app.route("/")
def index():   

    listar_produtos = produtoDAO().get_listar_produtos()

    return render_template('index.html', listar_produtos = listar_produtos)
