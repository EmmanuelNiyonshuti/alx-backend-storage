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
        a inserted ids.
    """
    doc = [{k : v} for k, v in kwargs.items()]
    res = mongo_collection.insert_many(doc)
    return res.inserted_ids

