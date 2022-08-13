from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    pets = relationship("Pet", back_populates="user")
    
class Pet(Base):
    __tablename__ = "Pets"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    age = Column(String, index=True)
    breed = Column(String, index=True)
    species = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="pets")
    