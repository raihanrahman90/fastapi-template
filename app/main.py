from fastapi import FastAPI
from app.feature.blog.routes import router as blog_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

# Register router blog
app.include_router(blog_router)
