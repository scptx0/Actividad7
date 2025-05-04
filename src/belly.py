from src.clock import get_current_time
from datetime import timedelta

class Belly:
    def __init__(self, clock_service=None):
        self.pepinos_comidos = 0
        self.clock_service = clock_service or get_current_time
        self.tiempo_inicio = self.clock_service()
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        if self.clock_service:
            tiempo_actual = self.clock_service() + timedelta(hours=self.tiempo_esperado)
            horas_pasadas = (tiempo_actual - self.tiempo_inicio).total_seconds() / 3600
            return horas_pasadas >= 1.5 and self.pepinos_comidos > 10.0
        
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10.0
        
