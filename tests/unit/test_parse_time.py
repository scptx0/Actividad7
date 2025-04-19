import pytest
from features.steps.steps import step_when_wait_time_description, convertir_palabra_a_numero
from src.belly import Belly

# Simular el argumento context de la función step_when_wait_time_description
class Context:
    def __init__(self):
        self.belly = Belly()

# Prueba para convertir la descripción de tiempo en horas
class TestParseTimeToNumber:
    def test_parse_one_and_half_hour (self):
        time_description = "una hora y media"
        expected_hours = 1.5
        context = Context()

        step_when_wait_time_description(context, time_description)

        assert context.belly.tiempo_esperado == expected_hours, f"Se esperaba {expected_hours} horas, pero se obtuvo {context.belly.tiempo_esperado} horas."

    def test_parse_half_hour(self):
        time_description = "media hora"
        expected_hours = 0.5
        context = Context()

        step_when_wait_time_description(context, time_description)

        assert context.belly.tiempo_esperado == expected_hours, f"Se esperaba {expected_hours} horas, pero se obtuvo {context.belly.tiempo_esperado} horas."

    def test_parse_two_hours__five_minutes_one_second(self):
        time_description = "dos horas 5 minutos un segundo"
        expected_hours = 2 + (5 / 60) + (1 / 3600)
        context = Context()

        step_when_wait_time_description(context, time_description)

        assert context.belly.tiempo_esperado == expected_hours, f"Se esperaba {expected_hours} horas, pero se obtuvo {context.belly.tiempo_esperado} horas."

    def test_parse_just_seconds(self):
        time_description = "50 segundos"
        expected_hours = 50 / 3600
        context = Context()

        step_when_wait_time_description(context, time_description)

        assert context.belly.tiempo_esperado == expected_hours, f"Se esperaba {expected_hours} horas, pero se obtuvo {context.belly.tiempo_esperado} horas."

    def test_incorrect_parsing(self):
        time_description = "hola"
        context = Context()

        try:
            step_when_wait_time_description(context, time_description)
        except ValueError:
            raise AssertionError(f"Se esperaba un error al analizar '{time_description}', pero no se produjo.")

