from flask import Flask
from controllers.app_controller import controller

app = Flask(__name__)

# Registrar el blueprint con las rutas
app.register_blueprint(controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
