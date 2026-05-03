# 🚀 Python OOP Learning Journey

**Một hành trình học OOP trong Python từ cơ bản đến nâng cao** - Từ Encapsulation → Inheritance → Polymorphism → Abstract Classes

---

## 📌 Tổng quan

Repository này là một chương trình học lập trình hướng đối tượng (OOP) trong Python, được tổ chức thành **6 ngày học** + **phần luyện tập (On_Tap)**, với sự phát triển dần dần:

```
Day 1 → Day 2 → Day 3 → Day 4 → Day 5 → Day 6 → On_Tap (Tổng hợp)
```

### ✨ Điểm nhấn

- ✅ **Encapsulation**: Sử dụng `@property` để bảo vệ dữ liệu
- ✅ **Inheritance**: Kế thừa từ class cha, override method
- ✅ **Polymorphism**: Cùng interface, hành vi khác nhau
- ✅ **Abstract Classes**: Định nghĩa contract cho class con
- ✅ **Template Method Pattern**: Kiểm soát flow trong class cha
- ✅ **Business Logic**: Validation, state management, error handling

---

## 📚 Cấu trúc Dự Án

```
📁 Python_Journey/
│
├── 📁 01_Basics/                    # ✏️ Nền tảng Python (6 ngày)
│   ├── day_1.py                    # Class cơ bản: Product
│   ├── day_2.py                    # Encapsulation: @property, validation
│   ├── day_3.py                    # Áp dụng: Book model
│   ├── day_4.py                    # Inheritance: Account → SavingsAccount, CheckingAccount
│   ├── day_5.py                    # Inheritance nâng cao: BankAccount + Template Method
│   └── day_6.py                    # Abstract Class + Polymorphism: PhuongTienThue
│
├── 📁 02_OOP_Basics/                # 🎓 OOP Cấp 1: Khái niệm cơ bản
│   ├── 01_sinh_vien.py             # Class Student: Encapsulation cơ bản
│   ├── 02_hinh_chu_nhat.py         # Rectangle: @property, tính toán
│   ├── 03_nhanvien.py              # Employee: Attributes & Methods
│   └── 04_xe_may.py                # Motorcycle: Class design
│
├── 📁 03_OOP_Intermediate/          # 📈 OOP Cấp 2: Kỹ thuật nâng cao
│   ├── 01_quan_ly_cua_hang_sach.py # BookStore: Encapsulation + Validation
│   ├── 02_quan_ly_thu_vien.py      # Library Management: Inheritance
│   ├── 03_quan_ly_luong.py         # Salary Management: Polymorphism
│   └── 04_bai_tap_doan_so.py       # Number Range: Abstract Class
│
├── 📁 04_Practice/                  # 🔥 Ôn tập & Thực hành tổng hợp
│   ├── 01_he_thong_phuong_tien.py  # Transport System: Multiple Inheritance
│   ├── 02_ket_thua_va_dong_goi.py  # Inheritance & Encapsulation: Combined
│   ├── 03_ngan_hang_ke_thua.py     # Bank System: Complex Inheritance
│   ├── 04_quan_ly_nhan_vien_crud.py # Employee CRUD: Full Management System
│   └── 05_xe_dap.py                # Bicycle System: OOP Design Pattern
│
├── 📁 05_Level_Up/                  # 🎯 Nâng cao: Project thực tế
│   ├── main.py                      # Application entry point
│   ├── test_seed.py                 # Seed data cho testing
│   ├── data/
│   │   └── student.json             # Database JSON
│   ├── logs/                        # Application logs
│   ├── models/
│   │   └── student.py               # Student data model
│   ├── repository/
│   │   └── student_repository.py    # Data access layer (DAO pattern)
│   ├── services/
│   │   └── student_service.py       # Business logic layer
│   └── utils/
│       └── logger.py                # Logging utility
│
├── 📁 06_FastAPI_Backend/           # 🚀 Backend API Development
│   ├── 01_Basics_API/
│   │   ├── CRUD-Customers/
│   │   │   └── main.py              # CRUD operations example
│   │   └── Learning-FastAPI/
│   │       ├── main.py              # FastAPI basics
│   │       ├── README.md
│   │       └── requirements.txt
│   ├── 02_CRUD/                     # Advanced CRUD operations
│   ├── 03_Validation/               # Input validation
│   ├── 04_Auth/                     # Authentication & Authorization
│   └── 05_Project_CRM/              # CRM project
│
└── README.md                        # 📖 Hướng dẫn này
```

---

## 🎯 Lộ trình học chi tiết

### **Day 1: Class Cơ Bản** 📌
**File**: `day_1.py`

**Nội dung chính**:
- Tạo class `Product`
- Khởi tạo object với `__init__`
- Định nghĩa instance attributes
- Tạo method cơ bản: `display_info()`, `sell()`

