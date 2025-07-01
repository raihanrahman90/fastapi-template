from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.models import Blog
from uuid6 import uuid7

# ----- Schema -----
class BlogCreate(BaseModel):
    title: str
    body: str

class BlogResponse(BlogCreate):
    id: str

    class Config():
        from_attributes = True

# ----- Service -----
def create_blog(db: Session, request: BlogCreate) -> BlogResponse:
    new_blog = Blog(
        id=str(uuid7()),
        title=request.title,
        body=request.body,
        created_by="system",
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
