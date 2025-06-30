from fastapi import FastAPI, Depends, responses, Response, HTTPException
from starlette import status
from starlette.responses import JSONResponse

import schemas, models

from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}")
def get_blog_by_id(id: int, response: Response,
                   db: Session = Depends(get_db),
                   status_code: int = status.HTTP_200_OK):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Blog with id {id} not found")
    return blog

@app.delete('/blog/{id}')
def delete_blog_by_id(id: int, response: Response,
                      db: Session = Depends(get_db),
                      status_code: int = status.HTTP_200_OK):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    db.delete(blog)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": f"Blog with id {id} has been deleted"})


@app.put("/blog/{id}", response_model=schemas.Blog)
def update_blog_by_id(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.title = request.title
    blog.body = request.body

    db.commit()
    db.refresh(blog)

    return blog