**Concept**:
```python
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self._price = price           # chuẩn bị encapsulation
        self._stock_quantity = stock_quantity

    def sell(self, quantity):
        # Xử lý bán hàng
        pass
```

**Kết quả học**:
- Hiểu cách tạo class & object
- Nắm được `__init__` method
- Biết cách gọi method trên object

---

### **Day 2: Encapsulation & Validation** 🔒
**File**: `day_2.py`

**Nội dung chính**:
- Sử dụng `@property` để bảo vệ dữ liệu
- Tạo setter để validate dữ liệu
- Implement `update_stock()` method
- Double-check validation

**Concept**:
```python
class Product:
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Giá không hợp lệ!")
        self._price = value

    def update_stock(self, quantity_change):
        new_quantity = self.stock_quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Không đủ hàng")
        self.stock_quantity = new_quantity
```

**Kết quả học**:
- Hiểu Encapsulation (đóng gói dữ liệu)
- Biết cách validate dữ liệu
- Nắm được business logic + data protection

---

### **Day 3: Áp Dụng & Consolidation** 📖
**File**: `day_3.py`

**Nội dung chính**:
- Tạo class `Book` (tương tự `Product`)
- Validate loại dữ liệu: `isinstance(value, int)`
- Implement `add_pages()` & `remove_pages()`
- Tạo `display_book_info()` để hiển thị

**Concept**:
```python
class Book:
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Số trang phải > 0")
        self._page_count = value

    def add_pages(self, extra_pages):
        self.page_count = self.page_count + extra_pages
```

**Kết quả học**:
- Consoliate kiến thức Day 1-2
- Hiểu cách design một domain model
- Biết validate kiểu dữ liệu và giá trị

---

### **Day 4: Inheritance Cơ Bản** 🏦
**File**: `day_4.py`

**Nội dung chính**:
- Tạo base class `Account`
- Tạo class con: `SavingsAccount` (tính lãi)
- Tạo class con: `CheckingAccount` (rút tiền có phí)
- Sử dụng `super().__init__()` gọi constructor cha

**Concept**:
```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_monthly_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

class CheckingAccount(Account):
    def withdraw(self, amount):
        total_withdraw = amount + 5000  # phí rút
        super().withdraw(total_withdraw)
```

**Kết quả học**:
- Hiểu Inheritance (kế thừa)
- Biết cách gọi `super()`
- Nắm được override method
- Thấy Polymorphism (cùng method, hành vi khác)

---

### **Day 5: Inheritance Nâng Cao & Template Method** 🏦
**File**: `day_5.py`

**Nội dung chính**:
- Cải tiến base class `BankAccount`
- Implement Template Method Pattern: `monthly_process()`
- Override `monthly_process()` trong class con
- Thêm OVERDRAFT_LIMIT trong `CheckingAccount`

**Concept**:
```python
class BankAccount:
    def monthly_process(self):
        # Template method - cái này có thể bị override
        print("Xử lý cuối tháng (mặc định)")

class SavingsAccount(BankAccount):
    def monthly_process(self):
        # Override - cứ vào đây thay vì class cha
        print("Tính lãi")
        self.add_interest()

class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = -500  # Class variable

    def withdraw(self, amount):
        new_balance = self._balance - amount
        if new_balance < self.OVERDRAFT_LIMIT:
            print("Vượt hạn mức thấu chi")
            return
        self._balance = new_balance
```

**Kết quả học**:
- Hiểu Template Method Pattern
- Nắm cách sử dụng class variable
- Biết thiết kế flow kiểm soát bởi class cha
- Thấy polymorphism trong thực tế

---

### **Day 6: Abstract Classes & Full Polymorphism** 🚲
**File**: `day_6.py`

**Nội dung chính**:
- Tạo Abstract Base Class (ABC): `PhuongTienThue`
- Định nghĩa abstract method: `tinh_chi_phi_phu()`
- Implement 3 class con: `XeDapThuong`, `XeDapDien`, `XeDapDoi`
- Sử dụng loop để gọi cùng interface → hành vi khác nhau

**Concept**:
```python
from abc import ABC, abstractmethod

class PhuongTienThue(ABC):
    @abstractmethod
    def tinh_chi_phi_phu(self):
        pass

    def tinh_tong_tien(self):
        tien_co_ban = self.gia_co_ban_ngay * self.so_ngay_thue
        chi_phi_phu = self.tinh_chi_phi_phu()  # gọi method con
        return tien_co_ban + chi_phi_phu

class XeDapThuong(PhuongTienThue):
    def tinh_chi_phi_phu(self):
        return 5000

class XeDapDien(PhuongTienThue):
    def tinh_chi_phi_phu(self):
        return 20000 * self.so_ngay_thue

# Polymorphism tại đây:
danh_sach_xe = [XeDapThuong(...), XeDapDien(...), XeDapDoi(...)]
for xe in danh_sach_xe:
    print(xe.tinh_tong_tien())  # ← mỗi xe xử lý khác nhau!
```

