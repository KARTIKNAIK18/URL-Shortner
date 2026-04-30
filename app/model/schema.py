from pydantic import BaseModel,HttpUrl


class UrlForamt(BaseModel):
    url:HttpUrl