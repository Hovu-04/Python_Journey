# 🚀 FastAPI – Basics (Day 1 → Day 4)

## 📌 Mục tiêu

- Hiểu HTTP & REST API
- Tạo API bằng FastAPI
- Làm việc với:
  - Path Operation
  - Response (JSON)
  - Path Parameter
  - Query Parameter
  - Request Body
  - Pydantic Model
  - Validation dữ liệu

---

## ⚙️ Cài đặt

```bash
pip install fastapi uvicorn
```

Hoặc:

```bash
pip install -r requirements.txt
```

---

## ▶️ Chạy server

```bash
uvicorn main:app --reload
```

👉 Truy cập:

- API: http://127.0.0.1:8000  
- Docs: http://127.0.0.1:8000/docs  

---

# 📚 Danh sách API

## 🔹 1. Root

```http
GET /
```

```json
{"msg": "API is running"}
```

---

## 🔹 2. Hello

```http
GET /hello
```

```json
{"msg": "Xin chào Vũ!"}
```

---

## 🔹 3. Students (list + query)

```http
GET /students?name=Nguyễn
```

```json
[
  {"id": 1, "name": "Nguyễn Văn A", "age": 20},
  {"id": 2, "name": "Nguyễn Văn B", "age": 22}
]
```

👉 Query dùng để lọc danh sách

---

## 🔹 4. Student by ID

```http
GET /students/{student_id}
```

```json
{"id": 1, "name": "Nguyễn Văn A", "age": 20}
```

---

## 🔹 5. Tạo Student (POST)

```http
POST /students
```

```json
{
  "name": "Nguyễn Văn C",
  "age": 25
}
```

```json
{
  "msg": "student created",
  "data": {
    "id": 3,
    "name": "Nguyễn Văn C",
    "age": 25
  }
}
```

👉 Status: `201 Created`

---

## 🔹 6. Products

```http
GET /products
```

```json
[
  {"id": 1, "name": "Đất nền", "price": 1000000000},
  {"id": 2, "name": "Nhà phố", "price": 3000000000}
]
```

---

## 🔹 7. Product by ID + Query

```http
GET /products/{product_id}?detail=true
```

```json
{
  "id": 1,
  "name": "Đất nền",
  "price": 1000000000,
  "description": "Thông tin chi tiết sản phẩm"
}
```

---

## 🔹 8. Tạo Product (POST)

```http
POST /products
```

```json
{
  "name": "Shophouse",
  "price": 5000000000
}
```

```json
{
  "msg": "product created",
  "data": {
    "id": 3,
    "name": "Shophouse",
    "price": 5000000000
  }
}
```

👉 Status: `201 Created`

---

## 🔹 9. Me

```http
GET /me
```

```json
{
  "name": "Vũ",
  "goal": "Giỏi backend + kiếm tiền"
}
```

---

## 🔹 10. Status

```http
GET /status
```

```json
{"status": "running"}
```

---

# 🧠 KIẾN THỨC ĐÃ HỌC

## 1. HTTP & REST API

- HTTP = giao thức client ↔ server  
- REST API = thiết kế API theo resource  

| Method | Ý nghĩa     |
|--------|------------|
| GET    | Lấy dữ liệu |
| POST   | Tạo mới     |
| PUT    | Cập nhật    |
| DELETE | Xóa         |

---

## 2. Path Operation

```python
@app.get("/students")
```

👉 Gồm:
- Method
- Path
- Function

---

## 3. Response (JSON)

```python
return {"msg": "ok"}
```

👉 FastAPI tự convert thành JSON

---

## 4. Path Parameter

```python
@app.get("/students/{student_id}")
```

👉 Lấy 1 resource

---

## 5. Query Parameter

```python
def get_students(name: str = None)
```

👉 Lọc dữ liệu

---

## ⚔️ So sánh

| Path           | Query            |
|----------------|------------------|
| /students/1    | /students?page=1 |
| 1 resource     | danh sách        |

---

## 6. Request Body

```json
{
  "name": "Vũ",
  "age": 20
}
```

---

## 7. Pydantic Model

```python
class Student(BaseModel):
    name: str
    age: int
```

👉 Validate dữ liệu

---

## 8. Validation

Sai dữ liệu:

```json
{
  "name": "A",
  "age": "hai mươi"
}
```

→ lỗi:

```
422 Unprocessable Entity
```

---

# ⚠️ Lưu ý

- Resource dùng số nhiều (`/students`, `/products`)
- Không dùng query để lấy 1 object
- GET không thay đổi dữ liệu
- POST dùng để tạo dữ liệu
- `/docs` dùng để test API

---

# 🎯 Kết quả

Sau Day 1 → Day 4:

- Viết được API GET & POST
- Hiểu Path + Query + Body
- Validate dữ liệu bằng Pydantic
- Hiểu cách API hoạt động

---

# 🚀 Hướng tiếp

- Day 5: CRUD API
- Day 6: Tách router/service
- Day 7+: Database

---

# 💥 Ghi nhớ

Path = định danh  
Query = điều kiện  
Body = dữ liệu  
Return = JSON  
Type = validationF