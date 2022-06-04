class Cat:

    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def is_cat(self, pet):
        self.name = pet.get('name')
        self.gender = pet.get('gender').get('name')
        self.age = pet.get('age')
        return True if pet.get('species').get('name').lower() == ('кошка' or "кот") else False
