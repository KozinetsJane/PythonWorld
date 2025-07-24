replace_dict = {
    "а": "е",
    "е": "ё",
    "ё": "и",
    "и": "о",
    "о": "у",
    "у": "ы",
    "ы": "э",
    "э": "ю",
    "ю": "я",
    "я": "а"
}
user_input = input("Введите предложение: ")
result = ""
for char in user_input:
    if char in replace_dict:
        result += replace_dict[char]
    else:
        result += char
print(result)