import os
from zipfile import ZipFile

direccion = "G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2/python_books.zip"

with ZipFile (direccion) as archivo:
    archivo.extractall("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2")

import shutil
shutil.rmtree("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2/__MACOSX")

for archivo in os.walk("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2/python_books"):
    print(archivo)
    
for raiz, dirs, archivos in os.walk("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2/python_books"):
    # print(raiz, dirs, archivos)	
    for a in archivos: 
        print(a)

import fitz

documento = fitz.open("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2/python_books/Python - Finance.pdf")

documento1 = fitz.open("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2/python_books/Python - AWS.pdf")

documento2 = fitz.open("G:/Mi unidad/NANI/_ESTUDIOS/_Especialización/Semestre 2/NLP/Clase 2/Taller 2/python_books/Python  Data Science Cookbook.pdf")

pagina = documento.loadPage(0)
texto = pagina.getText("text")
palabras = texto.split()
Num_palabras = len(palabras)
print ("El documento Python - Finance contiene: " + str(Num_palabras) + " palabras")

pagina1 = documento1.loadPage(0)
texto1 = pagina1.getText("text")
palabras1 = texto1.split()
Num_palabras1 = len(palabras1)
print ("El documento Python - AWS contiene: " + str(Num_palabras1) + " palabras")

pagina2 = documento2.loadPage(0)
texto2 = pagina2.getText("text")
palabras2 = texto2.split()
Num_palabras2 = len(palabras2)
print ("El documento Python  Data Science Cookbook contiene: " + str(Num_palabras2) + " palabras")

