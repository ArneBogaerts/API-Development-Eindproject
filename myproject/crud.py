from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas, auth

def get_cd(db: Session, cd_id: int):
    return db.query(models.CD).filter(models.CD.id == cd_id).first()

def get_cds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CD).order_by(models.CD.id).offset(skip).limit(limit).all()
def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).order_by(models.Artist.id).offset(skip).limit(limit).all()
def get_artists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artist).order_by(models.Artist.id).offset(skip).limit(limit).all()
def create_artist(db: Session, artist: schemas.ArtistBase):
    existing_artist = db.query(models.Artist).filter(models.Artist.name == artist.name).first()
    if existing_artist:
        raise HTTPException(status_code=400, detail="Artist already exists")
    db_artist = models.Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_reviews_by_cd(db: Session, cd_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Review).filter(models.Review.cd_id == cd_id).offset(skip).limit(limit)

def create_review(db: Session, review: schemas.ReviewCreate):
    cd_exists = db.query(models.CD).filter(models.CD.id == review.cd_id).first()
    if not cd_exists:
        raise HTTPException(status_code=404, detail="CD not found, try another CD-ID")
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def create_cd(db: Session, cd: schemas.CDCreate):
    existing_cd = db.query(models.CD).filter(models.CD.title == cd.title).first()
    if existing_cd:
        raise HTTPException(status_code=400, detail="CD already exists")
    artist = db.query(models.Artist).filter(models.Artist.name == cd.artist_name).first()
    if not artist:
        raise HTTPException(status_code=404, detail=f"Artist with name {cd.artist_name} not found")
    db_cd = models.CD(title=cd.title, artist_id=artist.id)
    db.add(db_cd)
    db.commit()
    db.refresh(db_cd)
    return db_cd

def delete_cd(db: Session, cd_id: int):
    db_cd = db.query(models.CD).filter(models.CD.id == cd_id).first()
    if db_cd:
        db.delete(db_cd)
        db.commit()
        return True
    return False

def delete_artist(db: Session, artist_id: int):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if db_artist:
        db.delete(db_artist)
        db.commit()
        return db_artist
    return None

def delete_artist_by_name(db: Session, name: str):
    db_artist = db.query(models.Artist).filter(models.Artist.name == name).first()
    if db_artist:
        db.delete(db_artist)
        db.commit()
        return db_artist
    return None

def delete_cd_by_title(db: Session, title: str):
    db_cd = db.query(models.CD).filter(models.CD.title == title).first()
    if db_cd:
        db.query(models.Review).filter(models.Review.cd_id == db_cd.id).delete()
        db.delete(db_cd)
        db.commit()
        return db_cd
    return False

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).order_by(models.User.id).offset(skip).limit(limit).all()

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    else:
        return False
