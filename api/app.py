import json
from flask import Flask, render_template

app = Flask(__name__)

# Carregar produtos de um arquivo JSON
def carregar_produtos():
    with open('products.json', 'r') as f:
        return json.load(f)

# Rota para mostrar a página do catálogo
@app.route('/')
def index():
    produtos = carregar_produtos()
    return render_template('index.html', produtos=produtos)

# Rota para retornar os produtos via API
@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    produtos = carregar_produtos()
    return json.dumps(produtos)

if __name__ == '__main__':
    app.run(debug=True)
