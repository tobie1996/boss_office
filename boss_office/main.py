from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, status, Depends
from . import models, schemas, crud
from .core.db import engine, get_db_session
import emails

from .utils.form_regx import generate_validation_code, validate_validation_code

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def send_validation_email(email: str, code: int):
    message = emails.html(html=f"<p>Hi!<br>Here is your validation code, to be able to create your organization:"
                               f" {str(code)}",
                          subject="Comii foundation",
                          mail_from=('CTO Comii', "comii@gmail.com"))

    r = message.send(to=email, smtp={'host': 'localhost', 'timeout': 5, "port": 1025})
    return r


@app.post("/user/email")
def create_validate_code(email: schemas.EmailCreate, db: Session = Depends(get_db_session)):
    bd_email = crud.code_email.get_by_email(db, email=email.email)
    if bd_email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This mail is already registered")
    code = validate_validation_code(generate_validation_code())
    r = send_validation_email(email.email, code)
    if r.status_code != 250:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This email did not go to the user")
    crud.code_email.create_validate_code(db=db, valid_information=email, code=code)
    return {"message": "mail send successfully"}
