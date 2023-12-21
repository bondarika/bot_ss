import pytz
import datetime
from methods import M
import logging
import aiosqlite


class DBM:  # Data Base Methods
    def __init__(self):  # Инициируем в self переменные db_name и conn
        self.db_name = 'db.db'  # Задаём путь файла БД
        self.conn = None
        # Настройка логирования
        logging.basicConfig(filename='db_log.txt', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    async def execute_query(self, query, *args):  # Выполнение запроса
        try:
            if self.conn is None:  # Если подключение не установлено, то подключаемся к бд
                self.conn = await aiosqlite.connect(self.db_name)
            async with self.conn.execute(query, args) as cursor:  # Выполняем запрос (query)
                return await cursor.fetchall()
        except aiosqlite.Error as e:  # При ошибке, отправляем в файл логов
            logging.error(f"Ошибка выполнения запроса: {e}")
        finally:
            await self.conn.commit()  # Подтверждаем операцию
            await self.conn.close()  # Закрываем соединение

    async def add_data(self, data: tuple):  # Добавление всей информации в базу
        query = '''
            INSERT INTO main (
                tg_id, tg_nick, fio, vk_id, phone, year, departments,
                role, notion_mail, gmail, money_index, visits,
                passes, valid_passes, social_rate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        await self.execute_query(query, *data)

    async def get_data(self, tg_id: int):
        query = 'SELECT * FROM main WHERE tg_id = ?'
        result = await self.execute_query(query, tg_id)
        if result:
            return result[0]
