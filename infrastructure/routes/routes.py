# infrastructure/routes/routes.py

from flask import Blueprint, jsonify, request
from infrastructure.database.databaseConnetion import DatabaseConnection
from infrastructure.repositories.sql_order_products_repository import SQLOrderProductsRepository
from domain.models import Order, OrderProduct
from infrastructure.repositories.sql_orders_repositories import SQLOrdersRepository

# Crear Blueprints para las rutas de la API relacionadas con órdenes y productos de órdenes
orders_bp = Blueprint('orders', __name__)
order_products_bp = Blueprint('order_products', __name__)

# Crear una instancia de DatabaseConnection para la conexión a la base de datos
db_connection = DatabaseConnection(database='api_gateway', user='root', password='')
db_connection.connect()

# Crear instancias de los repositorios utilizando la conexión a la base de datos
orders_repository = SQLOrdersRepository(db_connection)
order_products_repository = SQLOrderProductsRepository(db_connection)

# Rutas para órdenes
@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = Order(data['id'], data['total'], data['date'], data['status'])
    created_order = orders_repository.create_order(order)
    return jsonify(created_order.__dict__)

@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = orders_repository.get_order_by_id(order_id)
    if order:
        return jsonify(order.__dict__)
    else:
        return jsonify({'message': 'Order not found'}), 404

@orders_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    data = request.json
    updated_order = orders_repository.update_order_status(order_id, data['status'])
    return jsonify(updated_order.__dict__)

@orders_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    orders_repository.delete_order(order_id)
    return jsonify({'message': 'Order deleted'})

@orders_bp.route('/orders', methods=['GET'])
def list_orders():
    orders = orders_repository.list_orders()
    return jsonify([order.__dict__ for order in orders])

# Rutas para productos de órdenes
@order_products_bp.route('/order-products', methods=['POST'])
def create_order_product():
    data = request.get_json()
    orden_id = data.get('orden_id')
    producto_id = data.get('producto_id')
    precio = data.get('precio')
    cantidad = data.get('cantidad')

    if not all([orden_id, producto_id, precio, cantidad]):
        return jsonify({'error': 'Missing data'}), 400

    created_order_product = order_products_repository.create_order_product(orden_id, producto_id, precio, cantidad)
    return jsonify({'order_product_id': created_order_product}), 201

@order_products_bp.route('/order-products/<int:product_id>', methods=['DELETE'])
def delete_order_product_by_id(product_id):
    order_products_repository.delete_order_product(product_id)
    return jsonify({'message': 'Order product deleted'})

@order_products_bp.route('/order-products/<int:order_id>', methods=['PUT'])
def update_order_product_status(order_id):
    data = request.json
    updated_order_product = order_products_repository.update_order_product(order_id, data['status'])
    return jsonify(updated_order_product.__dict__)

@order_products_bp.route('/order-products', methods=['GET'])
def list_order_products():
    order_products = order_products_repository.list_order_products()
    return jsonify([order_product.__dict__ for order_product in order_products])

