from fastapi import FastAPI,HTTPException,status,Depends
from fastapi.responses import RedirectResponse
from app.model.models import Urls
from app.model.schema import UrlForamt
from app.helper.hash import url_hash
from app.helper.get_url import local_DB,check_Url
from sqlalchemy.orm import Session
from app.db.engine import get_db,Sessionlocal,engine
from app.model import models


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post('/shorten')
def get_userURl_shrt(UrlData:UrlForamt,db:Session=Depends(get_db)):
    try:
        shortened_url = url_hash(str(UrlData.url))

        while db.query(Urls).filter(Urls.hashed_url==shortened_url).first():
            shortened_url = url_hash(str(UrlData.url) + shortened_url)
        
        new_data = Urls(
            original_url=str(UrlData.url),
            hashed_url = shortened_url
        )
        db.add(new_data)
        db.commit()
            
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    return {"shortened_url": f"http://localhost:8000/{shortened_url}"}



@app.get("/{UrlData}")
def forward_Url(UrlData:str,db:Session=Depends(get_db)):
    try:
        exist = db.query(Urls).filter(UrlData==Urls.hashed_url).first()
        if exist:
            return RedirectResponse(url=exist.original_url)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
    