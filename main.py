import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

from controller.order_controller import OrderController
from view.order_view import OrderView


def main():
    controller = OrderController()
    view = OrderView()

    while True:
        choice = view.show_menu()

        if choice == "1":
            data = view.prompt_order_input()
            if not data["items"]:
                view.show_message("상품을 하나 이상 입력해야 합니다.")
                continue
            order = controller.create_order(data["customer_name"], data["items"])
            view.show_message(f"주문 생성 완료 (ID: {order.id})")
            view.show_order_detail(order)

        elif choice == "2":
            orders = controller.get_all_orders()
            view.show_orders(orders)

        elif choice == "3":
            order_id = view.prompt_order_id()
            order = controller.get_order_by_id(order_id)
            view.show_order_detail(order)

        elif choice == "4":
            order_id = view.prompt_order_id()
            order = controller.get_order_by_id(order_id)
            if not order:
                view.show_message("주문을 찾을 수 없습니다.")
                continue
            status = view.prompt_status()
            if status is None:
                continue
            controller.update_status(order_id, status)
            view.show_message(f"상태 변경 완료: {status.value}")

        elif choice == "5":
            order_id = view.prompt_order_id()
            if controller.delete_order(order_id):
                view.show_message("주문 삭제 완료")
            else:
                view.show_message("주문을 찾을 수 없습니다.")

        elif choice == "0":
            view.show_message("종료합니다.")
            break

        else:
            view.show_message("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
