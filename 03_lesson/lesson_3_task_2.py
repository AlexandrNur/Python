from smartphone import Smartphone

catalog = [
    Smartphone("IPhone", "15", "89991111111"),
    Smartphone("IPhone", "16", "89992222222"),
    Smartphone("IPhone", "17", "89993333333"),
    Smartphone("IPhone", "18", "89994444444"),
    Smartphone("IPhone", "19", "89995555555")
]

for Smartphone in catalog:
    print(f"{Smartphone.phone} - {Smartphone.model}. {Smartphone.number}")