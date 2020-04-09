from dataclasses import dataclass

@dataclass
class GoogleUser:
    id: str
    first_name: str
    last_name: str
    email: str
    picture_url: str


@dataclass
class User:
    id: int
    username: str
    google_user_id: str
    eid: str
    first_name: str
    last_name: str
    picture_url: str
    phone: str
    is_banned: bool
