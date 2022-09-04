from argentina_extraccion import ExtraccionArgentina
from cololombia_extraccion import ExtraccionColombia
from mexico_extraccion import ExtraccionMexico

if '__main__'== __name__:
    ruta_arg = "app\dataextraction\Recibos\ARG\AR02 BSF AR02_IVA_02.2022_F 731 DDJJ .pdf"
    ruta_col = "app\dataextraction\Recibos\COL\Decla. IVA II BIM 2022 - CO10.pdf"
    ruta_mex = "app\dataextraction\Recibos\MEX\MEX_VAT_Feb2022_Detail.pdf"

    argentina = ExtraccionArgentina()
    texto = argentina.lectura(ruta_arg)
    lineas_procesa = argentina.procesamiento(texto)
    extracion_arg = argentina.extraccion(texto, lineas_procesa)
    print(extracion_arg)

    colombia = ExtraccionColombia()
    texto = colombia.lectura(ruta_col)
    lineas_process = colombia.procesamiento(texto)
    extracion_col = colombia.extraccion(texto, lineas_process)
    print(extracion_col)
   
    mexico = ExtraccionMexico()
    texto = mexico.lectura(ruta_mex)
    extracion_mex = mexico.extraccion(texto)
    print(extracion_mex)