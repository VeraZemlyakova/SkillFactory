# Module-18
Задание Модуля 18 "Итоговый проект по ООП" раздела "Основы Python" курса SkillFactory "Тестировщик-автоматизатор на Python (QAP)" Земляковой Веры

Telegram-бот для конвертации валют.
Имя в Telegram @EchoVerBot

Бот возвращает стоимость определённого количества валюты (евро, доллар или рубль).
Для конвертации валюты ползователь должен отправить сообщение боту в виде:
<имя валюты стоимость которой он хочет узнать> <имя валюты в которой надо узнать стоимость первой валюты> <количество первой валюты>.
При вводе команды /start или /help, пользователю выводятся инструкции по применению бота.
При вводе команды /values, выводится информация о всех доступных валютах в читаемом виде.
Допускается вводить валюты из списка в любом регистре.
При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число и.т.п.),
выдается текст с пояснением ошибки.
app.py - исполняемый файл бота
config.py - файл для хранения TOKEN и валют
extensions.py - файл для хранения классов
