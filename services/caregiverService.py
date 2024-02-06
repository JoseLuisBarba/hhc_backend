from sqlalchemy.sql import func
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from datetime import datetime
from dtos.caregiver import CaregiverOut, CaregiverOutResponse, CaregiversResponse, CaregiverCreate, CaregiverCreated, CaregiverCreatedResponse
from repository.caregiver import getAllAviablesCaregivers
from models.orm import  Caregiver
from sqlalchemy.sql import func
from typing import List



class CaregiverService:

    def __init__(self, dbSession: Session):

        self.dbSession = dbSession

    async def createCaregiver(self, caregiver: CaregiverCreate) -> Optional[CaregiverCreatedResponse]:
        try:
            caregiverIn = Caregiver(
                dni= caregiver.dni, 
                skill= caregiver.skill,
                schedule_id= caregiver.schedule_id,
                is_active= True,
                createdAt= func.now(),
                updatedAt= None,
                deletedAt= None
            )
            
            self.dbSession.add(caregiverIn)
            await self.dbSession.flush()

            caregiverOut = CaregiverCreated(
                dni= caregiver.dni, 
                skill= caregiver.skill, 
                schedule_id= caregiver.schedule_id, 
                createdAt= datetime.now()
            )
        

            return CaregiverCreatedResponse(status=True, details='Caregiver created', caregiverOut=caregiverOut)
        
        except SQLAlchemyError as e:
            print(e)
            return  CaregiverCreatedResponse(status=True, details='Caregiver was not created', caregiverOut=None)
        

    async def getAllCaregivers(self) ->  CaregiversResponse:
        try:
            caregivers = await getAllAviablesCaregivers(self.dbSession)

            if not caregivers:
                return CaregiversResponse(status=False, details='The caregivers were not get', caregiversOut=[])
            
            

            return CaregiversResponse(status=True, details='The caregivers were get', caregiversOut=caregivers)
        
        except SQLAlchemyError as e:
            print(e)
            return CaregiversResponse(status=False, details='Error, the caregivers were not get', caregiversOut=[])
        


    # async def getScheduleById(self, id: int) -> Optional[ScheduleOutResponse]:
    #     try:

    #         schedule = await getScheduleById(self.dbSession, id)

    #         if not schedule:
    #             return  ScheduleOutResponse(status=False, details='error in getting schedule', scheduleOut=None)
            
    #         scheduleOut = ScheduleOut(
    #             id= schedule.id, 
    #             start_time= schedule.start_time, 
    #             leaving_time= schedule.leaving_time, 
    #             is_active= schedule.is_active, 
    #             createdAt= schedule.createdAt
    #         )

    #         return ScheduleOutResponse(status=True, details='The schedule was get', scheduleOut=scheduleOut)
        
    #     except SQLAlchemyError as e:
    #         print(e)
    #         return  ScheduleOutResponse(status=False, details='error in getting schedule', scheduleOut=None)
        

