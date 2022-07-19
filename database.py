from sqlalchemy import Integer, Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///veterinary.db")

# Create declarative database instance
base = declarative_base()

# Define Todo table
class Pet(base):
    __tablename__ = "Pets"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(String(50))
    race = Column(String(50))
    species = Column(String(50)) 
    
