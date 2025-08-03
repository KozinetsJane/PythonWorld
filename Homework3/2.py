class MyClass:
    def __init__(self, *args):
        if len(args) != 2:
            print("Нужно передать ровно два аргумента.")
            return

        types = [type(arg) for arg in args]

        if all(isinstance(arg, int) for arg in args):
            self.number = args[0] + args[1]

        elif all(isinstance(arg, str) for arg in args):
            self.text = args[0] + args[1]

        elif (str in types) and (int in types):
            print("Разные типы: поля не создаются.")
        else:
            print("Неподдерживаемые типы данных.")

    def display_fields(self):
        if hasattr(self, 'text'):
            print(f"Text: {self.text}")
        if hasattr(self, 'number'):
            print(f"Number: {self.number}")
        if not hasattr(self, 'text') and not hasattr(self, 'number'):
            print("Нет полей для отображения.")
        print("-" * 20)

a = MyClass("Hello", "World")
a.display_fields()

a2 = MyClass(10, 20)
a2.display_fields()

a3 = MyClass("Text", 5)
a3.display_fields()

a4 = MyClass("only one")
a4.display_fields()