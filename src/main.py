import fitz 
doct=fitz.open("D:\\Jazmin\\Archivos Personales\\Facultad\\Facultad Analista de Sistemas\\5 CUATRI\\4Practica Profesional\\Recibos\\COL\\VIMEO_SD_PRESENTADA_1BIM_2022.pdf")
pag=doct.load_page(0)
resultado=pag.search_for("Transactions taxed with the general rate")
# extraer = pag.get_textbox(resultado)

convertido=pag.get_text("xhtml")

# for line in convertido:
#     print(line)

print(convertido)
doct_html=open("documento.html","w")
doct_html.write(convertido)
doct_html.close()
print(doct.get_toc())