# app/model.py

from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id :int = Field(default=None)
    title : str = Field(...)
    content : str = Field(...)


    class Config:
        json_schema_extra = {
            'example': {
                'title': 'Securing FastAPI applications with jwt',
                'content':'In this tutorial you will learn how to secure your API using jwt, encide and decode jwt tokens'
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(..., min_length=2, max_length=100)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)

    class Config:
        json_schema_extra = {
            'example': {
                'fullname': 'Fawad Irfan Sheikh',
                'email': 'fawad@stopmail.com',
                'password': 'HukonaMattata'
            }
        }
        validate_assignment = True    # Validate on field updates
        extra = "forbid"             # Reject unexpected fields
        case_sensitive = False       # More flexible field matching

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)

    class Config:
        json_schema_extra = {
            'example' : {
                'email' : 'fawad@stopmail.com',
                'password': 'HukonaMattata'
            }
        }
        validate_assignment = True    # Validate on field updates
        extra = "forbid"             # Reject unexpected fields
        case_sensitive = False       # More flexible field matching