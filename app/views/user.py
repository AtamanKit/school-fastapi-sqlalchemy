from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.database import get_db

from ..models import User as UserModel

router = APIRouter(prefix="/user", tags=["user"])


class UserSchemaBase(BaseModel):
    email: str | None = None
    full_name: str | None = None


class UserSchemaCreate(UserSchemaBase):
    pass


class UserSchema(UserSchemaBase):
    id: str

    class Config:
        from_attributes = True


@router.get("/get-user", response_model=UserSchema)
async def get_user(id: str, db:AsyncSession = Depends(get_db)):
    user = await UserModel.get(db, id)
    return user


@router.post("/create-user", response_model=UserSchema)
async def create_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_db)):
    user = await UserModel.create(db, **user.dict())
    return user