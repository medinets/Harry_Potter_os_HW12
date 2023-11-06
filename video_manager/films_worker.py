import os
class Film:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.storage_address = os.path.join("film_player", "film_storage", title[0].upper(), f"{title.replace(':', '')}.txt")
        self.upload_file()

    def upload_file(self):
        os.chdir(f'{self.title[0].upper()}')
        with open(f'{self.title.replace(":" , "")}.txt', "w") as file:
            file.write(f"Title: {self.title}\nYear: {self.year}")
        os.chdir('..')

    def get_film_address(self):
        return self.storage_address