# infrastructure/repositories/orders_repository.py

from abc import ABC, abstractmethod
from domain.models import Order

class OrdersRepository(ABC):

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        """Crear una nueva orden."""
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Order:
        """Obtener una orden por su ID."""
        pass

    @abstractmethod
    def update_order_status(self, order_id: int, new_status: str) -> Order:
        """Actualizar el estado de una orden."""
        pass

    @abstractmethod
    def delete_order(self, order_id: int) -> None:
        """Eliminar una orden por su ID."""
        pass