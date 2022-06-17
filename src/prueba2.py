# ***Formato separado**
# 
from tabula import read_pdf
from tabulate import tabulate
import pandas as pd
doct=read_pdf("D:\\Jazmin\\Archivos Personales\\Facultad\\Facultad Analista de Sistemas\\5 CUATRI\\4Practica Profesional\\Recibos\\COL\\Decla. ICA II BIM 2022 - CO10.pdf")
# doct=read_pdf("D:\\Jazmin\\Archivos Personales\\Facultad\\Facultad Analista de Sistemas\\5 CUATRI\\4Practica1 Profesional\\Recibos\\ARG\\PruebaAR02_IVA_DDJJ.pdf")
# doct=read_pdf("D:\\Jazmin\\Archivos Personales\\Facultad\\Facultad Analista de Sistemas\\5 CUATRI\\4Practica Profesional\\Recibos\\COL\\VIMEO_SD_PRESENTADA_1BIM_2022.pdf")

for fila in doct[0].itertuples():
    # print(fila)
    # print(f'{fila[1]}|{fila[17]}|{fila[18]}')
    valor = 0
    if fila[17] != 'nan':
        valor = fila[17]
    if fila[18] != 'nan':
        valor = fila[18]
    print(f'{fila[1]}|{valor}')
 