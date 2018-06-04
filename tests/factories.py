from factory.alchemy import SQLAlchemyModelFactory

from fundz.make_app import db
from fundz import models


class TaskOrderFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.TaskOrder
        sqlalchemy_session = db.session
