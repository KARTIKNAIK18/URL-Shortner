from fastapi import HTTPException,status

db ={}

def local_DB(originalUrl:str,hashedUrl:str):
    db[hashedUrl]=originalUrl
    return db
    


def check_Url(hashcode):
    try:
        res = db.get(hashcode)
        return res
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

