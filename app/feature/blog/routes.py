from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .services.create_blog import BlogResponse, BlogCreate, create_blog
from ...core.database import get_db

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)
@router.post("/", response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
def create_new_blog(request: BlogCreate, db: Session = Depends(get_db)):
    return create_blog(db, request)
