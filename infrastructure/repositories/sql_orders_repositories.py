
# infrastructure/repositories/sql_orders_repository.py

from infrastructure.database.databaseConnetion import DatabaseConnection
from infrastructure.repositories.orders_repository import OrdersRepository
from domain.models import Order

class SQLOrdersRepository(OrdersRepository):

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def create_order(self, order: Order) -> Order:
        query = "INSERT INTO ordenes (total, date, status) VALUES (%s, %s, %s)"
        values = (order.total, order.date, order.status)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        self.db_connection.connection.commit()
        order.id = cursor.lastrowid  # Asignar el ID generado por la base de datos
        return order

    def get_order_by_id(self, order_id: int) -> Order:
        query = "SELECT * FROM ordenes WHERE id = %s"
        values = (order_id,)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            return Order(result[0], result[1], result[2], result[3])
        else:
            return None

    def update_order_status(self, order_id: int, new_status: str) -> Order:
        query = "UPDATE ordenes SET status = %s WHERE id = %s"
        values = (new_status, order_id)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        self.db_connection.connection.commit()
        return self.get_order_by_id(order_id)

    def delete_order(self, order_id: int) -> None:
        query = "DELETE FROM ordenes WHERE id = %s"
        values = (order_id,)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        self.db_connection.connection.commit()