**Kết quả học**:
- Hiểu Abstract Base Class (ABC)
- Biết định nghĩa contract cho class con
- Nắm full Polymorphism concept
- Thấy sức mạnh OOP trong design

---

## 🎯 Level 5: Kiến trúc Project Thực Tế (05_Level_Up)

**Mục đích**: Ứng dụng OOP vào một dự án thực tế với kiến trúc lớp

### Cấu trúc thư mục

```
05_Level_Up/
├── main.py                          # Entry point của ứng dụng
├── test_seed.py                     # Dữ liệu mẫu cho testing
├── data/
│   └── student.json                 # Database (JSON format)
├── models/
│   └── student.py                   # Model Student (data class)
├── repository/
│   └── student_repository.py        # DAO pattern - xử lý DB
├── services/
│   └── student_service.py           # Business logic layer
└── utils/
    └── logger.py                    # Logging utility
```

### Kiến trúc 3-Layer

1. **Models** (`student.py`): Định nghĩa cấu trúc dữ liệu
   - Student class với validation

2. **Repository** (`student_repository.py`): Data Access Object (DAO)
   - `create()`, `read()`, `update()`, `delete()`
   - Quản lý JSON file

3. **Services** (`student_service.py`): Business Logic
   - Xử lý logic phức tạp
   - Validation dữ liệu

4. **Main** (`main.py`): Presentation Layer
   - Menu CLI
   - Gọi service methods

### Concepts Được Áp Dụng

- ✅ Encapsulation: Private attributes với @property
- ✅ Repository Pattern: Tách database từ business logic
- ✅ Service Layer: Xử lý validation & business rules
- ✅ Logging: Ghi log hoạt động
- ✅ JSON File I/O: Lưu trữ dữ liệu

---

## 🚀 Level 6: FastAPI Backend (06_FastAPI_Backend)

**Mục đích**: Từ OOP lên Backend Web Development

### 📚 01_Basics_API/

#### Learning-FastAPI/
- Học cơ bản FastAPI
- Tạo route cơ bản
- Request/Response handling

**Ví dụ**:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

#### CRUD-Customers/
- CRUD operations (Create, Read, Update, Delete)
- In-memory database
- API endpoints cho Customer management

### 📊 02_CRUD/
- Advanced CRUD operations
- Database integration
- Error handling

### ✅ 03_Validation/
- Pydantic models
- Input validation
- Type checking

### 🔐 04_Auth/
- Authentication (JWT)
- Authorization
- User management

### 🎯 05_Project_CRM/
- Customer Relationship Management system
- Full-stack application
- Integrates tất cả concepts trước

---

## 📝 Phần Luyện Tập: On_Tap

**Mục đích**: Tổng hợp & ứng dụng toàn bộ kiến thức từ Day 1-6

### **test.py**
- Luyện tập các model cơ bản

### **xe_dap.py**
- Ứng dụng Day 6 concept

### **ngan_hang_ke_thua.py**
- Ứng dụng Day 4-5 concept

### **ket_thua_va_dong_goi.py**
- Kết hợp Inheritance + Encapsulation

### **he_thong_phuong_tien.py**
- Tổng hợp tất cả kiến thức

---

## 📝 Phần Bài Tập: OOP_BaiTap

**Mục đích**: Bài tập thực hành OOP theo cấp độ từ cơ bản đến trung bình

### **Cap1_CoBan/** (Cấp 1: Cơ bản)
- **cap1_01_sinh_vien.py**: Quản lý thông tin sinh viên
- **cap1_02_hinh_chu_nhat.py**: Tính toán hình chữ nhật
- **cap1_03_nhanvien.py**: Quản lý nhân viên
- **cap1_03_xemay.py**: Quản lý xe máy

### **Cap2_TrungBinh/** (Cấp 2: Trung bình)
- **cap2_01_quan_ly_cua_hang_sach.py**: Quản lý cửa hàng sách
- **cap2_02_quan_ly_thu_vien.py**: Quản lý thư viện
- **cap2_03_quan_ly_luong.py**: Quản lý lương nhân viên
- **cap2_04_bai_tap_doan_so.py**: Bài tập đoạn số

---

## 🎓 Những Concept Được Học

| Mục | Concept | File/Folder |
|------|---------|------|
| 1 | Class & Object | day_1.py |
| 2 | Encapsulation | day_2.py |
| 3 | Consolidation | day_3.py |
| 4 | Inheritance | day_4.py |
| 5 | Template Method | day_5.py |
| 6 | Polymorphism & ABC | day_6.py |
| Ôn | Tổng hợp OOP | 04_Practice/ |
| 5️⃣ | Architecture Pattern | 05_Level_Up/ |
| 6️⃣ | FastAPI Backend | 06_FastAPI_Backend/ |

