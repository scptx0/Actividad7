import pytest
from src.belly import Belly

@pytest.mark.ejercicio10
def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15