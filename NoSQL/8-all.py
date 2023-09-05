#!/usr/bin/env python3
"""
list all file in collection with python
"""
import pymongo

def list_all(mongo_collection):
    "list all file in collection with python"
    return list(mongo_collection.find())
