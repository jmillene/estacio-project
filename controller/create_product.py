from flask import jsonify, request
from service.create_product import create_product

def add_product():
    try:
        # Obtendo os dados do JSON
        data = request.get_json()

        # Extraindo os campos necessários
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        stock_quantity = data.get('stock_quantity')

        # Verificando se todos os campos obrigatórios foram fornecidos
        if not name or not price or not stock_quantity or not description:
            return jsonify({"message": "Todos os campos são obrigatórios."}), 400

        # Tentando criar o produto
        create_product(name, description, price, stock_quantity)
        return jsonify({"message": "Produto criado com sucesso!"}), 201

    except KeyError as e:
        # Erro ao acessar uma chave que não existe no JSON
        return jsonify({"message": f"Erro de chave: {str(e)}"}), 400

    except Exception as e:
        # Tratamento genérico para outras exceções
        return jsonify({"message": f"Erro interno do servidor: {str(e)}"}), 500
