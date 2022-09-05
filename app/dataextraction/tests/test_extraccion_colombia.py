
import unittest
from app.dataextraction.cololombia_extraccion import ExtraccionColombia

class TestColombiaExtraction(unittest.TestCase):
    
    texto = ''

    # Prepara los datos para realizar los test
    def setUpClass():
        ruta_archivo = "app\dataextraction\Recibos\COL\Decla. IVA II BIM 2022 - CO10.pdf"
        extraccion = ExtraccionColombia()
        TestColombiaExtraction.texto = extraccion.lectura(ruta_archivo)

    def test_extraccion_colombia_lectura_exito(self):
        self.assertNotEqual("", self.texto)
        self.assertEqual(len(self.texto),5013) ## validar como carajo se ejct


    def test_extraccion_colombia_ruta_no_valida(self):
        """Test prueba cuando la función lectura recibe una ruta vacia y devuelve Exception"""
        with self.assertRaises(Exception):
            extraccion = ExtraccionColombia()
            extraccion.lectura("")
    
    def test_extraccion_colombia_validaformulario_pais(self):
        """Test prueba si es correcto el numero de formualario del pais Colombia"""
        n_formulario_output = ''
        extraccion = ExtraccionColombia()
        diccionario = extraccion.procesamiento(self.texto)
        resultado = extraccion.extraccion(self.texto, diccionario)
        n_formulario_output = resultado[4]
        self.assertEqual(len(resultado),9)
        self.assertEqual(n_formulario_output, "300")

      
