from flask import Blueprint, jsonify, abort

from fundz.models import TaskOrder
from fundz.serializers.task_order import TaskOrderSerializer


api = Blueprint('api', __name__)

@api.route('/')
def root():
    return jsonify({'hello': 'world'})

@api.route('/task-order/<string:order_number>', methods=['GET'])
def get_task_order(order_number):
    task_order = TaskOrder.query.filter_by(number=order_number).first()
    if task_order is None:
        abort(404)

    return TaskOrderSerializer().jsonify(task_order)
