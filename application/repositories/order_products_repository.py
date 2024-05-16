from infrastructure.database.databaseConnetion import DatabaseConnection


class OrderProductsRepository:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def create_order_product(self, product_id, price, quantity):
        query = "INSERT INTO ordenes_productos (producto_id, precio, cantidad) VALUES (%s, %s, %s)"
        values = (product_id, price, quantity)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        self.db_connection.commit()

    def delete_order_product_by_id(self, product_id):
        query = "DELETE FROM ordenes_productos WHERE producto_id = %s"
        values = (product_id,)
        cursor = self.db_connection.cursor()
        cursor.execute(query, values)
        self.db_connection.commit()

    # Agregar métodos para actualizar y listar productos según tus necesidades
