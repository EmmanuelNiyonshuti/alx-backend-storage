#!/usr/bin/env python3
"""This script provides statistics about Nginx logs in MongoDB."""

from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Get and print the number of documents in the logs collection
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # Define HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Get and print the number of documents for each HTTP method
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Get and print the number of documents
    # with method 'GET' and path '/status'
    stats_count = collection.count_documents(
        {"method": methods[0], "path": "/status"}
    )
    print("{} status check".format(stats_count))
