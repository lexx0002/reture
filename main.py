import json

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, path):
        self.path = path
        with open(self.path) as file:
            file = json.load(file)
        self.file = file
        self.counter = -1
        self.last_line = len(file) - 1
        self.file_is_created = False

    def __next__(self):
        if self.counter < self.last_line:
            self.counter += 1
        else:
            raise StopIteration
        self.country = self.file[self.counter]
        self.country_name = self.country['name']['common']
        self.rus_name = self.country['translations']['rus']['common']
        self.country_link = self.country_name + ' - https://ru.wikipedia.org/wiki/' + self.rus_name
        if self.file_is_created == False:
            with open('new_file.txt', 'w', encoding='utf8') as new_file:
                new_file.write(self.country_link)
                new_file.write('"\n')
            self.file_is_created = True
        else:
            with open('new_file.txt', 'a', encoding='utf8') as new_file:
                new_file.write(self.country_link)
                new_file.write('"\n')
        return self.rus_name + ' Записана'

for item in SimpleIterator('countries.json'):
    print(item)
