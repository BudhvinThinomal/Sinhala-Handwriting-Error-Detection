def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "full_name": item["full_name"],
        "username": item["username"],
        "password": item["password"],
        "result": item["result"],
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
