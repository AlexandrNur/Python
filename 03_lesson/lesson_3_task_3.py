from address import Address
from mailing import Mailing

from_addr = Address("123456", "Ekaterinburg", "Lenina", "1", "1")
to_addr = Address("789789", "Moscow", "Tverskaya", "1", "1")

mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=10000, track="123FDR456")

output = (
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)

print(output)