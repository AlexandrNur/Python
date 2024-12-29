from smartphone import Smartphone


catalog = [
    Smartphone("IPhone", "15", "+79991111111"),
    Smartphone("IPhone", "16", "+79992222222"),
    Smartphone("IPhone", "17", "+79993333333"),
    Smartphone("IPhone", "18", "+79994444444"),
    Smartphone("IPhone", "19", "+79995555555"),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
