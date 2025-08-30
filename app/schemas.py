from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = 0
    image_url: Optional[HttpUrl] = None
    category: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class PostTaskBase(BaseModel):
    text: str
    media_url: Optional[HttpUrl] = None
    scheduled_time: datetime
    destination: str  # fb, ig or both


class PostTaskCreate(PostTaskBase):
    pass


class PostTask(PostTaskBase):
    id: int
    posted: bool

    class Config:
        orm_mode = True


class MessageLog(BaseModel):
    id: int
    platform: str
    sender_id: str
    message: str
    response: Optional[str] = None
    timestamp: datetime

    class Config:
        orm_mode = True
