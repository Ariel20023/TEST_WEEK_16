from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.test
employees = db.employees


def get_engineering_high_salary_employees ():
    return list(employees.find({"job_role.department":"Engineering","salary":{"$gt":65000}},
                                {"_id": 0,
                                "employee_id":1,
                                "name":1,
                                "salary":1}))



def get_employees_by_age_and_role():
    return list(employees.find({"age":{"$gte":30 ,"$lte":45},"job_role.title":{"$in":["Specialist","Engineer"]}}
                               ,{"_id": 0}))



def get_top_seniority_employees_excluding_hr():
    return list(employees.find({"job_role.department":{"$ne":"HR"}},
                               {"_id": 0}).sort("years_at_company",-1).limit(7))



def get_employees_by_age_or_seniority():
    return list(employees.find({"$or":[{"age":{"$gt":50}},{"years_at_company":{"$lt":3}}]}
                                ,{"_id": 0,
                                "employee_id":1,
                                "name":1,
                                "age":1,
                                "years_at_company":1}))



def get_managers_excluding_departments():
    return list(employees.find({"job_role.title":"Manager","job_role.department":{"$nin":["Sales","Marketing"]}}
                               ,{"_id": 0}))




def get_employees_by_lastname_and_age():
    return list(employees.find({"age":{"$lt":35},"$or":[{"name":{"$regex": "Nelson$"}},{"name":{"$regex": "Wright$"}}]}
                                ,{"_id": 0,
                                "name":1,
                                "age":1,
                                "job_role.department":1}))





















