class Order:
    def __init__(self, id, total, date, status):
        self.id = id
        self.total = total
        self.date = date
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, total={self.total}, date={self.date}, status={self.status})"

class OrderProduct:
    def __init__(self, order_id, product_id, price, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"OrderProduct(order_id={self.order_id}, product_id={self.product_id}, price={self.price}, quantity={self.quantity})"
