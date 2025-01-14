from fastapi import APIRouter, status, Response, HTTPException
from fastapi.responses import JSONResponse
from models import Equipment, User
from database import Base, engine, session
from utils import get_hashed_password
from schema import AddEquipment, AddUser


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.get("/equipments")
async def get_equipments():
    all_equipments = session.query(Equipment).all()

    serialized_equipments_data = [equipment.to_dict() for equipment in all_equipments]

    return JSONResponse(
        content=serialized_equipments_data,
        status_code=200
    )


@router.post("/equipments")
async def add_equipments(addEquipment : AddEquipment):
    new_equipment = Equipment(
        equipment_name = addEquipment.equipment_name,
        equipment_type = addEquipment.equipment_type,
        equipment_status = addEquipment.equipment_status,
        description = addEquipment.description
    )

    session.add(new_equipment)

    session.commit()

    return Response(
        content="Equipment added successfully.",
        status_code=status.HTTP_201_CREATED
    )
    
@router.delete("/equipments/{equipment_id}")
async def delete_equipments(equipment_id:int):
    existing_equipment = session.query(Equipment).filter(Equipment.equipment_id==equipment_id).first()

    if existing_equipment:
        session.delete(existing_equipment)

        session.commit()

        return Response(
            content="Object deleted successfully.",
            status_code=status.HTTP_200_OK
        )
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Object does not exist"
        )


@router.put("/equipments/{equipment_id}")
async def update_equipments(equipment_id:int, addEquipment : AddEquipment):
    existing_equipment=session.query(Equipment).filter(Equipment.equipment_id==equipment_id).first()

    if existing_equipment:
        existing_equipment.equipment_name = addEquipment.equipment_name
        existing_equipment.equipment_type = addEquipment.equipment_type
        existing_equipment.equipment_status = addEquipment.equipment_status
        existing_equipment.description = addEquipment.description

        session.commit()
        
        return Response(
            content="Object updated successfully.",
            status_code=status.HTTP_200_OK
        )
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Object does not exist"
        )
    

@router.post("/users")
async def add_users(addUser: AddUser):
    existing_user=session.query(User).filter_by(username=addUser.username).first()

    if existing_user:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this user name already exist"
        )
    else:
        hashed_password = get_hashed_password(password=addUser.password)

        new_user = User(
            username = addUser.username,
            password = hashed_password,
            nic = addUser.nic,
            email = addUser.email,
            phone = addUser.phone
        )

        session.add(new_user)

        session.commit()

        session.refresh(new_user)

        return Response(
            content="User added successfully.",
            status_code=status.HTTP_201_CREATED
        )





