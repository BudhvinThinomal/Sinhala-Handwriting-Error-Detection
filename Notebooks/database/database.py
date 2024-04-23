from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://budhvint:Lp7IOv7XoAFJhwHo@cluster0.dzdoqtg.mongodb.net/?retryWrites=true&w=majority"
)

db = client.akuruMithuru

collection_name = db["users"]
