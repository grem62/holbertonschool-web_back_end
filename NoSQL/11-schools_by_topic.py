#!/usr/bin/env python3
"""
task11
"""


def schools_by_topic(mongo_collection, topic):
    "Write a Python function that returns the list of school"
    return list(mongo_collection.find({"topic": topic}))
