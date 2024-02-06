from typing import Optional
from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime

class UserCreate(BaseModel):
    dni: str = Field(..., description="User's DNI")
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=8, max_length=24, description="User's password")
    name: str = Field(..., description="User's first name")
    lastname: str = Field(..., description="User's last name")
    birthdate: str = Field(..., description="User's birthdate (YYYY-MM-DD)")  
    phone: str = Field(..., description="User's phone number")
    rol_id: int = Field(..., description="ID of the user's role") 