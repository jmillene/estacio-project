from flask import jsonify, request
from service.update_order import update_order


def atualizar_ordem_por_id(order_id):
    dados = request.get_json()
    status = dados.get('status')
    
    if not status:
        return jsonify({"mensagem": "O status é obrigatório"}), 400
    
    resultado = update_order(order_id, status)
    if resultado:
        return jsonify({"mensagem": "Ordem atualizada com sucesso"}), 200
    else:
        return jsonify({"mensagem": "Ordem não encontrada"}), 404
