#!/usr/bin/env python3
"""
task10
"""


def update_topics(mongo_collection, name, topics):
    "Write a Python function that change all topic of a school"
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
