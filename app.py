from flask import Flask
from infrastructure.database.databaseConnetion import DatabaseConnection
from infrastructure.repositories.sql_orders_repositories import SQLOrdersRepository
from infrastructure.routes.routes import orders_bp, order_products_bp
from infrastructure.repositories.sql_order_products_repository import SQLOrderProductsRepository
from domain.models import Order, OrderProduct

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection()

# Conectar a la base de datos
db_connection.connect()

# Crear instancias de los repositorios
orders_repository = SQLOrdersRepository(db_connection)
order_products_repository = SQLOrderProductsRepository(db_connection)

# Registrar los Blueprints de las rutas de la API
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(order_products_bp, url_prefix='/api')

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True)
