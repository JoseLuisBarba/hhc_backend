from dtos.patient import PatientCreate, PatientOut, PatientOutResponse
from core.security import getPassword, verifyPassword
from models.orm import Patient
from repository.users import getUserById

from sqlalchemy.sql import func
from typing import Optional
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from datetime import datetime

class PatientService:
    def __init__(self, dbSession: Session):
        self.dbSession = dbSession

    async def createPatient(self, user: PatientCreate) -> Optional[PatientOutResponse]:
        try:
            hashedPassword = getPassword(user.password)

            patientIn = Patient(
                dni=user.dni,
                is_active=True,
                createdAt=func.now(),
                updatedAt=None,
                deletedAt=None
            )

            self.dbSession.add(patientIn)

            await self.dbSession.flush()
            
            patientOut = PatientOut(
                dni= user.dni, 
            )

            return PatientOutResponse(status=True, PatientOut=patientOut)

        except SQLAlchemyError as e:
            print(e)
            return  PatientOutResponse(status=False, PatientOut=None)
