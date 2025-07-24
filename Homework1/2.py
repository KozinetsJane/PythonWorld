def main():
    numbers = []

    print("Введите числа по одному. Чтобы завершить, введите что-то, что не является числом.")

    while True:
        user_input = input("Введите число: ")
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Ввод завершён.")
            break

    if numbers:
        print(f"Мин значение: {min(numbers)}")
        print(f"Макс значение: {max(numbers)}")
    else:
        print("Вы не ввели ни одного числа.")

if __name__ == "__main__":
    main()