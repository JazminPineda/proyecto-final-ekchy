# ***Formato separado**
# 
from tabula import read_pdf
from tabulate import tabulate
import pandas as pd
import numpy as np
# doct=read_pdf("D:\\Jazmin\\Archivos Personales\\Facultad\\Facultad Analista de Sistemas\\5 CUATRI\\4Practica Profesional\\Recibos\\COL\\VIMEO_SD_PRESENTADA_1BIM_2022.pdf")

#**Formulario IvA-ARG
#doct=read_pdf("D:\\Jazmin\\Archivos Personales\\Facultad\\Facultad Analista de Sistemas\\5 CUATRI\\4Practica Profesional\\Recibos\\ARG\\PruebaAR02_IVA_DDJJ.pdf")


# año_gravable= doct[0].iloc[[1],[3]] # pendiente separar cuit y periodo fiscal 
#form_razon=doct[0].iloc[[4],[0]] #pendiente separar formulario y razon social 
# nit= esta todo unido activi principal 
#actividad_princ= doct[0].iloc[[3],[3]] #pendiente separar form, CUIT, actividad principal y N° verificador
# Saldo_proveedores = doct[0].iloc[[11],[3]] #pendiente separar CUIT y valor 
# debito_fiscal= doct[0].iloc[[12],[3]]
# credito_fiscal= doct[0].iloc[[13],[3]]
#valores todos

for fila in doct[0].loc[11:].itertuples():#salo las primeras 11 filas
    print(fila[1], fila[4])
    
  



#**Formulario ICA-COL
#doct=read_pdf("D:\\Jazmin\\Archivos Personales\\Facultad\\Facultad Analista de Sistemas\\5 CUATRI\\4Practica Profesional\\Recibos\\COL\\Decla. ICA II BIM 2022 - CO10.pdf")

# año_gravable=doct[0].iloc[[0],[0]]
# periodo fiscal= n/a esta tomado con x y no se lee
# razon_social=doct[0].iloc[[2],[3]]
# nit=doct[0].iloc[[4],[3]]
# actividad_princ=doct[0].iloc[[7],[0]]
    
# # print(f'{fila[1]}|{fila[17]}|{fila[18]}') ** impresión valores formulario ICA
# for fila in doct[0].loc[10:].itertuples():#salo las primeras 10 filas
#     valor = 0

#     if type(fila[17]) == str:
#         valor = fila[17]
#     if type(fila[18]) == str:
#         valor = fila[18]
#     valores_ica={fila[1]}|{valor}
#     #print(f'{fila[1]}|{valor}')
 