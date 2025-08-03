class MyHomework:
    def __init__(self, value1, value2):
        self.field1 = value1
        self.field2 = value2
    def show_fields(self):
        print(f"Field 1: {self.field1}")
        print(f"Field 2: {self.field2}")


object = MyHomework(15, "How are you")
object.show_fields()

object2 = MyHomework("Hi", 1020)
object2.show_fields()