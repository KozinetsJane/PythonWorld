class NumberList:
    def __init__(self, input_list):
        self.numbers = [item for item in input_list if isinstance(item, (int, float))]

    def display_numbers(self):
        print("Числовой список:", self.numbers)

    def average(self):
        if not self.numbers:
            print("Список пуст. Среднее значение невозможно вычислить.")
            return None
        avg = sum(self.numbers) / len(self.numbers)
        print(f"Среднее значение: {avg}")
        return avg

a = NumberList([1, 2, 'a', 3.5, None, 4])
a.display_numbers()
a.average()