from mechanize import Browser
import csv
with open ('namecsv.csv') as csvfile:
    reaver=csv.DictReader(csvfile)
    for rows in csvfile:
        browser=Browser()
        browser.open("https://www.tse.go.cr/consulta_persona/consulta_cedula.aspx")
        form=browser.select_form("form1")
        browser["texcedula"]=rows
        response=browser.submit()
        name=str(rows)
        file=open("+name+.html","w")
        file.write(response.read())
        file.close()