import deZIP as Zip
import convertSRT as SRT
import cleanTXT as TXT
import lemmatization as lem
from pathlib import Path
import process_asyncio as asyn
import client as client


directSub = Path(__file__).with_name('sous-titres')
directSub = directSub.absolute()

directFull = Path(__file__).with_name('subtitle_FULL')
directFull = directFull.absolute()

directClean = Path(__file__).with_name('Word_Clean')
directClean = directClean.absolute()

def testAlgo():
    rep = ''
    while (rep not in ['allUser', 'likeUser', 'insertUser', 'insertLike', 'willLike', 'search', 'exit']):
        print(' __________________________________________________________________________________________________________________')
        print('|     Lister tout les utilisateurs                 : allUser                                                       |')
        print('|     Voir les series Like d\'un utilisateur        : likeUser                                                      |')
        print('|     Inserer un Utilisateur                       : insertUser                                                    |')
        print('|     Ajouter des Series like pour un utilisateur  : insertLike                                                    |')
        print('|     Recommendation serie pour un utilisateur     : willLike                                                      |')
        print('|     Chercher une serie                           : search                                                        |')
        print('|                                                                                                                  |')
        print('|     exit : quit                                                                                                  |')
        print('|__________________________________________________________________________________________________________________|')
        rep = input(" : ")
    
    if (rep == 'allUser'):
        for name in client.getListClient():
            print(name['UserName'])

    if (rep == 'likeUser'):
        inp = input('User : ')
        for n in client.getSerieLiked(inp):
            print(n['seriLike'])
    
    if (rep == 'insertUser'):
        inp = input('Utilisateur à ajouter : ')
        client.insertClient(inp)

    if (rep == 'insertLike'):
        i = input('Utilisateur : ')
        inp = []
        r=''
        while (r == 'q'):
            inp.append(input('Serie aimer à ajouter au client ', i, '(q pour stop) : '))
        client.addLikeToClient(i, inp)

    if (rep == 'willLike'):#------------------------------------------------------------------------------------------------------------------------------
        print()

    if (rep == 'search'):#--------------------------------------------------------------------------------------------------------------------------------
        print()

    if (rep == 'quit'):
        return 'y'

    while (rep not in ['y', 'n']):
        print(' __________________________________________________________________________________________________________________')
        rep = input('Retourner au choix precedent ? (y/n) : ')
    return rep

def workSub():
    rep = ''
    while(rep not in ['zip', 'txt','_full', '_clean', 'mongodb', 'exit']):
        print(' __________________________________________________________________________________________________________________')
        print('|     run only deZip                               : zip                                                           |')
        print('|     run depuis Conversion en TXT                 : txt                                                           |')
        print('|     run depuis Creation des _FULL.TXT            : _full                                                         |')
        print('|     run depuis Creation des fichiers _CLEAN.TXT  : _clean                                                        |')
        print('|     run generation database                      : mongodb                                                       |')
        print('|                                                                                                                  |')
        print('|     exit : quit                                                                                                  |')
        print('|__________________________________________________________________________________________________________________|')
        rep = input("option de lancement : ")

    if (rep in ['zip']):
        i=0
        n= input('Combien de deZip necessaire (default 3) : ')
        if (n==''): 
            n=3
        while( i < int(n)):
            Zip.main(directSub) #specify quantity of dezip
            i=i+1
        print('--------------------------------------------------UNZIP DONE--------------------------------------------------------')

    if (rep in ['txt']):
        SRT.main(directSub)
        print('----------------------------------------------TXT CONVERT DONE------------------------------------------------------')

    if (rep in ['txt','_full']):
        TXT.main(directSub, directFull)
        print('--------------------------------------------_FULL GENERATION DONE---------------------------------------------------')

    if (rep in ['txt','_full', '_clean']):
        lem.main(directFull, directClean)
        print('--------------------------------------------_CLEAN GENERATION DONE--------------------------------------------------')

    if (rep in ['txt','_full', '_clean', 'mongodb']):
        asyn.main()
        print('-------------------------------------------DATABASE GENERATION DONE-------------------------------------------------')

rep = ''
while(rep not in ['algo', 'generate','exit']):
    print(' __________________________________________________________________________________________________________________')
    print('|     Algorithme de recherhe / recommandation et gestion des Users   : algo                                        |')
    print('|     Ajouter de nouveau sous-titres à la database                   : generate                                    |')
    print('|                                                                                                                  |')
    print('|     exit : exit                                                                                                  |')
    print('|__________________________________________________________________________________________________________________|')

    rep = input(" : ")

if(rep == 'generate'):
    workSub()
elif (rep == 'algo'):
        loop = 'y'
        while (loop == 'y') :
            loop = testAlgo()