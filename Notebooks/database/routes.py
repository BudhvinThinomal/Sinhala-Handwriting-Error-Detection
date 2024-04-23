from fastapi import APIRouter, HTTPException
from Notebooks.database.database_models import User
from Notebooks.database.database import collection_name
from Notebooks.database.schema import userEntity, usersEntity
from bson import ObjectId

database_router = APIRouter()


# fetchAll
@database_router.get("/database/get-all-users")
async def get_all_users():
    return usersEntity(collection_name.find())


# fetchById
@database_router.get("/database/get-user/{id}")
async def get_user_by_id(id: str):
    user = collection_name.find_one({"_id": ObjectId(id)})
    if user:
        return userEntity(collection_name.find_one({"_id": ObjectId(id)}))
    else:
        raise HTTPException(status_code=404, detail="User not found")


# verify
@database_router.get("/database/verify/{username}")
async def user_verification(username: str, password: str):
    user = collection_name.find_one({"username": username})
    if user:
        user_data = userEntity(user)
        user_instance = User(**user_data)  # Create an instance of User
        if user_instance.verify_password(password):
            return {
                "message": "User verified",
                "user": user_data,
            }
        else:
            raise HTTPException(status_code=401, detail="Invalid password")
    else:
        raise HTTPException(status_code=404, detail="User not found")


# post
@database_router.post("/database/create-user")
async def create_user(user: User):
    # Check if the username already exists
    existing_user = collection_name.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Serialize the password
    hashed_password = user.hashed_password()
    user_data = user.dict()
    user_data["password"] = hashed_password

    # Insert the user details into the collection
    inserted_user = collection_name.insert_one(user_data)
    return {
        "message": "User created successfully",
        "user_id": str(inserted_user.inserted_id),
    }


# update
@database_router.put("/database/update-user/{id}")
async def update_user(id: str, user: User):
    # Check if the username already exists
    if user.username:
        existing_user = collection_name.find_one(
            {"username": user.username, "_id": {"$ne": ObjectId(id)}}
        )
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

    # Serialize the password
    if user.password:
        hashed_password = user.hashed_password()
        user.password = hashed_password

    # Update the user details in the collection
    updated_data = user.dict(exclude_unset=True)  # Only include updated fields

    # Check if any fields are provided in the update request
    if len(updated_data) == 0:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": updated_data})
    return {
        "message": "User updated successfully",
        "user_id": userEntity(collection_name.find_one({"_id": ObjectId(id)})),
    }


# delete
@database_router.delete("/database/delete-user/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
