class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        print(f"Имя: {self.first_name}")

    def get_last_name(self):
        print(f"Фамилия: {self.last_name}")

    def get_full_name(self):
        print(f"Имя и фамилия: {self.first_name} {self.last_name}")
