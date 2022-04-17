from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd

app = Flask(__name__)

#construir as funcionalidades
@app.route('/')
def main():
    return 'A API está no ar'

@app.route('/totvendas')
def totvendas():
    tabela = pd.read_csv('C:/Users/lilic/flsk-treino/vflsk-api/advertising.csv')
    total_vendas = round(tabela['Vendas'].sum(),3)
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)

#rodar a api
if __name__ == '__main__':
    app.run(debug=True)
