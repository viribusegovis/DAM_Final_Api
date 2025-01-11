from datetime import datetime, UTC

from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, DateTime

from app.models.base import Base


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String)
    preparation_time = Column(Integer, nullable=False)
    servings = Column(Integer, nullable=False)
    difficulty = Column(String(10))
    image_url = Column(String)
    author_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    category = Column(String(100), nullable=False)
    __table_args__ = (
        CheckConstraint(difficulty.in_(['FACIL', 'MEDIO', 'DIFICIL']), name='valid_difficulty'),
    )
