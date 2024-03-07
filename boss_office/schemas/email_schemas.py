from pydantic import BaseModel, EmailStr


class EmailCreate(BaseModel):
    email: EmailStr


class Email(EmailCreate):
    id: str
    code: int

    class Config:
        orm_mode = True
