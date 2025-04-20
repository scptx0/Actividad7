import time
from features.steps.steps import step_when_wait_time_description
from src.belly import Belly

class Context:
    def __init__(self):
        self.belly = Belly()  # Simulando el objeto Belly
        self.error = None

def test_stress_wait_time_description():
    context = Context()
    start_time = time.time()
    iterations = int(1e5)  # Simular carga con 1000 iteraciones

    for i in range(iterations):
        time_description = "200 horas 300 minutos 17 segundos"
        step_when_wait_time_description(context, time_description)

    end_time = time.time()
    print(f"Pruebas de estrés realizada en {end_time - start_time:.2f} segundos")