#!/usr/bin/env python3
"""
task10
"""

def update_topics(mongo_collection, name, topics):
    "Write a Python function that changes all topics of a school document based on the name:"
    return mongo_collection.updatemany({name : name}, { "$set" :{topics : topics}})