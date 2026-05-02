from fastapi import FastAPI, status
from pydantic import BaseModel, Field
from unidecode import unidecode

app = FastAPI(title="Welcome FastAPI")


# =========================
# Pydantic Models
# =========================


class Student(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0)


class Product(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)


# =========================
# Fake Data
# =========================

students = [
    {"id": 1, "name": "Nguyễn Văn A", "age": 20},
    {"id": 2, "name": "Nguyễn Văn B", "age": 22},
]

products = [
    {"id": 1, "name": "Đất nền", "price": 1000000000},
    {"id": 2, "name": "Nhà phố", "price": 3000000000},
]


# =========================
# Basic APIs
# =========================


@app.get("/")
def root():
    return {"msg": "API is running"}


@app.get("/hello")
def hello():
    return {"msg": "Xin chào Vũ!"}


@app.get("/me")
def get_me():
    return {"name": "Vũ", "goal": "Giỏi backend + kiếm tiền"}


@app.get("/status")
def get_status():
    return {"status": "running"}


# =========================
# Student APIs
# =========================


@app.get("/students")
def get_students(name: str | None = None):
    if name:
        keyword = unidecode(name.lower())
        return [
            student
            for student in students
            if keyword in unidecode(student["name"].lower())
        ]
    return students


@app.get("/students/{students_id}")
def get_students_by_id(studens_id: int):
    for student in students:
        if student["id"] == studens_id:
            return student
    return {"msg": "Student not found!"}


@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    new_student = {"id": len(students) + 1, "name": student.name, "age": student.age}
    students.append(new_student)

    return {"msg": "created student", "data": new_student}


# =========================
# Product APIs
# =========================


@app.get("/products")
def get_products(name: str | None = None):
    if name:
        keyword = unidecode(name.lower())
        return [
            product
            for product in products
            if keyword in unidecode(product["name"].lower())
        ]
    return products


@app.get("/products/{products_id}")
def get_product_by_id(products_id: int):
    for product in products:
        if product["id"] == products_id:
            return product
    return {"msg": "Product not found!"}


@app.post("/products", status_code=status.HTTP_201_CREATED)
def created_producs(product: Product):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price,
    }

    products.append(new_product)
    return {"msg": "created products", "data": new_product}
