import sys
import os
import unittest
from io import StringIO
from publicacion import Publicacion

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPublicacion(unittest.TestCase):
    def setUp(self):
        self.publicacion = Publicacion("Cien años de soledad", 1967)

    def test_inicializacion(self):
        self.assertEqual(self.publicacion.titulo, "Cien años de soledad")
        self.assertEqual(self.publicacion.año_publicacion, 1967)

    def test_mostrarInfo(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        self.publicacion.mostrarInfo()

        sys.stdout = sys.__stdout__

        expected_output = "Titulo: Cien años de soledad, Año de publicacion: 1967\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()