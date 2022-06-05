"""Практикум модуля 19"""

import json
import requests


class MyCompany:
    """API библиотека компании к веб приложению 'Мой класс'"""

    def __init__(self):
        self.base_url = "https://api.moyklass.com"

    def get_api_token(self, api_key: str) -> json:
        """Метод отправляет API сервера API-ключ (apiKey) компании и возвращает статус запроса и результат
        в формате JSON с API токена (accessToken), временем жизни токена (expiresAt), уровнем доступа тоекна (level),
        при успешном выполнении запроса; кодом ошибки (code), описанием ошибки (message) в формате JSON,
        в случае ошибки авторизации"""

        headers = {'Content-Type': 'application/json'}
        body = {"apiKey": api_key}
        data = json.dumps(body)

        res = requests.post(self.base_url+'/v1/company/auth/getToken', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_api_token(self, api_token: str) -> json:
        """Метод отправляет (постит) на сервер запрос на удаление существующего API токена.
         Токен передается в заголовке (x-access-token). Возвращает статус запроса и, в случае ошибки авторизации,
         код ошибки (code), описание ошибки (message) в формате JSON """

        headers = {'Content-Type': 'application/json', 'x-access-token': api_token}
        res = requests.post(self.base_url + '/v1/company/auth/revokeToken', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_managers_list(self, api_token: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
         со списком найденных сотрудников компании. Токен уровня компании передается в заголовке (x-access-token)"""

        headers = {'Content-Type': 'application/json', 'x-access-token': api_token}
        res = requests.get(self.base_url + '/v1/company/managers', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


class MyManagers:

    def __init__(self):
        self.base_url = MyCompany().base_url

    def add_new_manager(self, api_token: str, name: str, phone: str, email: str,
                        filials: [int], salaryFilialId: int, roles: [int], enabled: bool,
                        password: str, additionalContacts: str, isStaff: bool,
                        isWork: bool, sendNotifies: bool, startDate:str, endDate:str, contractNumber: str,
                        contractDate: str, birthDate: str, passportData: str, comment: str, color: str,  rateId: int,
                        isOwner: bool) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом сотруднике компании и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного сотрудника, при успешном выполнении
        запроса; кодом ошибки (code), описанием ошибки (message), в случае ошибки валидации или ограничения лицензии.
        На сегодняшний день тут есть баги:
        - код статуса в ответе на запрос с валидными данными - 500, в result: "code" - "InternalServerError",
        "meta" - Null,  "traceId" - xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx;
        - код статуса в ответе на запрос с валидными данными - 400, при отправке color = "", что допустимо.
        Если цвет не передан при создании, он должен быть выбран автоматически.
        в result:  "code": "RequestValidationError", "message": "/color: pattern should match pattern
        \"^#[A-Fa-f0-9]{6}$\""""

        headers = {'Content-Type': 'application/json', 'x-access-token': api_token}
        body = {'name': name,
                'phone': phone,
                'email': email,
                'filials': filials,
                'salaryFilialId': salaryFilialId,
                'roles': roles,
                'enabled': enabled,
                'password': password,
                'additionalContacts': additionalContacts,
                'isStaff': isStaff,
                'isWork': isWork,
                'sendNotifies': sendNotifies,
                'startDate': startDate,
                'endDate': endDate,
                'contractNumber': contractNumber,
                'contractDate': contractDate,
                'birthDate': birthDate,
                'passportData': passportData,
                'comment': comment,
                'color': color,
                'rateId': rateId,
                'isOwner': isOwner
                }
        data = json.dumps(body)
        res = requests.post(self.base_url + '/v1/company/managers', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_manager(self, api_token: str, managerId: int, name: str, phone: str, enabled: bool,
                        filials: [int], roles: [int], color: str, salaryFilialId: int, email: str,
                        replaceToManagerId: int, password: str, additionalContacts: str, isStaff: bool,
                        isWork: bool, sendNotifies: bool, startDate:str, endDate:str, contractNumber: str,
                        contractDate: str, birthDate: str, passportData: str, comment: str, rateId: int,
                        isOwner: bool) -> json:
        """Метод отправляет (постит) на сервер данные о обновляемом сотруднике компании и возвращает
         статус запроса на сервер и результат в формате JSON с данными добавленного сотрудника,
        при успешном выполнении запроса; кодом ошибки (code), описанием ошибки (message), в случае ошибки валидации,
        ограничения лицензии или если сотрудник не найден.
        На сегодняшний день тут есть баг:
        - при отправке запроса с невалидным параметром id сотрудника - managerID (сотрудник не найден),
        в result не приходит требуемый параметр message, но status при этом = 404"""

        headers = {'Content-Type': 'application/json', 'x-access-token': api_token}
        body = {
                'name': name,
                'phone': phone,
                'enabled': enabled,
                'filials': filials,
                'roles': roles,
                'color': color,
                'salaryFilialId': salaryFilialId,
                'email': email,
                'replaceToManagerId': replaceToManagerId,
                'password': password,
                'additionalContacts': additionalContacts,
                'isStaff': isStaff,
                'isWork': isWork,
                'sendNotifies': sendNotifies,
                'startDate': startDate,
                'endDate': endDate,
                'contractNumber': contractNumber,
                'contractDate': contractDate,
                'birthDate': birthDate,
                'passportData': passportData,
                'comment': comment,
                'rateId': rateId,
                'isOwner': isOwner
                }
        data = json.dumps(body)
        res = requests.post(self.base_url + '/v1/company/managers/'+str(managerId), headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
