def user_schema(item) -> dict:
    return {
        "user_id" : str(item["_id"])
    }