import os
import json
import urllib.parse
from flask import Flask, render_template, request

app = Flask(__name__)
NUMERO_WHATSAPP = "5592999999999"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # pega caminho da pasta api/

def carregar_produtos():
    caminho = os.path.join(BASE_DIR, '..', '/products.json')  # volta um nível
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
