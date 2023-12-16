from pydantic import BaseModel
from typing import List

class ArtistBase(BaseModel):
    name: str

class Artist(ArtistBase):
    id: int
    class Config:
        orm_mode = True

class CDbase(BaseModel):
    title: str
class CDCreate(CDbase):
    artist_name: str

class CD(CDbase):
    id: int
    artist: Artist
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    rating: float
    comment: str

class ReviewCreate(ReviewBase):
    cd_id: int

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

