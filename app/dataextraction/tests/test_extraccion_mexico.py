import unittest
from app.dataextraction.mexico_extraccion import ExtraccionMexico

class TestMexicoExtraction(unittest.TestCase):
    lineas = ''
    def setUpClass():
        ruta_archivo = "app\dataextraction\Recibos\MEX\MEX_VAT_Feb2022_Detail.pdf"
        extraccion = ExtraccionMexico()
        TestMexicoExtraction.lineas = extraccion.lectura(ruta_archivo)

    def test_extraccion_mexico_lectura_exito(self):
        self.assertNotEqual("",self.lineas)
        self.assertEqual(len(self.lineas),34) ## validar como carajo se ejct


    def test_extraccion_mexicoa_ruta_no_valida(self):
        """Test prueba cuando la función lectura recibe una ruta vacia y devuelve Exception"""
        with self.assertRaises(Exception):
            extraccion = ExtraccionMexico()
            extraccion.lectura("")
    
    def test_extraccion_mexico_validaformulario_pais(self):
        """Test prueba si es correcto el numero de formualario del pais Mexico"""
        n_formulario_output = ''

        extraccion = ExtraccionMexico()
        resultado = extraccion.extraccion(self.lineas)
        n_formulario_output = resultado[4]        
        self.assertEqual(len(resultado),10)
        self.assertEqual(n_formulario_output, "001")
        