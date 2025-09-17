
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.utils.db_verify import is_email_taken

def signup_user(user,db:Session):
    user.email = user.email.strip().lower()
    # Check if the user exist in the database
    # If the email is unique
    if not is_email_taken(db,user.email):
        try:
            pass
        finally:
            db.close()
        return {"message":"Account created succesfully"}

    raise HTTPException(
        status_code = status.HTTP_409_CONFLICT,
        detail = "Email already in use"
    )