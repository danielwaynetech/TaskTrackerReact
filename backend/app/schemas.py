from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class TaskPrioritySchema(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskStatusSchema(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(..., min_length=6)

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    created_at: datetime
    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    colour: str = "#3B82F6"
    
class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    colour: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int
    user_id: int
    created_at: datetime
    class Config:
        from_attributes = True
    
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPrioritySchema = TaskPrioritySchema.MEDIUM
    status: TaskStatusSchema = TaskStatusSchema.TODO
    due_date: Optional[datetime] = None
    category_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPrioritySchema] = None
    status: Optional[TaskStatusSchema] = None
    is_completed: Optional[bool] = None
    due_date: Optional[datetime] = None
    category_id: Optional[int] = None

class TaskResponse(TaskBase):
    id: int
    user_id: int
    is_completed: bool
    created_at: datetime
    updated_at: datetime
    category: Optional[CategoryResponse] = None
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    username: str
    password: str