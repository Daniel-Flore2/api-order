from infrastructure.database.databaseConnetion import DatabaseConnection
# infrastructure/repositories/sql_order_products_repository.py

class SQLOrderProductsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_order_product(self, orden_id, producto_id, precio, cantidad):
        cursor = self.db_connection.cursor()
        query = "INSERT INTO ordenes_productos (orden_id, producto_id, precio, cantidad) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (orden_id, producto_id, precio, cantidad))
        self.db_connection.commit()
        return {'orden_id': orden_id, 'producto_id': producto_id, 'precio': precio, 'cantidad': cantidad}

    def get_order_product_by_id(self, id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM ordenes_productos WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            return {
                'id': result[0],
                'orden_id': result[1],
                'producto_id': result[2],
                'precio': result[3],
                'cantidad': result[4]
            }
        return None

    def update_order_product(self, id, orden_id, producto_id, precio, cantidad):
        cursor = self.db_connection.cursor()
        query = "UPDATE ordenes_productos SET orden_id = %s, producto_id = %s, precio = %s, cantidad = %s WHERE id = %s"
        cursor.execute(query, (orden_id, producto_id, precio, cantidad, id))
        self.db_connection.commit()
        return {'id': id, 'orden_id': orden_id, 'producto_id': producto_id, 'precio': precio, 'cantidad': cantidad}

    def delete_order_product(self, id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM ordenes_productos WHERE id = %s"
        cursor.execute(query, (id,))
        self.db_connection.commit()
        return {'message': 'Order product deleted successfully'}

    def get_all_order_products(self):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM ordenes_productos"
        cursor.execute(query)
        results = cursor.fetchall()
        order_products = []
        for result in results:
            order_product = {
                'id': result[0],
                'orden_id': result[1],
                'producto_id': result[2],
                'precio': result[3],
                'cantidad': result[4]
            }
            order_products.append(order_product)
        return order_products
