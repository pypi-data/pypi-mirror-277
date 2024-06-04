from typing import Any
import os
import pandas as pd
import pymongo
import json
from ensure import ensure_annotations


class mongo_operation:
    """
    A single call to MongoDB operation.

    -----
    PARAMS:
    client_uri : The client uri that you get from mongodb web page
    database_name : The database that one wants to connect to
    collection_name : The name of the collection that one wanta to connect to
    """

    __collection = None  # a variable that will be storing the collection name
    __database = None  # a variable that will be storing the databse name

    def __init__(
        self, client_uri: str, database_name: str, collection_name: str = None
    ):
        self.client_uri = client_uri
        self.database_name = database_name
        self.collection_name = collection_name

    @property
    def create_mongo_client(self):

        client = pymongo.MongoClient(self.client_uri)
        return client

    @property
    def connect_database(self):
        """
        for connecting the database
        """
        if mongo_operation.__database == None:
            self.database = self.create_mongo_client[self.database_name]
        return self.database

    @ensure_annotations
    def set_new_database(self, database: str):
        """
        To set new database for the mongoclient

        Args:
            database (str): pass the new db name
        """
        database = self.create_mongo_client[database]
        mongo_operation.__database = database
        self.database_name = database

    @property
    def connect_collection(self):
        """
        For connecting to collection instance
        """
        if mongo_operation.__collection == None:
            self.collection = self.connect_database[self.collection_name]

        return self.collection

    @ensure_annotations
    def set_new_collection(self, collection_name: str):
        """to set a new collection name

        Args:
            collection_name (str): pass new collection name

        """
        self.collection = self.connect_database[collection_name]
        mongo_operation.__collection = collection_name
        self.collection_name = collection_name

    @ensure_annotations
    def insert_record(self, record: dict, collection_name: str) -> Any:
        """
        insert one record to mongodb

        Args:
            record (dict): should be a dict
            collection_name (str): pass the name of collection that you want the record in
        """
        self.set_new_collection(collection_name=collection_name)
        if type(record) == list:
            for data in record:
                if type(data) != dict:
                    raise TypeError(" record must be dictionary")
            self.connect_collection.insert_many(record)
        elif type(record) == dict:
            self.connect_collection.insert_one(record)

    @ensure_annotations
    def bulk_insert(self, dataframe, collection_name: str = None, **kwargs):
        """
        Insert data from df object/ csv/ excel file to mongodb

        ------
        dataframe : path of the csv file or pandas df object
         ** kwargs : any paramters of pandas read function.
        """

        if collection_name:
            self.set_new_collection = collection_name

        if not isinstance(dataframe, pd.DataFrame):
            path = dataframe
            if path.endswith(".csv"):
                dataframe = pd.read_csv(path, encoding="utf8", **kwargs)
            elif path.endswith(".xlsx"):
                dataframe = pd.read_excel(path, encoding="utf8", **kwargs)

        data_json = json.loads(dataframe.to_json(orient="records"))
        self.connect_collection.insert_many(data_json)

    @ensure_annotations
    def find(self, collection_name: str = None, query: dict = {}):
        """
        To find data in mongodb
        returns the dataframe of the searched data
        """

        if self.collection_name not in self.connect_database.list_collection_name():
            raise NameError("collection not found in mongodb")
        else:
            self.set_new_collection = collection_name

        cursor = self.connect_collection.find(query)
        data = pd.DataFrame(list(cursor))

        return data

    @ensure_annotations
    def update(self, where_condition: dict, update_query: dict, update_all_data=False):
        """
        To update data in mongo db

        Args:
            where_condition (dict): condition to find the data
            update_query (dict): query to update the data
            update_all_data (bool, optional): if true, update all data in mongo db


        """
        if update_all_data:
            self.connect_collection.update_many(where_condition, {"$set": update_query})
        else:
            self.connect_collection.update_one(where_condition, {"$set": update_query})

    @ensure_annotations
    def delete_record(self, where_condition: dict, delete_all=False):
        """
        Use it to delete a record

        Args:
            where_condition (dict):
                            coloumn name and value upon which
                            the delete operation will be performed. pass this
                            as a dict
            delete_all (bool, optional):
                            Set to True if multiple records are to be deleted

        """
        if delete_all:
            self.connect_collection.delete_many(where_condition)
        else:
            self.connect_collection.delete_one(where_condition)
