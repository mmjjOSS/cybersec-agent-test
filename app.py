from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados simulado da empresa
# Contém dados confidenciais de faturas de clientes diferentes
BANCO_DE_DADOS_FATURAS = {
    "1001": {"cliente_id": "user_joao", "valor": 150.00, "status": "Pago", "detalhes": "Serviço de Nuvem AWS"},
    "1002": {"cliente_id": "user_joao", "valor": 350.00, "status": "Pendente", "detalhes": "Licença Adobe Creative Cloud"},
    "1003": {"cliente_id": "user_maria", "valor": 12000.00, "status": "Pago", "detalhes": "Consultoria de TI Confidencial"},
    "1004": {"cliente_id": "user_empresa_concorrente", "valor": 85000.00, "status": "Pago", "detalhes": "Aquisição de Patente"}
}

@app.route('/api/faturas/<fatura_id>', methods=['GET'])
def obter_fatura(fatura_id):
    # Simula o ID do usuário que está logado na sessão (ex: João está logado)
    # Em um sistema real, isso viria de um Token JWT ou cookie de sessão seguro
    usuario_logado_id = request.headers.get('X-User-Id', 'user_joao')

    # Busca a fatura no banco de dados
    fatura = BANCO_DE_DADOS_FATURAS.get(fatura_id)
    
    if not fatura:
        return jsonify({"erro": "Fatura não encontrada"}), 404

    # FALHA CRÍTICA (IDOR/BOLA): O código apenas verifica se a fatura existe.
    # Ele NUNCA valida se o 'usuario_logado_id' é o dono legítimo da fatura.
    # Se o João (user_joao) requisitar a fatura '1003' ou '1004', ele verá dados confidenciais da Maria ou da Concorrente!
    return jsonify(fatura), 200

if __name__ == '__main__':
    app.run(port=5000)
