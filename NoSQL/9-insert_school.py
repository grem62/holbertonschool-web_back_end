#!/usr/bin/env python3
"""
task9
"""


def insert_school(mongo_collection, **kwargs):
    "insert new objet with kwargs"
    result = mongo_collection.insert_one(kwargs)
    return result._id
