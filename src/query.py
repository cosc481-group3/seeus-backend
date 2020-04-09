from database import db
from models import User, GoogleUserInfo


def create_user(user: User) -> User:
    result = db.query_one("""
        insert into users (
            google_user_id, username, first_name, last_name, phone, eid, picture_url
        ) values (
            %(google_id)s, %(username)s, %(fname)s, %(lname)s, %(phone)s, %(eid)s, %(pic_url)s
        ) 
        returning id
        """, {
        'google_id': user.google_user_id,
        'username': user.username,
        'fname': user.first_name,
        'lname': user.last_name,
        'phone': user.phone,
        'eid': user.eid,
        'pic_url': user.picture_url
    })
    db.commit()
    user.id = result['id']
    return user


def update_user(user: User) -> User:
    db.query_commit("""
        update users set 
            first_name = %(fname)s,
            last_name = %(lname)s,
            phone = %(phone)s,
            eid = %(eid)s,
            picture_url = %(pic_url)s
        """, {
        'fname': user.first_name,
        'lname': user.last_name,
        'phone': user.phone,
        'eid': user.eid,
        'pic_url': user.picture_url
    })
    return user


def find_or_create_user(google_user: GoogleUserInfo) -> User:
    row = db.query_one('select * from users where google_user_id = %s', [google_user.id])
    if row:
        user = _map_user_row(row)
        if user.picture_url != google_user.picture_url:
            user.picture_url = google_user.picture_url
            update_user(user)
        return user

    return create_user(User(
        username=google_user.email.replace('@emich.edu', ''),
        google_user_id=google_user.id,
        first_name=google_user.first_name,
        last_name=google_user.last_name,
        picture_url=google_user.picture_url
    ))


def _map_user_row(row: dict) -> User:
    return User(
        id=row['id'],
        username=row['username'],
        google_user_id=row['google_user_id'],
        eid=row['eid'],
        first_name=row['first_name'],
        last_name=row['last_name'],
        phone=row['phone'],
        is_banned=row['is_banned'],
        picture_url=row['picture_url']
    )
