from pymongo import MongoClient
import json

client = MongoClient("mongodb://mongo:27017")

db = client.test
employees = db.employees


def init_doc():
    if employees.count_documents({}) == 0:
        with open("employee_data_advanced.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        employees.insert_many(data)