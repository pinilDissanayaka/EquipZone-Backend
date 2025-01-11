from fastapi import APIRouter, HTTPException, Response, status, Depends
from utils import get_current_user    
from fastapi.responses import JSONResponse
from database import Base, session, engine
from models import Equipment


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/get-equipments")
async def get_equipments():
    all_equipments = session.query(Equipment).all()

    serialized_equipments_data = [equipment.to_dict() for equipment in all_equipments]

    return JSONResponse(
        content=serialized_equipments_data,
        status_code=status.HTTP_200_OK)


# Protected endpoint
@router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {current_user['sub']}! This is a protected route."}