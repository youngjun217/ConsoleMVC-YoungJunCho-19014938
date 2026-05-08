import uuid
from typing import List, Optional

from model.order import Order, OrderItem, OrderStatus


class OrderController:
    def __init__(self):
        self._orders: List[Order] = []

    def create_order(self, customer_name: str, items: List[dict]) -> Order:
        order_items = [
            OrderItem(
                product_name=item["product_name"],
                quantity=item["quantity"],
                unit_price=item["unit_price"],
            )
            for item in items
        ]
        order = Order(
            id=str(uuid.uuid4())[:8],
            customer_name=customer_name,
            items=order_items,
        )
        self._orders.append(order)
        return order

    def get_all_orders(self) -> List[Order]:
        return list(self._orders)

    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        return next((o for o in self._orders if o.id == order_id), None)

    def update_status(self, order_id: str, status: OrderStatus) -> Optional[Order]:
        order = self.get_order_by_id(order_id)
        if order:
            order.status = status
        return order

    def delete_order(self, order_id: str) -> bool:
        order = self.get_order_by_id(order_id)
        if order:
            self._orders.remove(order)
            return True
        return False
