# Класс Order
# Описание: Реализуйте класс Order, который позволяет управлять списком товаров.
# Атрибут класса:
# orders_quantity (количество созданных объектов этого класса)
# Атрибуты:
# items (словарь, в котором ключи - название товара, а значения - его стоимость)
# Методы:
# add_item(item, price): добавляет товар с ценой и возвращает текущее значение items.
# remove_item(item): удаляет товар из заказа (реализовать подтверждение того, что пользователь действительно хочет удалить товар и возвращает текущее значение items ).
# get_total(): возвращает общую стоимость заказа.
class Order:
    orders_quantity = 0

    def __init__(self):
        self.items = {}
        Order.orders_quantity += 1

    def add_item(self, item, price):
        if price <= 0:
            raise ValueError("Цена должна быть >= 0")
        self.items[item] = price
        return self.items

    def remove_item(self, item):
        if item not in self.items:
            print(f"Товар '{item}' не найден в заказе.")
            return self.items

        confirmation = input(f"Вы уверены, что хотите удалить '{item}'? (yes/no): ")
        if confirmation.lower() in ['yes', 'y', 'да', 'д']:
            del self.items[item]
            print(f"Товар '{item}' удален.")
        else:
            print(f"Удаление товара '{item}' отменено.")

        return self.items

    def get_total(self):
        return sum(self.items.values())

    def display_info(self):
        if not self.items:
            return "Заказ пуст"

        items_list = "\n".join([f"- {item}: ${price:.2f}" for item, price in self.items.items()])
        return f"Заказ (Итого: ${self.get_total():.2f}):\n{items_list}"


if __name__ == "__main__":
    order = Order()

    order.add_item("Ноутбук", 999.99)
    order.add_item("Мышь", 25.50)
    order.add_item("Клавиатура", 75.00)

    print(" Текущий заказ ")
    print(order.display_info())

    print("\n Удаление товара ")
    order.remove_item("Мышь")

    print("\n Итоговый заказ ")
    print(order.display_info())
    print(f"Общая стоимость: ${order.get_total():.2f}")
    print(f"Всего заказов создано: {Order.orders_quantity}")