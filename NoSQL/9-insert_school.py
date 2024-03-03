#!/usr/bin/env python3
"""Working with pymongo module"""


def insert_school(mongo_collection, **kwargs):
    """A function that inserts a new document
    in a collection based on kwargs"""

    documents_insterted = mongo_collection.insert_one(kwargs)
    return documents_insterted.inserted_id