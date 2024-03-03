import SRT_TXT as TXT
import SRT_SUB_ASS as SUB_ASS
import os

##directSub = 'D:\IUT\Semestre5\SAE\sous-titres'

def main(directSub):
    i=0
    for x in os.walk(directSub) :
        for name in x[2]:
            if name.endswith('.srt') or name.endswith('.vo') or name.endswith('.VO') or name.endswith('.SRT'): 
                TXT.main(x[0] +'/'+ name)
                i=i+1
            elif name.endswith('.sub') or name.endswith('.SUB'):
                SUB_ASS.converterSUB(x[0] +'/'+ name)
                i=i+1
            elif name.endswith('.ass') or name.endswith('.ssa') or name.endswith('.ASS') or name.endswith('.SSA'):
                SUB_ASS.converterASS(x[0] +'/'+ name)
                i=i+1
    ''' For test
            else :
                if not (name.endswith('.zip') or name.endswith('.rar')):
                    print(name) 
    '''
    print('Nbr de fichier convertit : ',i)