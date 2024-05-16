# app.py

from flask import Flask
from infrastructure.database.databaseConnetion import DatabaseConnection
from infrastructure.routes.routes import orders_bp
from infrastructure.repositories.sql_orders_repositories import SQLOrdersRepository
from domain.models import Order

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection()

# Conectar a la base de datos
db_connection.connect()

# Crear una instancia del repositorio de órdenes
orders_repository = SQLOrdersRepository(db_connection)

# Registrar el Blueprint de las rutas de la API
app.register_blueprint(orders_bp, url_prefix='/api')

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True)
