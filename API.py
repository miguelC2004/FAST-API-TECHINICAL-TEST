from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Sample data for demonstration purposes
users = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "pass123",
        "country": "USA"
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "password": "pass456",
        "country": "Canada"
    },
    # Add more sample data as needed
]


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    country: str


class Address(BaseModel):
    city: str
    postal_code: str


class UserWithAddress(User):
    addresses: List[Address] = []


@app.post("/users/", response_model=UserWithAddress)
def create_user(user: UserWithAddress):
    user_data = user.dict()
    user_data["id"] = len(users) + 1
    users.append(user_data)
    return user_data


@app.get("/users/", response_model=List[UserWithAddress])
def get_users_by_country(country: str):
    result = [user for user in users if user["country"].lower() == country.lower()]
    if not result:
        raise HTTPException(status_code=404, detail="No users found for the given country.")
    return result
