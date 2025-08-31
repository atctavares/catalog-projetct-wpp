import json
import urllib.parse
from flask import Flask, render_template, request

app = Flask(__name__)
NUMERO_WHATSAPP = "5592999999999"  # seu número com DDI + DDD

def carregar_produtos():
    with open('products.json', 'r', encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def index():
    produtos = carregar_produtos()
    base_url = request.host_url.rstrip('/')  # pega URL base automaticamente

    for p in produtos:
        mensagem = f"""Olá! Tenho interesse neste produto:
📦 Nome: {p['nome']}
💲 Valor: R$ {p['valor']}
📌 Descrição: {p['descricao']}
📑 Detalhes: {p['detalhes']}
📏 Tamanho: {p['tamanho']}
🖼️ Imagem: {base_url}{p['imagem']}"""

        p["whatsapp_url"] = f"https://wa.me/{NUMERO_WHATSAPP}?text={urllib.parse.quote(mensagem)}"

    return render_template('index.html', produtos=produtos)

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    produtos = carregar_produtos()
    return json.dumps(produtos, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    app.run(debug=True)
