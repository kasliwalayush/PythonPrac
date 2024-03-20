def noteEntity(item) -> dict:
    return{
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
    }

def notesEntity(item) -> list:
    return [noteEntity(item) for item in item]