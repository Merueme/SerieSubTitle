from sklearn.feature_extraction.text import TfidfVectorizer
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import os
import glob
from collections import defaultdict
resp = []

def _resp(s):
    global resp
    return resp.append(s)

def tfidfvectoriser(X):
    vectorizer = TfidfVectorizer(decode_error='ignore')
    X = vectorizer.fit_transform(X)
    tfidf_tokens = vectorizer.get_feature_names_out()
    tfidf_values = X.toarray()[0]
    result = list(zip(tfidf_tokens, tfidf_values))
    return result

async def insert_mongobd(collection, buffer):
    for corpus_name, buffer_by_corpus in buffer.items():
        for word, series_list in buffer_by_corpus.items():
            try:
                # Utiliser $addToSet pour ajouter des éléments uniques à la liste
                await collection.update_one({'word': word},
                                             {'$addToSet': {'series': {'$each': series_list}}},
                                             upsert=True)
                print('data inserted')
            except Exception as e:
                print(f'Error updating data for word ({word}) in corpus ({corpus_name}):', e)

async def process_data(name, sentence, collection):
    result_dict = defaultdict(list)
    tfidf_list = tfidfvectoriser([sentence])
    for word, tfidf in tfidf_list:
        existing = next((entry for entry in resp if entry[0] == word), None)
        if existing:
            existing[1].append([name, tfidf])
        else:
            _resp([word, [[name, tfidf]]])

        try:
            await collection.update_one({'word': word},
                                         {'$addToSet': {'series': {'tfidf': tfidf, 'serie': name}}},
                                         upsert=True)
        except Exception as e:
            print(f'Error updating data for word ({word}) in corpus ({name}):', e)

async def main():
    myclient = AsyncIOMotorClient("mongodb://localhost:27017/")
    mydb = myclient["SAE"]
    mycoll = mydb['Mots']
    path = 'Word_Clean'
    corpus_list = []
    name_file = []

    for fichier in glob.glob(os.path.join(path, "*.txt")):
        with open(fichier, 'r') as file:
            corpus = file.read()
            if corpus:
                corpus_list.append(corpus)
                file_name_splitOne = fichier.split('\\')
                file_name_splitTwo = file_name_splitOne[1].split('_')
                name_file.append(file_name_splitTwo[0])

    result_dict_by_corpus = defaultdict(lambda: defaultdict(list))
    tasks = []

    for i, corpus in enumerate(corpus_list, start=1):
        name = name_file[i-1]
        task = asyncio.create_task(process_data(name, corpus, mycoll))
        tasks.append(task)

    # Attendre que toutes les coroutines aient terminé
    await asyncio.gather(*tasks)

    myclient.close()

if __name__ == '__main__':
    asyncio.run(main())
