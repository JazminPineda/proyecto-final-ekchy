from argentina_extraccion import ExtraccionArgentina


if '__main__'== __name__:
    # ruta_archivo = "app/dataextraction/Recibos/ARG/AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    ruta_archivo = "app\dataextraction\Recibos\ARG\AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    argentina = ExtraccionArgentina()
    texto = argentina.lectura(ruta_archivo)
    lineas_procesa = argentina.procesamiento(texto)
    extracion_arg = argentina.extraccion(texto, lineas_procesa)
    print(extracion_arg)
   
