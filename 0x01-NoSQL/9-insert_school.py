#!/usr/bin/env python3
"""
implements a function that performs insertion on a mongodb database collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs.
    Args:
        mongo_collection - a collection object.
        kwargs - key worded args.
    Return:
        inserted ids.
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
