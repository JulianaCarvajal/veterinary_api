from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    # SELECT * FROM User WHERE id = user_id
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    # SELECT * FROM User WHERE email = email
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session):
    # SELECT * FROM User
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    # Build a new User object
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # Add the new User object to the database
    db.add(db_user)
    # Commit the changes to the database
    db.commit()
    # Refresh the user object to get the id
    db.refresh(db_user)
    # Return the new user object
    return db_user

def get_pets(db: Session):
    # SELECT * FROM Pet
    return db.query(models.Pet).all()

def create_user_pet(db: Session, pet: schemas.PetCreate, user_id: int):
    # Build a new Pet object
    # models.Pet(title=pet.title, description=pet.description, user_id=user_id)
    db_pet = models.Pet(**pet.dict(), user_id=user_id)
    # Add the new Pet object to the database
    db.add(db_pet)
    # Commit the changes to the database
    db.commit()
    # Refresh the pet object
    db.refresh(db_pet)
    # Return the new pet object
    return db_pet

def get_pet(db: Session, pet_id: int):
    # SELECT * FROM Pet WHERE id = pet_id
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()

# def update_pet(db: Session, pet: schemas.PetUpdate, pet_id: int):
#     pet.name = pet.name
#     pet.age = pet.age
#     pet.breed = pet.breed
#     pet.species = pet.species
    
#     db.commit()
#     db.refresh(pet)
#     return pet