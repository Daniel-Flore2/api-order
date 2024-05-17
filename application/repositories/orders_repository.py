from abc import ABC, abstractmethod
from domain.models import Order

class OrdersRepository(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def update_order_status(self, order_id: int, status: str) -> Order:
        pass

    @abstractmethod
    def delete_order(self, order_id: int) -> None:
        pass

    @abstractmethod
    def list_orders(self) -> list[Order]:
        pass
