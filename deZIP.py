import os
from zipfile import ZipFile
import rarfile

##directSub = 'D:\IUT\Semestre5\SAE\sous-titres'

def main(directSub) :
    for x in os.walk(directSub) :
        for name in x[2]:
            if name.endswith('.zip'):
                try :
                    print(x[0] + '/'+ name)
                    with ZipFile(x[0] + '/'+ name  ,'r') as file:
                        file.extractall(path = x[0])
                    print('DONE : ' + name)
                    os.remove(x[0] + '/'+ name)
                except :
                    print('BLOCKED :' + name)
            if name.endswith('.rar'):
                try :
                    print(x[0] + '/'+ name)
                    with rarfile(x[0] + '/'+ name  ,'r') as file:
                        file.extract(path = x[0])
                    print('DONE : ' + name)
                    os.remove(x[0] + '/'+ name)
                except :
                    print('BLOCKED :' + name)