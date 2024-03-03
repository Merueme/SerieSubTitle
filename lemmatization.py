from simplemma import lemmatize, lang_detector, text_lemmatizer
import os

directFull = 'D:\IUT\Semestre5\SAE\subtitle_FULL'
directClean = 'D:\IUT\Semestre5\SAE\Word_Clean'

def wordLanguage(word):
    list = lang_detector(word, lang=("en","fr"))
    buffer = 0
    l = 0
    for m in list :
        if m[1] > buffer:
            buffer=m[1]
            l = m[0]
    return l

def clean(word):
    lng = wordLanguage(word)
    if lng == 'fr' :
        w=lemmatize(word, lang='fr')
    elif lng == 'en' :
        w=lemmatize(word, lang='en')
    else :
        w=word
    return w

def main(directFull, directClean) :
    for x in os.walk(directFull):
        for name in x[2]:
            print(name)
            with open(directFull.__str__()+'/'+name, errors='replace', encoding='ANSI') as doc:
                text = doc.read()
                listWord = text_lemmatizer(text, lang=('en','fr'), greedy=True)
                listWordClean = ''
                print('--Done Cut--')
                
                print(listWord.__len__())
                listWordClean = ' '.join(listWord)

                '''for word in listWord :
                    listWordClean = listWordClean + ' ' + word
                    print(1)'''
                print('--Done Clean--')
                
            with open(directClean.__str__()+'/'+name, 'w', encoding='ANSI') as doc:
                doc.write(listWordClean)