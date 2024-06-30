from flask import Flask
from controller.controllerCaixa import rota_caixa

app = Flask(__name__)
app.register_blueprint(rota_caixa)

if __name__ == '__main__':
    app.run(debug=True)
