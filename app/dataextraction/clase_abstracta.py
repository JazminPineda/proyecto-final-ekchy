from abc import ABC, abstractmethod

"""Sirve para definir un conjunto de funciones comunes a otras clases."""
import pdfplumber

## Se Crea clase base / padre que hereda de
class Extraer(ABC):
    ruta = None

    _laparams = None


    @abstractmethod
    def extract_text(self, pdf) -> str:
        pass

    def lectura(self, ruta_archivo):
        if len(ruta_archivo) < 1:
            raise Exception("ruta no valida")

        with pdfplumber.open(ruta_archivo, laparams=self._laparams) as pdf:
            return self.extract_text(pdf)

    @abstractmethod
    def procesamiento(self, text):
        pass

    @abstractmethod
    def extraccion(self, text, lineas):
        pass

    # @abstractmethod
    # def guardar_datos(self):
    #     pass
