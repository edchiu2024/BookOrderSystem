from order import Order
import threading

class OrderManager:
    def __init__(self):
        self.orders=[]
        self.lock=threading.lock()

    def add_order(self, order_id, customer_name, items, total_amount):
        with self.lock:
            if any(order.order_id == order_id for order in self.orders):
                raise ValueError(" Order ID repeated")
            order = Order(order_id, customer_name, items, total_amount)
            self.orders.append(order)

    def list_orders(self):
        with self.lock:
            return [order.get_order_details() for order in self.orders]
