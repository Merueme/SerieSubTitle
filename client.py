import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["SAE"]
mycoll = mydb['Utilisateur']

def insertClient(name):
    try:
        mycoll.insert_one({'UserName': name, 'seriLike': []})
        print('Insert Sucessfull')
    except:
        print('Error during the insertion of ', name)

def addLikeToClient(name, listToAdd):
    try:
        mycoll.update_one({'UserName': name}, {'$addToSet': {'seriLike': { '$each' : listToAdd}}}, upsert=True)
        print('Update Sucessfull')
    except:
        print('Error during the insertion of ', listToAdd, ' for ', name)

def getSerieLiked(name):
    try:
        user = mycoll.find({'UserName': name['UserName']})
        return(user)
    except:
        return(-1)

def getListClient():
    try:
        lis = mycoll.find()
        return(lis)
    except:
        return(-1)

def generationUser():    
    insertClient('Broisin')
    insertClient('Boughanem')
    addLikeToClient('Broisin', ['lost'])


#for name in getListClient():
#    print(name['UserName'])
#    for n in getSerieLiked(name):
#        print(n['seriLike'])