import re, sys

def converterSUB(args):
    file_name = args
    with open(file_name, errors='replace', encoding='ANSI') as doc:
        lineList = []
        for line in doc:
            line.strip()
            str = ''
            for t in line.split('|'):
                str = str + ' ' + t.split("}")[-1]
            lineList.append(str)
        new_file_name = file_name[:-4] + '.txt'
        with open(new_file_name, 'w', encoding = 'ANSI') as f:
            for line in lineList:
                f.write(line)
        

def converterASS(args):
    file_name = args
    with open(file_name, errors='replace', encoding='ANSI') as doc:
        lineList = []
        for line in doc :
            line.strip()

            if not line.startswith("Dialogue") :
                continue
            
            clean = line.split(',')
            buffer = ",".join(clean[9:]).replace("  ", " ").replace("\\N", "\\n").split("\\n")
            bufferString = ''
            for a in buffer:
                bufferString = bufferString + ' ' + a
            lineList.append(re.sub('{.*}','',bufferString))
        new_file_name = file_name[:-4] + '.txt'
        with open(new_file_name, 'w', encoding = 'ANSI') as f:
            for line in lineList:
                f.write(line)
