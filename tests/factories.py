from factory.alchemy import SQLAlchemyModelFactory

from fundz.database import db
from fundz import models


class PENumberFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.PENumber
        sqlalchemy_session = db.session


class TaskOrderFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.TaskOrder
        sqlalchemy_session = db.session
