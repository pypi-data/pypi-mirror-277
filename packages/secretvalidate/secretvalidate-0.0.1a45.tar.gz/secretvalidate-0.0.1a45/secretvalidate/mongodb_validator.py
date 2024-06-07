# MongoDB connections using PyMongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

def validate_mongodb(connection_string, response):
    """Validate MongoDB connection string."""
    try:
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        # Attempt to retrieve server information to force a connection check
        server_info = client.server_info()
        if response:
            return "Active"
        else:
            return server_info       

        client.close()
    except (ConnectionError, ConnectionFailure) as e:
        if response:
            return "Inactive"
        else:
            return f"MongoDB connection string validation failed: {e}"
