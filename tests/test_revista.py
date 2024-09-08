import os
import sys
import unittest
from io import StringIO
from revista import Revista

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestRevista(unittest.TestCase):
    def setUp(self):
        self.revista = Revista("Editorial Sudamericana", 1967, 50, "Sudamericana")

    def test_inicializacion(self):
        self.assertEqual(self.revista.titulo, "Editorial Sudamericana")
        self.assertEqual(self.revista.año_publicacion, 1967)
        self.assertEqual(self.revista.numero_revista, 50)
        self.assertEqual(self.revista.nombre_revista, "Sudamericana")

    def test_mostrarInfo(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        self.revista.mostrarInfo()

        sys.stdout = sys.__stdout__

        expected_output = ("Titulo: Editorial Sudamericana, Año de publicación: 1967\n"
                           "Numero de la revista: 50, Nombre de la revista: Sudamericana\n")
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()