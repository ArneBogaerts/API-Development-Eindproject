from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    albums = relationship("CD", back_populates="artist")

class CD(Base):
    __tablename__ = "cds"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    artist = relationship("Artist", back_populates="albums", lazy='joined')
    reviews = relationship("Review", back_populates="cd")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float, index=True)
    comment = Column(String(255), index=True)
    cd_id = Column(Integer, ForeignKey("cds.id"))
    cd = relationship("CD", back_populates="reviews")
