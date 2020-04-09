from typing import Optional

from database import db
from models import User, GoogleUser


def create_user(user: User) -> User:
    result = db.query_one(
        'insert into users (google_user_id, first_name, last_name, phone, eid) '
        'values (%(google_id)s, %(fname)s, %(lname)s, %(phone)s, %(eid)s) '
        'returning id',
        {
            'google_id': user.google_user_id,
            'fname': user.first_name,
            'lname': user.last_name,
            'phone': user.phone,
            'eid': user.eid
        }
    )
    db.commit()
    user.id = result['id']
    return user


def create_user_from_google_user(google_user: GoogleUser) -> User:
    user = User(
        google_user_id=google_user.id,
        first_name=google_user.first_name,
        last_name=google_user.last_name,
        picture_url=google_user.picture_url
    )
    return create_user(user)


def find_user_by_google_id(google_id: str) -> Optional[User]:
    row = db.query_one('select * from users where google_user_id = %s', [google_id])

    if row is None:
        return None

    return map_user_row(row)


def map_user_row(row: dict) -> User:
    return User(
        id=row['id'],
        username=row['username'],
        google_user_id=row['google_user_id'],
        eid=row['eid'],
        first_name=row['first_name'],
        last_name=row['last_name'],
        phone=row['phone'],
        is_banned=row['is_banned'],
        picture_url=None
    )
