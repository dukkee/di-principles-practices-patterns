from sqlalchemy import Column, Integer, String, Boolean, Numeric

from .config import Base


__all__ = ['Product']


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    description = Column(String, nullable=False)
    unit_price = Column(Numeric(precision=2), nullable=False)
    is_featured = Column(Boolean, nullable=False)
