from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base
from .audit import AuditMixin
from uuid6 import uuid7
import uuid

class User(AuditMixin, Base):
    __tablename__ = 'user'

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid7()))
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)