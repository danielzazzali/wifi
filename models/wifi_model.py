import subprocess

def obtener_redes_wifi():
    try:
        resultado = subprocess.run(['nmcli', '-t', 'dev', 'wifi'], capture_output=True, text=True)
        print("Salida de nmcli:", resultado.stdout)  # Depuración
        if resultado.returncode == 0:
            return resultado.stdout if resultado.stdout else "No se encontraron redes WiFi."
        else:
            return "Error al obtener las redes WiFi."
    except Exception as e:
        return f"Error: {str(e)}"
