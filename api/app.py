import os
import json
import urllib.parse
from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # agora api/

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

NUMERO_WHATSAPP = "5592981934569"

def carregar_produtos():
    caminho = os.path.join(BASE_DIR, 'products.json')
    with open(caminho, 'r', encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def index():
    produtos = carregar_produtos()
    base_url = request.host_url.rstrip('/')

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

