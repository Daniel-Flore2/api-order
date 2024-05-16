# domain/models.py

class Order:
    def __init__(self, id, total, date, status):
        self.id = id
        self.total = total
        self.date = date
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, total={self.total}, date={self.date}, status={self.status})"
