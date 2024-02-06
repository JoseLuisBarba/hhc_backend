from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from dtos.user import UserCreate, UserOutResponse, UserDetailsResponse
from services.userService import UserService
from models.orm import User
from services.authService import getCurrentUser
from services.vehicleService import VehicleService
from db.mysql import async_session
from sqlalchemy.exc import IntegrityError
from dtos.auth import LoginDTO
from dtos.vehicle import VehicleOutResponse, VehicleCreate

vehicleRouter = APIRouter()

@vehicleRouter.post('/createVehicle', summary="Create new vehicle", response_model=VehicleOutResponse)
async def createUser(data: VehicleCreate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Invalid token",
                    )
                return await VehicleService(session).createVehicle(data)  
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Vehicle already exist"
                )


# @userRouter.get('/me', summary='Get details of currently logged in user', response_model=UserDetailsResponse)
# async def getMe(user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             return user