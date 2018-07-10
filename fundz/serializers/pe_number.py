from . import marshmallow
from fundz.models import PENumber


class PENumberSerializer(marshmallow.ModelSchema):
    class Meta:
        model = PENumber
