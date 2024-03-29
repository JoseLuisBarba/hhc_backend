# from dtos.user import UserOut, UserAuth, UserUpdate
# from dtos.serenazgo import SerenazgoCreate, SerenazgoUpdateImage, SerenazgoOut, SerenazgoLocationUpdate, SerenazgoUpdateActivate, SerenazgoStatus
# from core.security import getPassword, verifyPassword
# from models.users import User
# from models.serenazgo import Serenazgo
# from repository.serenazgo import getSerenazgoById, updateImageSerenazgoById, getAllSerenazgo, getSerenazgoStatusById, updateLocationSerenazgoById, updateActivateSerenazgoById
# from repository.users import getUserById

# from typing import Optional
# from sqlalchemy import or_
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy import update
# from sqlalchemy.future import select
# from sqlalchemy.orm import Session
# from datetime import datetime

# class SerenazgoService:

#     def __init__(self, dbSession: Session):
#         self.dbSession = dbSession

#     async def createSerenazgo(self, userDni: str, data: SerenazgoCreate) -> Optional[Serenazgo]:
#         SerenazgoIn = Serenazgo(
#             dni= userDni,
#             names= data.names,
#             surname1= data.surname1, 
#             surname2= data.surname2,
#             birthDate= data.birthDate,
#             phone= data.phone,
#             address= data.address,
#             urlImage= data.urlImage,
#             uploadDate= data.uploadDate,
#             is_active= data.is_active,
#             is_deleted= data.is_deleted,
#             createdAt= datetime.now(),
#             updatedAt= data.updatedAt,
#             deletedAt= data.deletedAt,
#             userId= userDni,
#             municipalityId= data.municipalityId,
#             scheduleId= data.scheduleId,
#             latitude= data.latitude,
#             longitude= data.longitude

#         )

#         self.dbSession.add(SerenazgoIn)
#         await self.dbSession.flush()
#         return SerenazgoIn



#     async def getSerenazgoById(self, dni: str) -> Optional[Serenazgo]:
#         Serenazgo = await getSerenazgoById(self.dbSession, dni)
#         if not Serenazgo:
#             return None
#         return Serenazgo
    
#     async def updateImageSerenazgoById(self, dni: str, data: SerenazgoUpdateImage):
#         serenazgo = await updateImageSerenazgoById(self.dbSession, dni, data)
#         if not serenazgo:
#             return None
#         return serenazgo
    
    
#     async def authenticate(self, identifier: str, hashedPassword: str) -> Optional[User]:
#         user = await getUserById(self.dbSession, identifier)

#         if not user or not verifyPassword(hashedPassword, user.hashed_password):
#             return None
#         return user

#     async def getUserByIdentifier(self, identifier: str) -> Optional[User]:
#         user = await getUserById(self.dbSession, identifier)

#         if not user:
#             return None
#         return user
    
#     async def getAllSerenazgo(self) -> list[Serenazgo]:
#         Serenazgo = await getAllSerenazgo(self.dbSession)
#         if not Serenazgo:
#             return None
#         return Serenazgo
    
#     async def getSerenazgoStatusById(self, dni: str) -> Optional[SerenazgoStatus]:
#         Serenazgo = await  getSerenazgoStatusById(self.dbSession, dni)
#         if not Serenazgo:
#             return None
#         return Serenazgo
    
#     async def updateLocationIncidenceById(self, dni: str, data: SerenazgoLocationUpdate)-> Optional[Serenazgo]:
#         Serenazgo = await updateLocationSerenazgoById(self.dbSession, dni, data)
#         if not Serenazgo:
#             return None
#         return Serenazgo
    
#     async def updateActivateSerenazgoById(self, dni: str, data: SerenazgoUpdateActivate)-> Optional[Serenazgo]:
#         Serenazgo = await updateActivateSerenazgoById(self.dbSession, dni, data)
#         if not Serenazgo:
#             return None
#         return Serenazgo
    
    
    
    
    
    
    
    
