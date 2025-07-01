from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.ext.declarative import declared_attr

class AuditMixin:
    @declared_attr
    def created_by(cls):
        return Column(String(100), nullable=True)

    @declared_attr
    def created_date(cls):
        return Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    @declared_attr
    def last_updated_by(cls):
        return Column(String(100), nullable=True)

    @declared_attr
    def last_updated_date(cls):
        return Column(DateTime(timezone=True), onupdate=func.now())
