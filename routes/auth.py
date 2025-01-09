from fastapi import APIRouter, HTTPException, status, Response
from schema import UserRegistration
from database import session
from models import User
from utils import get_hashed_password



router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/register")
async def register(user:UserRegistration):
    existing_user = session.query(User).filter_by()
    
    if user.username == existing_user.username:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this user name already exist"
        )
    else:
        hashed_password = get_hashed_password(password=user.password)


        new_user= User(
            user_id = user.user_id,
            username = user.username,
            password = hashed_password,
            nic = user.nic,
            email = user.email,
            phone = user.phone
        )

        session.add(new_user)

        session.commit()

        return Response(
            content="User Creation Successfully",
            status_code=status.HTTP_201_CREATED
        )



