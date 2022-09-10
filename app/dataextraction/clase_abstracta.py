from abc import ABC, abstractmethod
"""Sirve para definir un conjunto de funciones comunes a otras clases."""

  ## Se Crea clase base / padre que hereda de
class Extraer(ABC):
    ruta = None

    @abstractmethod
    def __init__(self, ruta):
       pass

    @abstractmethod
    def lectura(self):
        pass

    @abstractmethod
    def extraccion(self):
        pass

     @abstractmethod
    def guardar_datos(self):
        pass
