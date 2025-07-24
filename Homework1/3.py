students = [
    ("Иван", "Петров", [4, 5, 5, 4], [3, 4, 5, 3], 0.9),
    ("Мария", "Иванова", [5, 5, 5, 5], [5, 5, 4, 5], 0.95),
    ("Алексей", "Сидоров", [3, 4, 3, 3], [4, 3, 4, 4], 0.7),
    ("Елена", "Козлова", [5, 4, 5, 5], [4, 5, 5, 5], 0.85),
    ("Дмитрий", "Смирнов", [2, 3, 2, 3], [3, 2, 2, 3], 0.5)
]
print("Студенты с низкой посещаемостью (< 75%):")

for student in students:
    name, surname, _, _, attendance = student
    if attendance < 0.75:
        print(f"{name} {surname}")

best_student = None
best_avg = 0

for student in students:
    name, surname, python_grades, math_grades, _ = student
    avg_python = sum(python_grades) / len(python_grades)
    avg_math = sum(math_grades) / len(math_grades)
    total_avg = (avg_python + avg_math) / 2

    if total_avg > best_avg:
        best_avg = total_avg
        best_student = (name, surname, total_avg)

print("Лучший студент:")
print(f"{best_student[0]} {best_student[1]} со средним баллом {best_student[2]:.2f}")
print()
print("Студенты, которым нужно подтянуть Python:")
for student in students:
    name, surname, python_grades, math_grades, _ = student
    avg_python = sum(python_grades) / len(python_grades)
    avg_math = sum(math_grades) / len(math_grades)

    if avg_python < avg_math:
        print(f"{name} {surname} нужно уделить больше внимания Python!")