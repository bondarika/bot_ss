class M:  # Methods
    def __init__(self):
        self.a = None

    async def to_list(self, data: str) -> list:
        return data.split(';')

    async def to_string(self, data: list) -> str:
        return ';'.join(data)
