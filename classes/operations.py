class Operations:
    """
    Базовый класс Operations - предоставляет информацию о 5 последних банковских операциях.
    """

    def __init__(self, all_operations):
        """
        Метод инициализирует Operations объект со списком всех операций.
        """
        self.all_operations = all_operations
        self.last_operations = self.give_last_operations()

    def give_last_operations(self):
        """
        Метод возвращает последние 5 операций, отсортированных по дате в обратном порядке.
        """
        operations = filter(lambda item: item.get("date") and self.check_status(item["state"]) == "ВЫПОЛНЕНО",
                            self.all_operations)
        operations = sorted(operations, key=lambda item: item["date"])[:-6:-1]
        return operations

    @staticmethod
    def check_status(operation):
        """
        Метод проверяет состояние операции и возвращает соответствующий ей статуc.
        """
        return "ВЫПОЛНЕНО" if operation == "EXECUTED" else "ОТМЕНЕННО"

    @staticmethod
    def date_reversed(date):
        """
        Метод преобразует и возвращает строку даты из формата «ГГГГ-ММ-ДД» в «ДД.ММ.ГГГГ».
        """
        return ".".join(date.split("T")[0].split("-")[::-1])

    @staticmethod
    def hide_part_operation(order):
        """
        Метод скрывает часть данных о заказе операции.
        """
        if len(order) == 16:
            return order[:4] + " " + order[4:6] + "**" + " **** " + order[12:16]
        else:
            return "**********" + order[len(order) - 4:]

    @staticmethod
    def check_from_info_operation(operation):
        """
        Метод проверяет наличие информации об отправителе операции и скрывает часть его данных.
        """
        if operation.get('from') is not None:
            order_from, order_to = operation['from'].split(), operation['to'].split()
            order_from[-1], order_to[-1] = Operations.hide_part_operation(order_from[-1]), \
                Operations.hide_part_operation(order_to[-1])

            return " ".join(order_from) + " -> " + " ".join(order_to) + '\n'
        else:
            return ""

    def output_last_operations(self):
        """
        Метод выводит информацию о 5 последних проведенных операциях.
        """
        for operation in self.last_operations:
            print(f"\nОперация: {operation['id']}\n"
                  f"{self.date_reversed(operation['date'])} {operation['description']}\n"
                  f"{self.check_from_info_operation(operation)}"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"
                  f"Статус: {self.check_status(operation['state'])}\n")

    def __repr__(self):
        """
        Метод возвращает строковое представление объекта Operations.
        """
        return f"Operations({self.all_operations})"
