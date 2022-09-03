from mexparse import ArgumentError
import unittest
from mexico_extraccion import ExtraccionMexico

class TestMexicoExtraction(unittest.TestCase):

    ruta_archivo = "app/dataextraction/Recibos/MEX/MEX_VAT_Feb2022_Detail.pdf"

    def test_extraccion_mexico_lectura_exito(self):

        extraccion = ExtraccionColombia()
        resultado = extraccion.lectura(self.ruta_archivo)

        self.assertNotEqual("",resultado)
        self.assertEqual(len(resultado),3282) ## validar como carajo se ejct


    def test_extraccion_mexicoa_ruta_no_valida(self):
        """Test prueba cuando la función lectura recibe una ruta vacia y devuelve Exception"""
        with self.assertRaises(Exception):
            extraccion = ExtraccionColombia()
            resultado = extraccion.lectura("")
    
    def test_extraccion_mexico_validaformulario_pais(self):
        """Test prueba si es correcto el numero de formualario del pais Mexico"""

        if nomb_formulario == "IMPUESTO AL VALOR AGREGADO POR LA PRESTACIÓN DE SERVICIOS DIGITALES":
            n_formulario_output = "001"
            nomb_output = "IVA DIGITALES"

        else:
            print("Revisar ")


    def test_extraccion_mexico_procesamiento_regex(self):
        pass
    
    def test_extraccion_mexico_base_datos(self):
        pass