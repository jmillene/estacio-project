from flask import jsonify, request
from service.uptade_product import update_product

def update_product_endpoint(product_id):
    # Pegando os dados do corpo da requisição
    data = request.get_json()

    # Pegando cada campo individualmente
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock_quantity = data.get('stock_quantity')

    # Chama a função do controlador e passa os parâmetros
    result = update_product(product_id, name, description, price, stock_quantity)

    # Retorna o resultado
    return jsonify(result)