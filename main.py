from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create Pet
@app.post("/users/{user_id}/pets/", response_model=schemas.Pet)
def create_pet_for_user(
    user_id: int, pet: schemas.PetCreate, db: Session = Depends(get_db)
):
    return crud.create_user_pet(db=db, pet=pet, user_id=user_id)

@app.get("/pets/", response_model=list[schemas.Pet])
def get_pets(db: Session = Depends(get_db)):
    pets = crud.get_pets(db)
    return pets

@app.get("/pets/{pet_id}", response_model=schemas.Pet)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = crud.get_pet(db, pet_id)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

# # Update pet
# @app.put("/pets/{pet_id}", response_model=schemas.Pet)
# def update_pet(pet_id: int, pet: schemas.PetUpdate, db: Session = Depends(get_db)):
#     pet = crud.get_pet(db, pet_id)
#     if pet is None:
#         raise HTTPException(status_code=404, detail="Pet not found")
#     return crud.update_pet(db=db, pet=pet, pet_id=pet_id)

# # Delete pet
# @app.delete("/pet/{id}")
# def delete_pet(id: int):
#     # Create database session
#     session = Session(bind=engine, expire_on_commit=False)
    
#     pet = session.query(Pet).get(id) # SELECT * FROM Pets WHERE ID = id
#     if pet:
#         session.delete(pet)
#         session.commit()        
    
#     # Close session
#     session.close()
    
#     if not pet:
#         raise HTTPException(status_code=404, detail=f"Pet item with id {id} not found")
    
#     return pet