---

## 💡 Cách Học

### **Cách 1: Follow từng ngày (Basics → OOP)**
```bash
# Day 1-6
python 01_Basics/day_1.py
python 01_Basics/day_2.py
# ... tiếp tục đến Day 6
python 01_Basics/day_6.py
```

### **Cách 2: Luyện tập bài tập theo cấp độ**
```bash
cd 02_OOP_Basics
python 01_sinh_vien.py
python 02_hinh_chu_nhat.py

cd ../03_OOP_Intermediate
python 01_quan_ly_cua_hang_sach.py
```

### **Cách 3: Ôn luyện toàn bộ OOP**
```bash
cd 04_Practice
python 01_he_thong_phuong_tien.py
python 04_quan_ly_nhan_vien_crud.py
```

### **Cách 4: Kiến trúc thực tế (Level 5)**
```bash
cd 05_Level_Up
python main.py  # Chạy ứng dụng student management
python test_seed.py  # Tạo dữ liệu mẫu
```

### **Cách 5: Backend Development (Level 6)**
```bash
cd 06_FastAPI_Backend/01_Basics_API/Learning-FastAPI
pip install -r requirements.txt
uvicorn main:app --reload
```

### **Cách 6: Hoàn chỉnh từng level**
```
Level 1 (Day 1-3): Basics + Encapsulation
    ↓
Level 2 (Day 4-6): Inheritance + Polymorphism
    ↓
Level 3 (02_OOP_Basics): OOP Basics practice
    ↓
Level 4 (03_OOP_Intermediate): OOP Intermediate practice
    ↓
Level 5 (04_Practice): OOP Consolidation
    ↓
Level 6 (05_Level_Up): Real-world architecture
    ↓
Level 7 (06_FastAPI_Backend): Backend API Development
```

---

## 📚 Chi tiết từng Level

| Level | Tên | Mục tiêu | Concepts |
|-------|-----|----------|----------|
| **1** | Basics | Nắm vững Python cơ bản | Class, Object, Attributes |
| **2** | OOP Basics | Hiểu Encapsulation | @property, Validation |
| **3** | OOP Intermediate | Inheritance + Polymorphism | Super(), Override |
| **4** | Practice | Tổng hợp toàn bộ | Combined Patterns |
| **5** | Level Up | Kiến trúc thực tế | 3-Layer Architecture, Repository Pattern |
| **6** | FastAPI | Backend Development | REST API, CRUD, Authentication |

---

## 🎯 Key Takeaways

### ✅ Encapsulation (Đóng gói)
```python
# Ẩn dữ liệu bên trong, qua @property + setter
@property
def price(self):
    return self._price

@price.setter
def price(self, value):
    if value < 0:
        raise ValueError("Invalid!")
    self._price = value
```

### ✅ Inheritance (Kế thừa)
```python
# Class con kế thừa từ class cha
class CheckingAccount(BankAccount):
    def __init__(self, ...):
        super().__init__(...)  # gọi constructor cha
```

### ✅ Polymorphism (Đa hình)
```python
# Cùng interface → hành vi khác nhau
for xe in [XeDapThuong(), XeDapDien(), XeDapDoi()]:
    print(xe.tinh_tong_tien())  # ← mỗi class override khác nhau
```

### ✅ Abstract Classes (Lớp trừu tượng)
```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def method(self):
        pass

# ❌ Base() → TypeError
# ✅ class Child(Base): pass → OK
```

---

## 🔥 Best Practices Được Áp Dụng

1. **Validation đầu vào**: Validate ở `__init__` và setter
2. **Double-check**: Gán qua setter để đảm bảo consistency
3. **Private attributes**: Dùng `_` prefix cho dữ liệu cần ẩn
4. **Method naming**: `get_`, `set_`, `add_`, `remove_`
5. **Error messages**: Rõ ràng, giúp debug dễ hơn
6. **Step-by-step comments**: Giúp hiểu flow của code
7. **Separation of concerns**: Mỗi method một trách nhiệm

---

## 🚀 Mở Rộng

Sau khi hoàn thành, bạn có thể:
- ✏️ Thêm các class mới (Student, Employee, etc.)
- 📚 Kết hợp với database (SQLite, PostgreSQL)
- 🌐 Xây dựng API (Flask, FastAPI)
- 🧪 Viết unit tests (pytest)
- 📦 Đóng gói thành package (setuptools)

---

## 📖 Tài Liệu Tham Khảo

- Python Official Docs: https://docs.python.org/3/
- OOP Concepts: https://en.wikipedia.org/wiki/Object-oriented_programming
- Design Patterns: https://refactoring.guru/design-patterns/python

---

**Happy Learning! 🎉**
