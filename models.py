from datetime import datetime, UTC

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric, CheckConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)


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


class Instruction(Base):
    __tablename__ = "instructions"
    instruction_id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"))
    step_number = Column(Integer, nullable=False)
    instruction_text = Column(String, nullable=False)


class Ingredient(Base):
    __tablename__ = "ingredients"
    ingredient_id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.ingredient_id", ondelete="CASCADE"), primary_key=True)
    amount = Column(Numeric(10, 2), nullable=False)
    unit = Column(String(50), nullable=False)
