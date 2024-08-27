#!/usr/bin/env python3
"""
implements a function that updates a document based on it's name.
"""
def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name.
    Args:
        mongo_collection - a collection object.
        name (str) - a school name to update.
        topics (list) - list of topics approached in the school.
    """
    mongo_collection.update_one({ "name": name }, {"$set": { "topics": topics } })
