from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def main():
    resultado = None
    media = None

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)

        media = (primeira + segunda) / 2
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media,
                                         resultado=resultado)
# def index():
#     return render_template('index.html')
#
# @app.route('/eli')
# def eli():
#     return 'oi, aqui é a eli'

if __name__ == '__main__':
    app.run(debug=True)
