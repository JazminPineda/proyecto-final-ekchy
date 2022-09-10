import unittest
from dataextraction.argentina_extraccion import ExtraccionArgentina


class TestArgentinaExtraction(unittest.TestCase):

    texto = ""

    def setUpClass():
        ruta_archivo = "dataextraction\Recibos\ARG\AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"

        extraccion = ExtraccionArgentina()
        TestArgentinaExtraction.texto = extraccion.lectura(ruta_archivo)

    def test_extraccion_argentina_lectura_exito(self):
        self.assertNotEqual("", self.texto)
        self.assertEqual(len(self.texto), 3282)

    def test_extraccion_argentina_lectura_ruta_no_valida(self):
        """Test prueba cuando la función lectura recibe una ruta vacia y devuelve Exception"""
        with self.assertRaises(Exception):
            extraccion = ExtraccionArgentina()
            extraccion.lectura("")

    def test_extraccion_argentina_validaformulario_pais(self):
        """Test prueba si es correcto el numero de formualario del pais Argentina"""
        n_formulario_output = ""

        extraccion = ExtraccionArgentina()
        lineas = extraccion.procesamiento(self.texto)
        resultado = extraccion.extraccion(self.texto, lineas)
        n_formulario_output = resultado[4]

        self.assertEqual(len(resultado), 9)
        self.assertEqual(n_formulario_output, "731")
