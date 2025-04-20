import time
from features.steps.steps import step_given_eaten_cukes
from src.belly import Belly

class Context:
    def __init__(self):
        self.belly = Belly()  # Simulando el objeto Belly
        self.error = None

def test_stress_wait_random_intervals():
    context = Context()
    start_time = time.time()
    iterations = int(1e5)  # Simular carga con 1000 iteraciones

    for i in range(iterations):
        cukes = "1000000"  # Simulando la cantidad de pepinos
        step_given_eaten_cukes(context, cukes)

    end_time = time.time()
    print(f"Pruebas de estrés realizada en {end_time - start_time:.2f} segundos")