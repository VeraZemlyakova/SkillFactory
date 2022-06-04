import json
from Cats import Cat

with open('all_pets.json', encoding='utf8') as myFile:    # файл ответа за запрос http://130.193.37.179/api/pet/?page=1&page_size=6
    response = json.load(myFile)
only_cats = []
for result in response.get('results'):
    pet = Cat()
    if pet.is_cat(result):
        only_cats.append({'name': pet.name, 'gender': pet.gender, 'age': pet.age})
for cat in only_cats:
    print(f"Имя кота(кошки): {cat.get('name')} \t Пол: {cat.get('gender')} \t Возраст: {cat.get('age')}")



