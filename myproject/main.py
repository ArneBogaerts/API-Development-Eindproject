from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cds/", response_model=schemas.CD)
def create_cd(cd: schemas.CDCreate, db: Session = Depends(get_db)):
    return crud.create_cd(db=db, cd=cd)

@app.get("/cds/", response_model=List[schemas.CD])
def read_cds(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cds = crud.get_cds(db, skip=skip, limit=limit)
    return cds

@app.post("/artists/", response_model=schemas.Artist)
def create_artist(artist: schemas.ArtistBase, db: Session = Depends(get_db)):
    return crud.create_artist(db=db, artist=artist)

@app.get("/artists/", response_model=List[schemas.Artist])
def read_artists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    artists = crud.get_artists(db, skip=skip, limit=limit)
    return artists

@app.post("/reviews/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db=db, review=review)

@app.get("/cds/{cd_id}/reviews/", response_model=List[schemas.Review])
def read_reviews_by_cd(cd_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = crud.get_reviews_by_cd(db, cd_id=cd_id, skip=skip, limit=limit).all()
    return reviews


# @app.get("/cds/{cd_id}/reviews/", response_model=List[schemas.Review])
# def read_reviews_by_cd(cd_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     reviews = crud.get_reviews_by_cd(db, cd_id=cd_id).offset(skip).limit(limit).all()
#     if reviews is None:
#         raise HTTPException(status_code=404, detail="Reviews not found")
#     return reviews

@app.delete("/cds/{cd_id}", response_model=schemas.CD)
def delete_cd(cd_id: int, db: Session = Depends(get_db)):
    db_cd = crud.get_cd(db, cd_id=cd_id)
    if db_cd is None:
        raise HTTPException(status_code=404, detail="CD not found")
    crud.delete_cd(db, cd_id=cd_id)
    return db_cd

@app.delete("/artists/{artist_id}", response_model=schemas.Artist)
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.delete_artist(db, artist_id=artist_id)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artist

@app.delete("/artists/by-name/{artist_name}", response_model=schemas.Artist)
def delete_artist_by_name(artist_name: str, db: Session = Depends(get_db)):
    db_artist = db.query(models.Artist).filter(models.Artist.name == artist_name).first()
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(db_artist)
    db.commit()
    return db_artist

@app.delete("/cds/by-title/{cd_title}", response_model=schemas.CD)
def delete_cd_by_title(cd_title: str, db: Session = Depends(get_db)):
    db_cd = db.query(models.CD).filter(models.CD.title == cd_title).first()
    if db_cd is None:
        raise HTTPException(status_code=404, detail="CD not found")
    db.delete(db_cd)
    db.commit()
    return db_cd

