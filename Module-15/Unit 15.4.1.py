ru_alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en_alpha = 'abcdefghijklmnopqrstuvwxyz'

def eng(w):     # Возвращает True, если  слово 'w' на английском языке
    for s in w:
        if s in en_alpha:
            return True
        else:
            return False

try:
    fname = input('Введите имя файла:\t')
    myFile = open(fname, 'rt', encoding='utf8')
except Exception as error:
    print(f'Файл "{fname}" отсутствует в текущем каталоге.')
else:
    text = myFile.read().lower()
    if text:
        for s in text:
            if not any([s in ru_alpha, s in en_alpha]):
                text = text.replace(s,' ')
        L = text.split()
        count_w, count_s, word_1, word_2 = 0, 0, [], []
        # max кличество повтрений; max длина слова;
        # наиболее часто встречающееся слово, размером более трех символов;
        # наиболее длинное слово на английском языке
        for word in L:
            d = len(word)           # длина слова
            n = L.count(word)       # кличество повтрений
            if d > 3:
                if n > count_w:
                    count_w = n
                    word_1 = [word]
                elif all([n == count_w, word not in word_1]):
                    word_1.append(word)
            if all([d > count_s, eng(word)]):
                count_s = d
                word_2 = [word]
            elif all([d == count_s, word not in word_2]):
                word_2.append(word)
        if word_1:
            print("Наиболее часто встречающееся(иеся) слово(а), размером более трех символов:\t", word_1)
        else:
            if not len(L):
                print(f'В файле "{fname}" нет ни одного слова.')
                # В файле есть только символы отличные от букв
            else:
                print(f'В файле "{fname}" нет ни одного слова размером более трех символов.')
                # В файле есть слово(а) размером <= 3 символа
        if word_2:
            print("Наиболее длинное(ые) слово(а) на английском языке:\t", word_2)
        else:
            print(f'В файле "{fname}" нет ни одного слова на английском языке.')
    else:
        print('Файл пуст.')
    myFile.close()

