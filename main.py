from fastapi import FastAPI, HTTPException
from requests import Session
from database import base, engine, Pet
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Create database
base.metadata.create_all(engine)

app = FastAPI()

# Create Read Update Delete
@app.get("/")
def root():
    return "pet"

class PetRequest(BaseModel):
    name: str
    age: str
    race: str
    species: str

# Create
@app.post("/pet")
def create_pet(pet: PetRequest):
    
    # Create database session
    session = Session(bind=engine, expire_on_commit=False)
    
    # Create instance of the Pet database model
    petdb = Pet(name=pet.name, age=pet.age, race=pet.race, species=pet.species)
    
    session.add(petdb)
    session.commit()
    
    # Get the created name id
    id = petdb.id
    
    # Close session
    session.close()
    
    return {"id": id, "name": pet.name, "age": pet.age, "race": pet.race, "species": pet.species}

# Read
@app.get("/pet/{id}")
def read_pet(id: int):
    
    # Create database session
    session = Session(bind=engine, expire_on_commit=False)
    
    pet = session.query(Pet).get(id) # SELECT * FROM Pets WHERE ID = id
    
    # Close session
    session.close()
        
    if not pet:
        raise HTTPException(status_code=404, detail=f"Pet item with id {id} not found")
    
    return {"id": id, "name": pet.name, "age": pet.age, "race": pet.race, "species": pet.species}

# Update
@app.put("/pet/{id}")
def update_pet(id: int, name: str, age: str, race: str, species: str):
    # Create database session
    session = Session(bind=engine, expire_on_commit=False)
    
    pet = session.query(Pet).get(id) # SELECT * FROM Pets WHERE ID = id
    if pet:
        pet.name = name
        pet.age = age
        pet.race = race
        pet.species = species
        session.commit()        
    
    # Close session
    session.close()
    
    if not pet:
        raise HTTPException(status_code=404, detail=f"Pet item with id {id} not found")
    
    return pet

# Delete
@app.delete("/pet/{id}")
def delete_pet(id: int):
    # Create database session
    session = Session(bind=engine, expire_on_commit=False)
    
    pet = session.query(Pet).get(id) # SELECT * FROM Pets WHERE ID = id
    if pet:
        session.delete(pet)
        session.commit()        
    
    # Close session
    session.close()
    
    if not pet:
        raise HTTPException(status_code=404, detail=f"Pet item with id {id} not found")
    
    return pet

# Get all
@app.get("/pet")
def read_pet_list():
    # Create database session
    session = Session(bind=engine, expire_on_commit=False)
    
    pet_list = session.query(Pet).all() # SELECT * FROM Pets
    
    # Close session
    session.close()
    
    return pet_list
