from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from dtos.patient import PatientOutResponse, PatientCreate
from services.patientService import PatientService
from models.orm import User
from services.authService import getCurrentUser
from db.mysql import async_session
from sqlalchemy.exc import IntegrityError
from dtos.auth import LoginDTO

patientRouter = APIRouter()

@patientRouter.post('/create', summary="Create new patient", response_model=PatientOutResponse)
async def createUser(data: PatientCreate):
    async with async_session() as session:
        async with session.begin():
            try:
                return await PatientService(session).createPatient(data)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email or dni already exist"
                )
