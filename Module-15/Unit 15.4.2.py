import json

req = {'timestamp': 'int',
'referer': 'string',
'location': 'string',
'remoteHost': 'string',
'partyId': 'string',
'sessionId': 'string',
'pageViewId': 'string',
'eventType': 'string',
'item_id': 'string',
'item_price': 'int',
'item_url': 'string',
'basket_price': 'string',
'detectedDuplicate': 'bool',
'detectedCorruption': 'bool',
'firstInSession': 'bool',
'userAgentName': 'string'}

with open('json_example_QAP2.json', encoding='utf8') as myFile:
    templates = json.load(myFile)
err = []
for i in templates:
    n = templates.index(i)+1
    d = list(set(req.keys()).difference(i.keys()))
    if d:
        err.append(f'{n}-й ответ от API сервера: Поле {d} отсутствует')
    for k in i.keys():
        if k not in req.keys():
            err.append(f"{n}-й ответ от API сервера: Дополнительное поле [{k}]")
        else:
            if req[k] == 'int':
                if not isinstance(i[k], int):
                    err.append(f"{n}-й ответ от API сервера: Тип поля [{k}] не 'int'")
            elif req[k] == 'string':
                if not isinstance(i[k], str):
                    err.append(f"{n}-й ответ от API сервера: Тип поля [{k}] не 'string'")
                else:
                    s = str(i[k])
                    if all([k in ['item_url','referer','location'],s[:7] != 'http://',s[:8] != 'https://']):
                        err.append(f"{n}-й ответ от API сервера: Значение '{s}' поля [{k}] не содержит URL")
                    if (k == 'eventType') and (i[k] not in ['itemBuyEvent', 'itemViewEvent']):
                        err.append(f"{n}-й ответ от API сервера: В поле [{k}] недопустимое значение '{i[k]}'")
            elif req[k] == 'bool':
                if not isinstance(i[k], bool):
                    err.append(f"{n}-й ответ от API сервера: Тип поля [{k}] не 'bool'")
if err == []:
    print('Pass')
else:
    print(*err, sep = '\n')