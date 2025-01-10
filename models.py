from database import Base
from sqlalchemy import Column, Integer, String, Text, BigInteger
from uuid import uuid4


class User(Base):
    __tablename__="user"

    user_id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(length=50), unique=True)
    password = Column(String(length=1000))
    nic = Column(String(length=50))
    email = Column(String(length=50))
    phone = Column(String(length=50))


