from sqlalchemy.orm import Session
from .. import models, schemas


def create_validate_code(db: Session, valid_information: schemas.EmailCreate, code: int):
    db_validate = models.Email(**valid_information.dict(), code=code)
    db.add(db_validate)
    db.commit()
    db.refresh(db_validate)
    return db_validate


def get_by_email(db: Session, email: str):
    return db.query(models.Email).filter(models.Email.email == email).first()
