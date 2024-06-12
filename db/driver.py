import pymongo
from pymongo import MongoClient


class Driver:
    def __init__(self, username: str, password: str) -> None:
        uri = self._generate_login_string(username, password)
        try:
            self.client = MongoClient(uri)
        except Exception as e:
            raise Exception("Unable to connect.")

    def get_database(self, database: str) -> None:
        if database != "" and self.client is not None:
            self.database = self.client.get_database(database)

    def get_collection(self, collection: str) -> None:
        if collection != "":
            if isinstance(self.database, pymongo.database):
                self.collection = self.database.get_collection(collection)

    def _generate_login_string(self, username: str, password: str) -> str:
        uri = "mongodb+srv://{}:{}@a4.uajhqu4.mongodb.net/?retryWrites=true&w=majority&appName=a4"
        return uri.format(username, password)