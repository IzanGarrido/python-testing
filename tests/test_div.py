# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import div

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación resta
    def test_div(self):
        assert div(2,1) == 2
        assert div(3,1) == 3
        assert div(4,1) == 4
        assert div(5,1) == 5
