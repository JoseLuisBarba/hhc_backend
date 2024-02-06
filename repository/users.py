from models.orm import User

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError


async def getUserById(db: Session, identifier: int) -> Optional[User]:
    """Retrieves a user by their DNI or email
    """
    try:
        query = (
            select(User)
            .where(or_(User.dni == identifier, User.dni == identifier))
            .limit(1)
        )

        user = await db.scalar(query)
        return user
    except SQLAlchemyError as e:
        #logger.error(f"Error retrieving user by DNI: {e}")
        return None 

# async def getUserById(db: Session, identifier: int):

#     query = (
#         select(User)
#         .where(or_(User.email == identifier, User.dni == identifier))
#         .limit(1)
#     )

#     user = await db.scalar(query)
    
#     return user