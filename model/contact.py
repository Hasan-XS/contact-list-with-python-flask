from sqlalchemy import *
from extention import *

class Contact(db.Model):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False, index=True)
    address = Column(String, unique=False, nullable=False, index=True)
    code_post = Column(Integer, unique=False, nullable=False, index=True)
    last_name = Column(String, nullable=False, index=True)
    phone = Column(Integer, unique=False, nullable=False, index=True)