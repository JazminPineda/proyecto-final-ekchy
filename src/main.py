import fitz 
doct=fitz.open("recibos/VIMEO_SD_PRESENTADA_1BIM_2022.pdf")
pag=doct.load_page(0)
resultado=pag.search_for("Transactions taxed with the general rate")
pag.get_textbox(resultado)
print(pag.get_textbox(resultado))


# convertido=pag.get_text("dict")
# print(convertido)
# doct_html=open("documento.json","w")
# doct_html.write(convertido)
# doct_html.close()
#print(doct.get_toc())