from colparse import ArgumentError
import unittest
from colombia_extraccion import ExtraccionColombia

class TestColombiaExtraction(unittest.TestCase):
    # ruta_archivo = "app/dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    ruta_archivo = "app/dataextraction/Recibos/COL/Decla. IVA II BIM 2022 - CO10.pdf"

    def test_extraccion_colombia_lectura_exito(self):

        extraccion = ExtraccionColombia()
        resultado = extraccion.lectura(self.ruta_archivo)

        self.assertNotEqual("",resultado)
        self.assertEqual(len(resultado),3282) ## validar como carajo se ejct


    def test_extraccion_colombia_ruta_no_valida(self):
        """Test prueba cuando la función lectura recibe una ruta vacia y devuelve Exception"""
        with self.assertRaises(Exception):
            extraccion = ExtraccionColombia()
            resultado = extraccion.lectura("")
    
    def test_extraccion_colombia_validaformulario_pais(self):
        """Test prueba si es correcto el numero de formualario del pais"""
        if n_formulario_output == "300":
            nombre_formulario = "IVA"
        else:
            print("Revisar ")


    def test_extraccion_colombia_procesamiento_regex(self):
        pass
    
    def test_extraccion_colombia_base_datos(self):
        pass