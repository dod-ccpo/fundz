from . import marshmallow
from fundz.models import TaskOrder


class TaskOrderSerializer(marshmallow.ModelSchema):
    class Meta:
        model = TaskOrder
