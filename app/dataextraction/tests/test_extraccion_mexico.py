import unittest
from dataextraction.mexico_extraccion import ExtraccionMexico


class TestMexicoExtraction(unittest.TestCase):
    texto = ""

    def setUpClass():
        ruta_archivo = "dataextraction/Recibos/MEX/MEX_VAT_Feb2022_Detail.pdf"
        extraccion = ExtraccionMexico()
        TestMexicoExtraction.texto = extraccion.lectura(ruta_archivo)

    def test_extraccion_mexico_lectura_exito(self):
        self.assertNotEqual("", self.texto)
        self.assertEqual(len(self.texto), 1908)  ## validar como carajo se ejct

    def test_extraccion_mexicoa_ruta_no_valida(self):
        """Test prueba cuando la función lectura recibe una ruta vacia y devuelve Exception"""
        with self.assertRaises(Exception):
            extraccion = ExtraccionMexico()
            extraccion.lectura("")

    def test_extraccion_mexico_validaformulario_pais(self):
        """Test prueba si es correcto el numero de formualario del pais Mexico"""
        n_formulario_output = ""

        extraccion = ExtraccionMexico()
        lineas = extraccion.procesamiento(self.texto)
        resultado = extraccion.extraccion(lineas)
        n_formulario_output = resultado[4]
        self.assertEqual(len(resultado), 10)
        self.assertEqual(n_formulario_output, "001")
