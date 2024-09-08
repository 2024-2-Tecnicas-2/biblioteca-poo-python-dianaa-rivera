import os
import sys
import unittest
from io import StringIO
from libro import Libro

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLibro(unittest.TestCase):
    def setUp(self):
        self.libro = Libro("Cien años de soledad", 1967, "Gabriel Garcia Márquez", 447)

    def test_inicializacion(self):
        self.assertEqual(self.libro.titulo, "Cien años de soledad")
        self.assertEqual(self.libro.año_publicacion, 1967)
        self.assertEqual(self.libro.autor, "Gabriel Garcia Márquez")
        self.assertEqual(self.libro.num_paginas, 447)

    def test_mostrarInfo(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        self.libro.mostrarInfo()

        sys.stdout = sys.__stdout__

        expected_output = ("Titulo: Cien años de soledad, Año de publicacion: 1967\n"
                           "Autor: Gabriel Garcia Márquez, Numero de paginas: 447\n")
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()