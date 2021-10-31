from typing import List
from decimal import Decimal

from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from db.models import Product


__all__ = ['ProductService']


class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    unit_price: float
    is_featured: bool


class ProductService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_featured_products(self, is_customer_preferred: bool) -> List[ProductModel]:
        discount = Decimal(0.95 if is_customer_preferred else 1)

        q = await self.db_session.execute(select(Product).where(Product.is_featured))
        return [
            ProductModel(
                id=product.id,
                name=product.name,
                description=product.description,
                is_featured=product.is_featured,
                unit_price=product.unit_price * discount,
            )
            for product in q.scalars().all()
        ]
