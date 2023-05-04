from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PostOffice    (Base):
    __tablename__ = 'post_office'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

class Edge(Base):
    __tablename__ = 'edge'
    id = Column(Integer, primary_key=True)
    start = Column(Integer)
    end = Column(Integer)
    distance = Column(Float)