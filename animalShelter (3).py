#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 01:38:01 2023

@author: crystalberkha_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
     """ CRUD operations for Animal collection in MongoDB """
     def __init__(self, USER, PASS):
         USER = "aacuser"
         PASS = "password"
         HOST = 'nv-desktop-services.apporto.com'
         PORT = 31745
         DB = 'AAC'
         COL = 'animals'
         self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
         self.database = self.client['%s' % (DB)]
         self.collection = self.database['%s' % (COL)]
         
    #Complete this create method to implement the C in CRUD
     def create(self, data):
         if data is not None:
             self.database.animals.insert_one(data) #data should be dictionary
             print("True")
         else:
             raise Exception("Data cannot be created")
             print("False")
         
     #Create method to implement the R in CRUD
     def read(self, data):
         if data is not None: 
             return self.database.animals.find(data, {'_id': 0})
         else:
             raise Exception("Unable to find data")
        
    #Create method to implement the U in CRUD
     def update(self, data, updatedData):
        if data is not None:
            updated = self.database.animals.update_one(data, {"$set": updatedData})
            print("Updated")
        else:
            raise Exception("Unable to update")
        return updated.raw_result
    
    #Create method to implement the D in CRUD
     def delete(self, data):
         if data is not None:
             deleted = self.database.animals.delete_one(data)
         else:
             raise Exception("Unable to delete")
         return deleted.raw_result
            
            
            
            

