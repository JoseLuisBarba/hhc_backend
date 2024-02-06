from fastapi import APIRouter
from routers import users
from routers import auth
from routers import patient
from routers import vehicle

router = APIRouter()

router.include_router(users.userRouter, prefix='/users', tags=["users"])
router.include_router(auth.authRouter, prefix='/auth', tags=["auth"])
router.include_router(vehicle.vehicleRouter, prefix='/vehicles', tags=["vehicles"])
router.include_router(patient.patientRouter, prefix='/patient', tags=["patient"])


# router.include_router(users.userRouter, prefix='/users', tags=["users"])
# router.include_router(auth.authRouter, prefix='/auth', tags=["auth"])
# router.include_router(upload.uploadRouter, prefix='/upload', tags=["upload"])
# router.include_router(incidenceType.typeRouter, prefix='/incidenceType', tags=["incidenceType"])
# router.include_router(incidence.incidenceRouter, prefix='/incidence', tags=["incidence"])
# router.include_router(citizen.citizenRouter, prefix='/citizen', tags=["citizen"])
# router.include_router(serenazgo.serenazgoRouter, prefix='/serenazgo', tags=["Serenazgo"])
# router.include_router(status.statusRouter, prefix='/status', tags=["status"])
