from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float
from datetime import datetime

from .db import Base


class Product(Base):
    """Product in the inventory/catalogue."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(64), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)
    stock = Column(Integer, default=0)
    image_url = Column(String(1024), nullable=True)
    category = Column(String(255), nullable=True)


class PostTask(Base):
    """Scheduled social post."""

    __tablename__ = "post_tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    media_url = Column(String(1024), nullable=True)
    scheduled_time = Column(DateTime, nullable=False, index=True)
    destination = Column(String(10), nullable=False)  # fb, ig or both
    posted = Column(Boolean, default=False)


class MessageLog(Base):
    """Log of inbound and outbound messages."""

    __tablename__ = "message_logs"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(10), nullable=False)  # fb, ig, wa
    sender_id = Column(String(128), nullable=False)
    message = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Account(Base):
    """Connected accounts for MetaOps."""

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    page_id = Column(String(128), nullable=True)
    ig_business_id = Column(String(128), nullable=True)
    wa_phone_number_id = Column(String(128), nullable=True)
    access_token = Column(String(2048), nullable=False)
