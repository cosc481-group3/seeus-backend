from dataclasses import dataclass
from typing import Optional


@dataclass
class GoogleUser:
    id: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    picture_url: Optional[str] = None


@dataclass
class User:
    username: str
    google_user_id: str
    id: Optional[int] = None # id can be None when we create this object, before user exists in DB
    picture_url: Optional[str] = None
    phone: Optional[str] = None
    is_banned: bool = False
    eid: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
