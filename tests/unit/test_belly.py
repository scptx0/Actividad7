import pytest
from features.steps.steps import step_given_eaten_cukes
from src.belly import Belly
from unittest.mock import Mock
from datetime import datetime, timedelta

class Context:
    def __init__(self):
        self.error = None
        self.belly = Belly()

class TestBellyWithMockTime:
    def test_belly_gruñe_con_pepinos_y_tiempo(self):
        tiempo_base = datetime(2025, 5, 4, 12, 0, 0)
        mock_clock = Mock()
        mock_clock.return_value = tiempo_base
        
        belly = Belly(clock_service=mock_clock)
        
        belly.comer(12)
        
        mock_clock.return_value = tiempo_base + timedelta(hours=1.5)
        
        assert belly.esta_gruñendo() is True

class TestCukeAmount:
    # Test para una cantidad entera positiva de pepinos
    def test_cuke_positive_int_amount(self): 
        cukes = "5"
        context = Context()

        step_given_eaten_cukes(context, cukes)

        assert context.belly.pepinos_comidos == 5.0, f"Se esperaba 5 pepinos, pero se obtuvo: {context.belly.pepinos_comidos: d}"

    # Test para una cantidad decimal positiva de pepinos
    def test_cuke_positive_float_amount(self):
        cukes = "5.5"
        context = Context()

        step_given_eaten_cukes(context, cukes)

        assert context.belly.pepinos_comidos == 5.5, f"Se esperaba 5.5 pepinos, pero se obtuvo: {context.belly.pepinos_comidos: f}"

    # Test para una cantidad entera negativa de pepinos
    def test_cuke_negative_int_amount(self):
        cukes = "-5"
        context = Context()

        step_given_eaten_cukes(context, cukes)

        expected_error_message = f"Se esperaba un número válido (entre 0 y 10000), pero se obtuvo: {cukes}"
        assert isinstance (context.error, ValueError) and str(context.error) == expected_error_message, f"Se esperaba un error, pero no se produjo. Error: {context.error}"

    # Test para una cantidad decimal negativa de pepinos
    def test_cuke_negative_float_amount(self):
        cukes = "-5.5"
        context = Context()

        step_given_eaten_cukes(context, cukes)

        expected_error_message = f"Se esperaba un número válido (entre 0 y 10000), pero se obtuvo: {cukes}"
        assert isinstance (context.error, ValueError) and str(context.error) == expected_error_message, f"Se esperaba un error, pero no se produjo. Error: {context.error}"

    # Test para una cantidad no numérica de pepinos
    def test_cuke_invalid_amount (self):
        cukes = "hola"
        context = Context()

        step_given_eaten_cukes(context, cukes)

        expected_error_message = f"Se esperaba una cadena numérica, pero se obtuvo: {cukes}"
        assert isinstance (context.error, ValueError) and str(context.error) == expected_error_message, f"Se esperaba un error, pero no se produjo. Error: {context.error}"
        