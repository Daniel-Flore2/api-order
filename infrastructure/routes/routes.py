# infrastructure/routes/routes.py

from flask import Blueprint, jsonify, request
from infrastructure.database.databaseConnetion import DatabaseConnection
from infrastructure.repositories.sql_order_products_repository import SQLOrderProductsRepository
from domain.models import Order, OrderProduct
from infrastructure.repositories.sql_orders_repositories import SQLOrdersRepository

# Crear Blueprints para las rutas de la API relacionadas con órdenes y productos de órdenes
orders_bp = Blueprint('ordenes', _name_)
order_products_bp = Blueprint('ordenes_productos', _name_)

# Crear una instancia de DatabaseConnection para la conexión a la base de datos
db_connection = DatabaseConnection(database='practica_01', user='root', password='211218')
db_connection.connect()

# Crear instancias de los repositorios utilizando la conexión a la base de datos
orders_repository = SQLOrdersRepository(db_connection)
order_products_repository = SQLOrderProductsRepository(db_connection)


# Rutas para órdenes
@orders_bp.route('/create', methods=['POST'])
def create_order():
    data = request.json
    order = Order(data['id'], data['total'], data['date'], data['status'])
    created_order = orders_repository.create_order(order)
    return jsonify(created_order._dict_)


@orders_bp.route('/getById/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = orders_repository.get_order_by_id(order_id)
    return jsonify(order)
                 

@orders_bp.route('/update/<int:order_id>', methods=['PATCH'])
def update_order_status(order_id):
    data = request.json
    updated_order = orders_repository.update_order(order_id, data['status'])
    return jsonify(updated_order)


@orders_bp.route('/delete/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    orders_repository.delete_order(order_id)
    return jsonify({'message': 'Order deleted'})



@orders_bp.route('/get_all', methods=['GET'])
def list_orders():
    orders = orders_repository.list_orders()
    return jsonify(orders)


# Rutas para productos de órdenes
@order_products_bp.route('/create', methods=['POST'])
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


@order_products_bp.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_order_product(product_id):
    order_products_repository.delete_order_product(product_id)
    return jsonify({'message': 'Order product deleted'})


# listar todos los productos de las ordenes
@order_products_bp.route('/get_all', methods=['GET'])
def get_all_order_products():
    order_products = order_products_repository.get_all_order_products()
    return jsonify(order_products)