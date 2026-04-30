
import hashlib



def url_hash(url:str,count=6):
    hashed_url = hashlib.sha256(url.encode("utf-8")).hexdigest()
    temp = hashed_url[:count]
    return temp

