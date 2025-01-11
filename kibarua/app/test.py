from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.kibarua_db

# Insert test data
db.users.insert_one({'name': 'test_user', 'password': 'test_password'})

# Verify data
print(list(db.users.find()))
