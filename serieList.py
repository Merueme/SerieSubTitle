from os import walk
import openpyxl as xl

directSub = 'D:\IUT\Semestre5\SAE\sous-titres'
directXml = 'D:\IUT\Semestre5\SAE\Database.xlsx'
directGen = 'D:\IUT\Semestre5\SAE'
names = []

for x in walk(directSub) :
    serieName = x[0].replace(directSub , '')   
    serieName = serieName.replace('\\', '')
    if not serieName == '' :
        names.append(serieName)

file = xl.load_workbook(directXml)
workSheet = file['Sheet1']

i = 2

for n in names :
    workSheet.cell(i,1).value = n
    i=i+1

file.save(directXml)