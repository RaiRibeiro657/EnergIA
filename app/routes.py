from flask import request, jsonify
from .energy import EnergyManager

energy_manager = EnergyManager()

def configure_routes(app):
    @app.route('/status', methods=['GET'])
    def get_status():
        status = energy_manager.get_status()
        return jsonify(status)

    @app.route('/update', methods=['POST'])
    def update_loads():
        data = request.get_json()
        carga_critica = data.get('carga_critica', None)
        carga_secundaria = data.get('carga_secundaria', None)

        energy_manager.update_loads(carga_critica, carga_secundaria)
        status = energy_manager.get_status()
        return jsonify(status)