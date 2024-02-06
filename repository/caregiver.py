from models.orm import Schedule, User, Caregiver
from typing import List
from dtos.schedule import ScheduleCreate, ScheduleOut, ScheduleOutResponse
from dtos.caregiver import CaregiverOut
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.future import select 
from sqlalchemy import or_, and_, update
from datetime import datetime



async def getAllAviablesCaregivers(db: Session) -> List[CaregiverOut]:
    query = (
         select(Caregiver, User)
         .where(Caregiver.is_active == True)
         .join(User, Caregiver.dni == User.dni)

    )
    caregivers = await db.execute(query)

    caregiversResponse: List[CaregiverOut] = []

    for caregiver, user in caregivers:
        caregiversResponse.append(
            CaregiverOut(
                dni= caregiver.dni, 
                skill= caregiver.skill, 
                schedule_id= caregiver.schedule_id, 
                email= user.email, 
                name= user.name, 
                lastname= user.lastname, 
                is_active= user.is_active, 
                phone= user.phone, 
                birthdate= user.birthdate, 
                createdAt= user.createdAt
            )
        )

    return caregiversResponse


async def getCaregiverById(db: Session, identifier: int):
     query = ( 
         select(Caregiver)
         .where(Caregiver.dni == identifier)
         .join(User, Caregiver.dni == User.dni)
         .limit(1)
     )
     caregiver = await db.scalar(query)
     return caregiver
