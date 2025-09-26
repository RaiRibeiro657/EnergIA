class EnergyManager:
    def __init__(self):
        self.battery_level = 100
        self.carga_critica = True
        self.carga_secundaria = True

    def consumir_energia(self):
        consumo = 0
        if self.carga_critica:
            consumo += 5
        if self.carga_secundaria:
            consumo += 3
        self.battery_level = max(0, self.battery_level - consumo * 0.1)

    def get_status(self):
        return {
            'battery_level': round(self.battery_level, 2),
            'carga_critica': self.carga_critica,
            'carga_secundaria': self.carga_secundaria
        }

    def update_loads(self, carga_critica=None, carga_secundaria=None):
        if carga_critica is not None:
            self.carga_critica = carga_critica
        if carga_secundaria is not None:
            self.carga_secundaria = carga_secundaria
        self.consumir_energia()