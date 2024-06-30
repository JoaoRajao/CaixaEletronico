from flask import Blueprint, request, jsonify
from models.Caixa import CAIXA
from models.Excecoes import  ErroEntradaInvalida, ErroCedulasIndisponiveis

rota_caixa = Blueprint('caixa', __name__)

@rota_caixa.route('/api/saque', methods=['POST'])
def realizar_saque():
    """
    Endpoint para processar solicitações de saque via API. Recebe um valor de saque
    e retorna a distribuição de cédulas necessária ou um erro se o saque não for possível.

    Returns:
        Response: Uma resposta JSON contendo a distribuição de cédulas ou uma mensagem de erro.
    """
    dados = request.get_json()
    try:
        valor = dados.get('valor', 0)
        caixa = CAIXA()
        resultado = caixa.sacar(valor)
        return jsonify(resultado)
    except ErroEntradaInvalida as e:
        return jsonify({"error": str(e)}), 400
    except ErroCedulasIndisponiveis as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": "Erro interno do servidor"}), 500
