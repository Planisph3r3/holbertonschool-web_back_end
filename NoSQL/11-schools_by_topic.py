#!/usr/bin/env python3
"""Working with pymongo module"""


def schools_by_topic(mongo_collection, topic):
    """A function that returns the list of school having a specific topic"""
    specific_listing = mongo_collection.find({"topic":topic})
    return specific_listing