import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/diagnostico', methods=['GET'])
def diagnostico_rede():
    # O usuário passa um IP ou domínio para testar a conexão
    ip_alvo = request.args.get('ip')
    
    if not ip_alvo:
        return jsonify({"erro": "O parâmetro 'ip' é obrigatório"}), 400

    # FALHA CRÍTICA: O código usa concatenação de string direta dentro de um comando de sistema (os.system / os.popen)
    # Se o usuário mandar: "8.8.8.8; cat /etc/passwd" ou "8.8.8.8 && rm -rf /", o servidor executa!
    comando = f"ping -c 1 {ip_alvo}"
    
    # Executa o comando de forma insegura no shell do servidor
    resultado = os.popen(comando).read()
    
    return jsonify({
        "status": "Executado",
        "saida": resultado
    })

if __name__ == '__main__':
    app.run(port=5000)
