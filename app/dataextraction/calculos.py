from dataextraction.lectura_excel import ProcesamientoExcel

if __name__ == "django.core.management.commands.shell":
    ruta = "dataextraction/Recibos/Fechas_Indicadores.xlsx"
    datos_excel = ProcesamientoExcel.lectura_xls(ruta) #lista de diccionarios
    print(datos_excel)

