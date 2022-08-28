from argparse import ArgumentError
import unittest
from argentina_extraccion import ExtraccionArgentina

class TestArgentinaExtraction(unittest.TestCase):
    # ruta_archivo = "app/dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    ruta_archivo = "Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"

    def test_extraccion_argentina_lectura_exito(self):

        extraccion = ExtraccionArgentina()
        resultado = extraccion.lectura(self.ruta_archivo)

        self.assertNotEqual("",resultado)
        self.assertEqual(len(resultado),3282)


    def test_extraccion_argentina_lectura_ruta_no_valida(self):
        """Test prueba cuando la función lectura recibe una ruta vacia y devuelve Exception"""
        with self.assertRaises(Exception):
            extraccion = ExtraccionArgentina()
            resultado = extraccion.lectura("")
