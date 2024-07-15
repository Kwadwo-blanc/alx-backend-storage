#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

def log_stats():
    """Function that prints stats about Nginx logs from MongoDB"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Get the top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(collection.aggregate(pipeline))

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
