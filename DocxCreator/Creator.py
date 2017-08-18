import csv 
from docx import Document
from docx.shared import Inches

fileCSV  = open('leiaute.csv')
document = Document()
fileCsv = csv.reader(fileCSV, delimiter = ',')

exclusoes = {"4", "10", "13", "23", "31" , "36", "40", "44" , "48" ,"53" , "60", "61", "70", "78", "83", "92" , 
"100", "102", "107", "113" , "114", "122", "125", "126", "132", "132", "135", "137", "140", "147", "149", "155", 
"159", "163", "164", "168", "177", "182", "185", "187", "189", "194", "197"}

for x in fileCsv: 
    print(x[0])
    if((x[0] not in exclusoes)):
        linha = 'Campo '+ x[0] + ' - ' + x[1]+ '\n'+ x[8] + '\n' 
        document.add_paragraph(linha, style='ListNumber')

fileCSV.close()
document.save('demo.docx')
