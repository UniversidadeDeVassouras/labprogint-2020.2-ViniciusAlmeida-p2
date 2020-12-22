class Produto:
    def __init__ (self, id, imagem_produto, nome_produto, descricao_produto, preco_antigo, preco_novo, qtd_parcela_produto, valor_parcela_produto):
        self._id = id
        self._imagem_produto = imagem_produto
        self._nome_produto = nome_produto
        self._descricao_produto = descricao_produto
        self._preco_antigo = preco_antigo
        self._preco_novo = preco_novo
        self._qtd_parcela_produto = qtd_parcela_produto
        self._valor_parcela_produto = valor_parcela_produto

    
    def get_id (self):
        return self._id

    def get_imagem_produto (self):
        return self._imagem_produto
    
    def get_nome_produto (self):
        return self._nome_produto

    def get_descricao_produto (self):
        return self._descricao_produto

    def get_preco_antigo (self):
        return self._preco_antigo
    
    def get_preco_novo (self):
        return self._preco_novo
    
    def get_qtd_parcela_produto (self):
        return self._qtd_parcela_produto

    def get_valor_parcela_produto (self):
        return self._valor_parcela_produto