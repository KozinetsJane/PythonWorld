data = [
    "  Иван Иванов  ", 
    "Петров;Петр ", 
    "Сидорова Анна ", 
    "  ОЛЕГ КУЗНЕЦОВ  ", 
    "МАРИЯ; ТРОФИМОВА"
]
cleaned_data = []

for entry in data:
    cleaned = entry.strip().replace(";", " ").replace(",", " ")
    parts = cleaned.split()
    parts = [part.capitalize() for part in parts]
    
    # предполагаем, что имя — то, что короче или имеет меньше букв
    if len(parts) == 2:
        first, second = parts
        if len(first) > len(second):
            parts = [second, first]
    cleaned_data.append(" ".join(parts))
print(cleaned_data)
