from sqlalchemy import Column, Integer, String,text,TIMESTAMP
from app.db.engine import Base




class Urls(Base):
    __tablename__ = "Urls"
    id = Column(Integer,primary_key=True,index=True)
    original_url = Column(String,nullable=False)
    hashed_url = Column(String,unique=True,nullable=False)
    # created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))//for postgress
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('CURRENT_TIMESTAMP'))