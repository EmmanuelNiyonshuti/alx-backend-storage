#!/usr/bin/env python3
"""This script provides statistics about Nginx logs in MongoDB."""

from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017")
db = client.logs
collection = db.nginx

# Get and print the number of documents in the logs collection
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Define HTTP methods to check
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Get and print the number of documents for each HTTP method
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tMethod {method}: {count}")

# Get and print the number of documents
# with method 'GET' and path '/status'
stats_count = collection.count_documents(
    {"method": methods[0], "path": "/status"}
)
print(f"{stats_count} status check")


if __name__ == "__main__":
    main()

