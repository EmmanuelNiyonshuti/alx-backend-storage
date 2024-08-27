#!/usr/bin/env python3

"""
implements a function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection.
    Args:
        mongo_collection - pymongo collection object.
    Return:
        a list of all documents in the collection or
        an empty list otherwise.
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    return [doc for doc in mongo_collection.find()]
