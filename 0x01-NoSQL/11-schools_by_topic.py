#!/usr/bin/env python3
""" implements a function schools_by_topic. """


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic.
    Args:
        mongo_collection - pymongo collection object.
        topic (str) - topic to be searched.
    Return:
        list of school.
    """
    return mongo_collection.find({"topics": topic})
