from unicodedata import category
from sqlmodel.sql.expression import Select, SelectOfScalar
from sqlmodel import create_engine, Session
from beerlog.config import settings
from beerlog import models

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
