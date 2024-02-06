from typing import List
from pydantic import BaseModel, Field , EmailStr
from datetime import datetime
from datetime import time
from datetime import date


class CaregiverCreate(BaseModel):
    dni:str = Field(..., description="Caregiver dni")
    skill: float = Field(..., description="Caregiver Demand skill")
    schedule_id: int = Field(..., description="Caregiver schedule id")

class CaregiverCreated(BaseModel):
    dni:str 
    skill: float 
    schedule_id: int 
    createdAt: datetime

class CaregiverCreatedResponse(BaseModel):
    status: bool
    details: str
    caregiverOut: CaregiverCreated

class CaregiverOut(BaseModel):
    dni: str
    skill: float 
    schedule_id: int 
    email: EmailStr
    name: str
    lastname: str
    is_active: bool
    phone: str
    birthdate: date
    createdAt: datetime
    


class CaregiverOutResponse(BaseModel):
    status: bool
    details: str
    caregiverOut: CaregiverOut


class CaregiversResponse(BaseModel):
    status: bool
    details: str
    caregiversOut: List[CaregiverOut]
