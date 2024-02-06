from typing import Optional
from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime

class PatientCreate(BaseModel):
    dni: str = Field(..., description="User's DNI")

class PatientOut(BaseModel):
    dni: str

class PatientOutResponse(BaseModel):
    status: bool
    PatientOut: Optional[PatientOut]