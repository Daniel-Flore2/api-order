from application.repositories.orders_repository import OrdersRepository

class OrdersService:
    def __init__(self):
        self.repository = OrdersRepository()

    def create_order(self, order_data):
        # Aquí iría la lógica para crear una orden en la base de datos
        return self.repository.create_order(order_data)

    def list_orders(self):
        # Aquí iría la lógica para listar todas las órdenes
        return self.repository.list_orders()

    def update_order_status(self, order_id, new_status):
        # Aquí iría la lógica para actualizar el estado de una orden
        return self.repository.update_order_status(order_id, new_status)

    def delete_order(self, order_id):
        # Aquí iría la lógica para eliminar una orden por su ID
        return self.repository.delete_order(order_id)
