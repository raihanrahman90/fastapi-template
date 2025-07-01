from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base
from .audit import AuditMixin
from uuid6 import uuid7
import uuid

class Blog(AuditMixin, Base):
    __tablename__ = 'blog'

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid7()))
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)