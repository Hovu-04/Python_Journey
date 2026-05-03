from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from unidecode import unidecode

app = FastAPI(title="API quản lý khách hàng")


class Customer(BaseModel):
    name: str = Field(..., min_length=2)
    phone: str
    budget: float = Field(..., gt=0)


class CustomerResponse(Customer):
    id: int


customers = [
    {"id": 1, "name": "Anh A", "phone": "0903", "budget": 120000000},
    {"id": 2, "name": "Anh B", "phone": "0703", "budget": 300000000},
]


@app.get("/customers", response_model=list[CustomerResponse])
def get_customer(name: str | None = None, min_budget: float | None = None):
    result = customers.copy()
    if name:
        keyword = unidecode(name.lower())
        result = [c for c in result if keyword in unidecode(c["name"].lower())]
    if min_budget is not None:
        result = [c for c in result if c["budget"] >= min_budget]
    return result


@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer_by_id(customer_id: int):
    for c in customers:
        if c["id"] == customer_id:
            return c
    raise HTTPException(status_code=404, detail="Customer not found")


@app.post(
    "/customers", status_code=status.HTTP_201_CREATED, response_model=CustomerResponse
)
def create_customer(customer: Customer):
    new_customer = {
        "id": len(customers) + 1,
        "name": customer.name,
        "phone": customer.phone,
        "budget": customer.budget,
    }
    customers.append(new_customer)
    return new_customer


@app.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer: Customer):
    for c in customers:
        if c["id"] == customer_id:
            c.update(customer.model_dump())
            return c
    raise HTTPException(status_code=404, detail="Customer not found!")


@app.delete("/customers/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int):
    for i, c in enumerate(customers):
        if c["id"] == customer_id:
            customers.pop(i)
            return
    raise HTTPException(status_code=404, detail="Customer not found")
