#!/usr/bin/env python3
"""Working with pymongo module"""


def list_all(mongo_collection):
    """A function that lists all documents in a collection"""

    documents = mongo_collection.find()

    if not documents:
        return []
    else:
        return [document for document in documents]