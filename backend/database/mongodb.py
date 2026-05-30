import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class SalesCollectionProxy:
    def __init__(self):
        self._collection = None

    def _get_collection(self):
        if self._collection is None:
            mongo_uri = os.getenv("MONGO_URI")
            if not mongo_uri:
                raise RuntimeError("MONGO_URI environment variable is not configured")

            db_name = os.getenv("MONGO_DB_NAME", "smart_retail_db")
            collection_name = os.getenv("MONGO_COLLECTION", "sales")

            client = MongoClient(mongo_uri)
            self._collection = client[db_name][collection_name]

        return self._collection

    def __getattr__(self, name):
        return getattr(self._get_collection(), name)


sales_collection = SalesCollectionProxy()
