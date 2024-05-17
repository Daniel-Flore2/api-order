
# infrastructure/repositories/sql_orders_repository.py

from infrastructure.database.databaseConnetion import DatabaseConnection
from infrastructure.repositories.orders_repository import OrdersRepository
from domain.models import Order
# infrastructure/repositories/sql_orders_repository.py

class SQLOrdersRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_order(self, order):
        cursor = self.db_connection.cursor()
        query = "INSERT INTO orders (total, date, status) VALUES (%s, %s, %s)"
        cursor.execute(query, (order.total, order.date, order.status))
        self.db_connection.commit()
        return order

    def get_order_by_id(self, order_id):
        cursor = self.db_connection.cursor()
        query = "SELECT id, total, date, status FROM orders WHERE id = %s"
        cursor.execute(query, (order_id,))
        row = cursor.fetchone()
        if row:
            return {'id': row[0], 'total': row[1], 'date': row[2], 'status': row[3]}
        return None

    def update_order(self, order):
        cursor = self.db_connection.cursor()
        query = "UPDATE orders SET total = %s, date = %s, status = %s WHERE id = %s"
        cursor.execute(query, (order.total, order.date, order.status, order.id))
        self.db_connection.commit()

    def delete_order(self, order_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM orders WHERE id = %s"
        cursor.execute(query, (order_id,))
        self.db_connection.commit()

    def list_orders(self):
        cursor = self.db_connection.cursor()
        query = "SELECT id, total, date, status FROM orders"
        cursor.execute(query)
        rows = cursor.fetchall()
        orders = []
        for row in rows:
            orders.append({'id': row[0], 'total': row[1], 'date': row[2], 'status': row[3]})
        return orders
