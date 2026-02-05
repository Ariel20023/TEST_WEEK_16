from fastapi import FastAPI
from dal import *
from connection import *


app = FastAPI()


@app.on_event("startup")
def startup_event():
    init_doc()




@app.get("/employees/engineering/high-salary")
def employees_engineering_high_salary():
    return get_engineering_high_salary_employees()



@app.get("/employees/by-age-and-role")
def employees_by_age_and_role():
    return get_employees_by_age_and_role()


@app.get("/employees/top_seniority")
def employees_top_seniority():
    return get_top_seniority_employees_excluding_hr()


@app.get("/employees/age-or-seniority")
def employees_age_or_seniority():
    return get_employees_by_age_or_seniority()


@app.get("/employees/managers/excluding-departments")
def employees_managers_excluding_departments():
    return get_managers_excluding_departments()


@app.get("/employees/by-lastname-and-age")
def employees_by_lastname_and_age():
    return get_employees_by_lastname_and_age()







