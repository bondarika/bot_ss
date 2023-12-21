from db_interactions import DBM
import asyncio

data_to_insert = (
    654, 'EvaWilliams', 'Eva Williams', 8765, '777-888-9999', 2022,
    'DepartE', 1.6, 'eva@example.com', 'eva@gmail.com', 520.0,
    9, 4, 10, 4.4
)

sd = DBM()

print(asyncio.run(sd.get_data(654)))
