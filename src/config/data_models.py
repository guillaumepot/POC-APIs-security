#src/config/data_models.py

# Lib
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, PrivateAttr, field_validator
from typing import Optional

from src.utils.hashing import hash_string


class BrokenUserModel(BaseModel):
    firstname: str
    lastname: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    password: str = Field(..., min_length = 2 , max_length = 40)
    department: str = None
    manager_id: int = None
    annual_salary: float = None
    created_at: datetime = datetime.now()
    role: int = 1

    @classmethod
    def create_username(cls, firstname: str, lastname: str) -> str:
        return f"{firstname.lower()}_{lastname.lower()}"

    def __init__(self, **data):
        super().__init__(**data)
        self._username = self.create_username(self.firstname, self.lastname)
        self.password = hash_string(self.password)
        
    def to_db_values(self):
        return [
            self.firstname,
            self.lastname,
            self._username,
            self.email,
            self.phone,
            self.department,
            self.manager_id,
            self.annual_salary,
            self.password,
            self.created_at,
            self.role
        ]



class FixedUserModel(BaseModel):
    firstname: str
    lastname: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    password: str = Field(..., min_length = 2 , max_length = 40)
    _department: str = PrivateAttr(default = None)
    _manager_id: int = PrivateAttr(default = None)
    _annual_salary: float = PrivateAttr(default = None)
    _created_at: datetime = PrivateAttr(default = datetime.now())
    _role: int = PrivateAttr(default = 1)

    @field_validator("firstname", "lastname")
    @classmethod
    def capitalize_first_letter(cls, value: str) -> str:
        return value.capitalize()

    @field_validator("password")
    def validate_password(cls, value:str) -> str:
        if not any(char.isdigit() for char in value):
            raise "Password must contain at least one number"
        if not any(char.islower() for char in value) or not any(char.isupper() for char in value):
            raise "Password must contain at least one lowercase and one uppercase letter"
        if not any(char in "!?@#$%^&*()_+" for char in value):
            raise "Password must contain at least one special character: !?@#$%^&*()_+"
        return value

    @classmethod
    def create_username(cls, firstname: str, lastname: str) -> str:
        return f"{firstname.lower()}_{lastname.lower()}"

    def __init__(self, **data):
        super().__init__(**data)
        if self.email:
            self.email = self.email.lower()
        self._username = self.create_username(self.firstname, self.lastname)
        self.password = hash_string(self.password)

    def __setattr__(self, attribute, value):
        if attribute in ["_department", "_manager_id", "_annual_salary", "_created_at", "_role"]:
            raise AttributeError("An error occurred")
        super().__setattr__(attribute, value)

    def to_db_values(self):
        return [
            self.firstname,
            self.lastname,
            self._username,
            self.email,
            self.phone,
            self._department,
            self._manager_id,
            self._annual_salary,
            self.password,
            self._created_at,
            self._role
        ]