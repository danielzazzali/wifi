from flask import Blueprint, render_template
from models.wifi_model import obtener_redes_wifi

# Crear un Blueprint para las rutas
controller = Blueprint('controller', __name__)

@controller.route('/')
def home():
    wifi_result = obtener_redes_wifi()
    if not wifi_result or wifi_result == "No se encontraron redes WiFi.":
        wifi_result = "No se encontraron redes WiFi o ocurrió un error."
    return render_template('index.html', wifi_result=wifi_result)

