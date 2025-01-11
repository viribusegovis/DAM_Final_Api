from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str
    password: str
    is_active: bool = True


class UserCreate(UserBase):
    # Inherits all fields from UserBase and adds none
    pass
    # Contains:
    # - email: str
    # - name: str
    # - password: str


class UserResponse(UserBase):
    # Inherits all fields from UserBase and adds:
    user_id: int
    created_at: datetime
    last_login: Optional[datetime]

    # Contains:
    # - email: str
    # - name: str
    # - password: str
    # - is_active: bool
    # - user_id: int
    # - created_at: datetime
    # - last_login: Optional[datetime]


class RecipeBase(BaseModel):
    title: str
    description: Optional[str]
    preparation_time: int
    servings: int
    difficulty: str
    category: str
    image_url: Optional[str]


class RecipeCreate(RecipeBase):
    # Inherits all fields from RecipeBase and adds:
    author_id: int

    # Contains:
    # - title: str
    # - description: Optional[str]
    # - preparation_time: int
    # - servings: int
    # - difficulty: str
    # - category: str
    # - image_url: Optional[str]
    # - author_id: int


class RecipeResponse(RecipeBase):
    # Inherits all fields from RecipeBase and adds:
    id: int
    created_at: datetime

    # Contains:
    # - title: str
    # - description: Optional[str]
    # - preparation_time: int
    # - servings: int
    # - difficulty: str
    # - category: str
    # - image_url: Optional[str]
    # - id: int
    # - created_at: datetime

    class Config:
        from_attributes = True


class InstructionBase(BaseModel):
    step_number: int
    instruction_text: str


class InstructionCreate(InstructionBase):
    # Inherits all fields from InstructionBase and adds:
    recipe_id: int

    # Contains:
    # - step_number: int
    # - instruction_text: str
    # - recipe_id: int


class IngredientBase(BaseModel):
    name: str


class RecipeIngredientBase(BaseModel):
    # Inherits all fields from IngredientBase and adds:
    recipe_id: int
    ingredient_id: int
    amount: float
    unit: str

    # Contains:
    # - name: str
    # - recipe_id: int
    # - ingredient_id: int
    # - amount: float
    # - unit: str
