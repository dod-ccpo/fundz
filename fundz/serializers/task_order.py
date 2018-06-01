from fundz.app import ma
from fundz.models import TaskOrder


class TaskOrderSerializer(ma.ModelSchema):
    class Meta:
        model = TaskOrder
