from flask import Blueprint, jsonify, request
from infrastructure.database.databaseConnetion import DatabaseConnection
from infrastructure.repositories.sql_orders_repositories import SQLOrdersRepository
from domain.models import Order

# Crear un Blueprint para las rutas de la API relacionadas con órdenes
orders_bp = Blueprint('orders', __name__)

# Crear una instancia de DatabaseConnection para la conexión a la base de datos
db_connection = DatabaseConnection(database_name='api_gateway', user='root', password='')

# Crear una instancia de SQLOrdersRepository utilizando la conexión a la base de datos
orders_repository = SQLOrdersRepository(db_connection)

# Ruta para crear una nueva orden
@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = Order(data['id'], data['total'], data['date'], data['status'])
    created_order = orders_repository.create_order(order)
    return jsonify(created_order.__dict__)

# Ruta para obtener una orden por su ID
@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = orders_repository.get_order_by_id(order_id)
    if order:
        return jsonify(order.__dict__)
    else:
        return jsonify({'message': 'Order not found'}), 404

# Ruta para actualizar el estado de una orden
@orders_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    data = request.json
    updated_order = orders_repository.update_order_status(order_id, data['status'])
    return jsonify(updated_order.__dict__)

# Ruta para eliminar una orden por su ID
@orders_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    orders_repository.delete_order(order_id)
    return jsonify({'message': 'Order deleted'})

# Agregar el Blueprint al objeto app de Flask en el archivo app.py
# app.register_blueprint(orders_bp, url_prefix='/api')
