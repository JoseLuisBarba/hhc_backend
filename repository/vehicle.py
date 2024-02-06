from models.orm import Vehicle
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_, update


async def getAllActiveVehicles(db: Session) -> List[Vehicle]:
    query = (
         select(Vehicle).where(Vehicle.is_active == True)
    )
    vehicles = await db.scalars(query)
    return vehicles