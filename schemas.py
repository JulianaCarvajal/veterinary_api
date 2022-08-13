from pydantic import BaseModel
from typing import Union

class PetBase(BaseModel):
    name: str
    age: Union[str, None] = None
    breed: str
    species: str

class Pet(PetBase):
    id: int
    user_id: int
    
    class Config:
        orm_mode = True

class PetCreate(PetBase):
    pass

# class PetUpdate(PetBase):
#     pass

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    pets: list[Pet] = []
    
    class Config:
        orm_mode = True  