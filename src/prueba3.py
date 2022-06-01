import PyPDF2
pdf_file_obj= open("recibos/VIMEO_SD_PRESENTADA_1BIM_2022.pdf", "rb")
pdf_read= PyPDF2.PdfFileReader(pdf_file_obj)
#print("encriptado", pdfReader.isEncrypted)
info =pdfReader.documentInfo()
