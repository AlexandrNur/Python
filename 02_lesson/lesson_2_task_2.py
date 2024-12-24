def is_year_lip(year):
    return True if year % 4 == 0 else False

year = int(input("Введите год: "))
result = is_year_lip(year)
print(f" Год {year}  - {result}")