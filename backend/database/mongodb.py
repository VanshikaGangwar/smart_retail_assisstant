from pymongo import MongoClient

MONGO_URI = "mongodb+srv://vanshikagangwar98_db_user:g9i3TQpBir6LErA9@cluster1.jhamd2u.mongodb.net/?appName=Cluster1"

client = MongoClient(MONGO_URI)

db = client["smart_retail_db"]

sales_collection = db["sales"]