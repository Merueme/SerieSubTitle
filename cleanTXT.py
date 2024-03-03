import os
import openpyxl as xl

dirSub = '.\sous-titres'
dirEnd = '.\subtitle_FULL'

def main(dirSub, dirEnd) :
    dirList = os.listdir(dirSub)

    for name in dirList:
        dirSerie = dirSub.__str__() + '/' + name
        concat = ''
        for x in os.walk(dirSerie):
            for title in x[2]:
                if title.endswith('.txt'):
                    with open(x[0] +'/'+ title, encoding='ANSI') as file:
                        text = file.read()
                        concat = concat + '\n' + text
        with open(dirEnd.__str__() + '/' + name + '_FULL.txt' ,'w', encoding='ANSI') as file :
            file.write(concat)

