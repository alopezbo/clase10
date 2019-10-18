# from mechanize import Browser
# import csv
# with open('namecsv.csv') as csvfile: #forma correcta de abrir un archivo
#     reader=csv.DictReader(csvfile)
#     for rows in csvfile:
#         browser=Browser()   #crear variable Browser
#         browser.open("https://www.tse.go.cr/consulta_persona/consulta_cedula.aspx")
#         form=browser.select_form("form1")
#         browser["txtcedula"]=rows
#         response=browser.submit()
#         name=str(rows)
#         file=open(name+".html","w")                    #Forma incorrecta
#         file.write(response.read().decode("utf-8"))     #de abrir
#         file.close()                                    #un archivo


#EJEMPLO 2
from mechanize import Browser
import csv
with open('namecsv.csv') as csvfile: #forma correcta de abrir un archivo
    reader=csv.DictReader(csvfile)
    for rows in csvfile:
        browser=Browser()   #crear variable Browser
        browser.open("https://www.tse.go.cr/consulta_persona/consulta_nombres.aspx")
        form=browser.select_form("form1")
        browser["txtcedula"]=rows
        response=browser.submit()
        name=str(rows)
        file=open(name+".html","w")                    #Forma incorrecta
        file.write(response.read().decode("utf-8"))     #de abrir
        file.close()                                    #un archivo


        txtnombre
        txtapellido1
        txtapellido2