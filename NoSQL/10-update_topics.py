#!/usr/bin/env python3
"""Working with pymongo module"""


def update_topics(mongo_collection, name, topics):
    """A function that changes all topics of a school document based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})