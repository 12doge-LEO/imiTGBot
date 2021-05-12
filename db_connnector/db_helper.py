import pymongo
from gridfs import *
import bson


class dbConnector:
    def __init__(self):
        self.__db_name = "imiDB"
        self.__user_name = "doge12"
        self.__user_pwd = "doge12"
        self.__token = f"mongodb+srv://{self.__user_name}:{self.__user_pwd}@cluster0.mk62e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

        self.__client = pymongo.MongoClient(self.__token)

        self.__collection = "imiRecords"

    def _get_collection(self):
        return self.__collection

    def test(self):
        print(self.__client[self._get_collection()])

    def insert_record(self, data: dict):
        if self.__client[self._get_collection()]["db1"].find({"rid": data["rid"]}).count() > 0:
            print("record exists")
            return False
        else:
            return self.__client[self._get_collection()]["db1"].insert_one(data)

    def insert(self, data: dict):
        return self.__client[self._get_collection()]["db1"].insert_one(data)

    def find(self,key: dict=''):
        try:
            return list(self.__client[self._get_collection()]["db1"].find(key))
        except Exception as e:
            print(e)

    def insert_file(self, filename: str = '', id: str = '',collection:str =''):
        if filename == '':
            return False
        else:
            fs = GridFS(self.__client[self._get_collection()], collection=collection)
            with open(filename,'rb') as f:
                audio_bin = bson.binary.Binary(f.read())
            fs.put(filename=filename,id=id, data=audio_bin)

    def update(self,key:dict ='',data:dict=''):
        if self.__client[self._get_collection()]["db1"].find(key).count() > 0:
            return self.__client[self._get_collection()]["db1"].update(key,data)
        else:
            self.insert(data)

    def get_file(self,filename: str='',collection:str =''):
        if filename == '':
            return
        else:
            fs = GridFS(self.__client[self._get_collection()], collection=collection)
            if fs.exists({"filename":filename}):
                for grid_out in fs.find({"filename":"meow2.mp3"}):
                    return grid_out.read()
            else:
                print("file not exist")
                return False


imi_db_connector = dbConnector()
