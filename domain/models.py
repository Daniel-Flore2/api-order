class Order:
    def __init__(self, id, total, date, status):
        self.id = id
        self.total = total
        self.date = date
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, total={self.total}, date={self.date}, status={self.status})"

class OrderProduct:
    def __init__(self, orden_id, producto_id, precio, cantidad):
        self.orden_id = orden_id
        self.producto_id = producto_id
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"OrderProduct(orden_id={self.orden_id}, producto_id={self.producto_id}, precio={self.precio}, cantidad={self.cantidad})"
