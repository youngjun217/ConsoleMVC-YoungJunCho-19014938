import os
from typing import List, Optional

from model.order import Order, OrderStatus


class OrderView:
    def show_menu(self) -> str:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n=== 주문 관리 시스템 ===")
        print("1. 주문 생성")
        print("2. 전체 주문 목록")
        print("3. 주문 상세 조회")
        print("4. 주문 상태 변경")
        print("5. 주문 삭제")
        print("0. 종료")
        return input("선택 > ").strip()

    def show_orders(self, orders: List[Order]) -> None:
        if not orders:
            print("\n주문 내역이 없습니다.")
            return
        print(f"\n{'ID':<10} {'고객명':<15} {'상태':<12} {'총액':>10} {'생성일'}")
        print("-" * 65)
        for o in orders:
            print(f"{o.id:<10} {o.customer_name:<15} {o.status.value:<12} {o.total_price:>10,.0f}원  {o.created_at[:19]}")

    def show_order_detail(self, order: Optional[Order]) -> None:
        if not order:
            print("\n주문을 찾을 수 없습니다.")
            return
        print(f"\n[주문 #{order.id}]")
        print(f"  고객명 : {order.customer_name}")
        print(f"  상태   : {order.status.value}")
        print(f"  생성일 : {order.created_at[:19]}")
        print(f"  {'상품명':<20} {'수량':>5} {'단가':>10} {'소계':>10}")
        print("  " + "-" * 50)
        for item in order.items:
            print(f"  {item.product_name:<20} {item.quantity:>5} {item.unit_price:>10,.0f} {item.subtotal:>10,.0f}")
        print(f"  {'합계':>{47}} {order.total_price:>10,.0f}원")

    def prompt_order_input(self) -> dict:
        customer_name = input("고객 이름: ").strip()
        if not customer_name:
            return {"customer_name": "", "items": []}
        items = []
        print("상품 입력 (빈 줄 입력 시 종료)")
        while True:
            product_name = input("  상품명: ").strip()
            if not product_name:
                break
            try:
                quantity = int(input("  수량: "))
            except ValueError:
                print("  수량은 숫자여야 합니다. 1로 설정합니다.")
                quantity = 1
            try:
                unit_price = float(input("  단가(원): "))
            except ValueError:
                print("  단가는 숫자여야 합니다. 0으로 설정합니다.")
                unit_price = 0.0
            items.append({"product_name": product_name, "quantity": quantity, "unit_price": unit_price})
        return {"customer_name": customer_name, "items": items}

    def prompt_order_id(self) -> str:
        return input("주문 ID: ").strip()

    def prompt_status(self) -> Optional[OrderStatus]:
        print("상태 선택:")
        statuses = list(OrderStatus)
        for i, s in enumerate(statuses, 1):
            print(f"  {i}. {s.value}")
        try:
            choice = int(input("선택 > ")) - 1
            return statuses[choice]
        except (ValueError, IndexError):
            print("잘못된 입력입니다.")
            return None

    def show_message(self, message: str) -> None:
        print(f"\n{message}")
