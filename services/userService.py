from dtos.user import UserOut, UserAuth, UserUpdate, UserCreate, UserOutResponse
from core.security import getPassword, verifyPassword
from models.orm import User
from repository.users import getUserById

from sqlalchemy.sql import func
from typing import Optional
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from datetime import datetime

class UserService:

    def __init__(self, dbSession: Session):
        self.dbSession = dbSession

    async def createUser(self, user: UserCreate) -> Optional[UserOutResponse]:
        try:
            hashedPassword = getPassword(user.password)

            userIn = User(
                dni=user.dni,
                email=user.email,
                password=hashedPassword,
                name=user.name,
                lastname=user.lastname,
                phone=user.phone,
                birthdate=  datetime.strptime(user.birthdate, '%Y-%m-%d').date(),
                is_active=True,
                createdAt=func.now(),
                updatedAt=None,
                deletedAt=None
            )

            self.dbSession.add(userIn)

            await self.dbSession.flush()
            
            userOut = UserOut(
                dni= user.dni, 
                email= user.email, 
                name= user.name, 
                lastname=user.lastname, 
                is_active=True
            )

            return UserOutResponse(status=True, userOut=userOut)
        
        
    
        except SQLAlchemyError as e:
            print(e)
            return  UserOutResponse(status=False, userOut=None)


    async def authenticate(self, identifier: str, hashedPassword: str) -> Optional[UserOut]:
        user = await getUserById(self.dbSession, identifier)

        if not user or not verifyPassword(hashedPassword, user.hashed_password):
            return None
        
        return UserOut (
            dni= user.dni, 
            email= user.email, 
            name= user.name, 
            lastname=user.lastname, 
            is_active=user.is_active
        )

    async def getUserByIdentifier(self, identifier: str) -> Optional[UserOut]:

        user = await getUserById(self.dbSession, identifier)

        if not user:
            return None
        
        return UserOut (
            dni= user.dni, 
            email= user.email, 
            name= user.name, 
            lastname=user.lastname, 
            is_active=user.is_active
        )