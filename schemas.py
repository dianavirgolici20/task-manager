from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str
    description: str = ""

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    done: bool

    class Config:
        from_attributes = True
class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=8, max_length=72)

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
