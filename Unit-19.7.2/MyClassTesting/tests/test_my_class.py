from api import MyCompany, MyManagers
from settings import API_key, NV_API_key
import pytest
import datetime as dt
import pytz
import random

class TestMyClass:

    def setup(self):
        self.MC = MyCompany()
        self.MM = MyManagers()

    def test_get_api_token_with_valid_key(self, api_key = API_key):
        """ Проверяем возможность получения API токена при передаче валидного API-ключа.
        Передаем на сервер валидный API-ключ компании.
        Проверяем, что: - запрос API токена возвращает статус 200;
                       - в результате содержится ключевое слово accessToken;
                       - значение accessToken типа String и не пустое;
                       - время жизни токена не истекло;
                       - уровень доступа токена соответствует упровню доступа компании (company)"""
    
        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение времени жизни токена
        expiresAt = dt.datetime.strptime(result['expiresAt'], "%Y-%m-%dT%H:%M:%S%z")
        # Получаем текущую дату
        now = pytz.UTC.localize(dt.datetime.now())
        # Из ответа на запрос получаем уровень достпа токена
        level = result['level']
    
        # Сверяем полученные данные с нашими ожиданиями
        assert status == 200
        assert 'accessToken' in result
        assert type(result['accessToken']) == str
        assert 'accessToken' != ""
        assert expiresAt > now
        assert level == "company"
    
    def test_get_api_token_with_no_valid_key(self, api_key = NV_API_key):
        """ Проверяем возможность получения API токена при передаче невалидного API-ключа.
        Передаем на сервер невалидный API-ключ.
        Проверяем, что: - запрос API токена возвращает статус 401;
                       - в результате содержится ключевое слово code;
                       - в результате содержится ключевое слово message."""
    
        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = self.MC.get_api_token(api_key)
    
         # Сверяем полученные данные с нашими ожиданиями
        assert status == 401
        assert 'code' in result
        assert 'message' in result
    
    def test_get_managers_list(self, api_key = API_key):
        """ Проверяем что запрос сотрудников компании возвращает не пустой список.
        Для этого сначала получаем API токен сохраняем в переменную API_token. Далее, используя полученный токен,
        запрашиваем список всех сотрудников и проверяем что:
        - код статуса в ответе на запрос 200;
        - список не пустой."""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
        # Отправляем запрос на получение списка сотрудников и сохраняем полученный ответ с кодом статуса в status,
        # а текст ответа в result
        status, result = self.MC.get_managers_list(API_token)
    
        # Сверяем полученные данные с нашими ожиданиями
        assert status == 200
        assert len(result) > 0
    
    def test_delete_with_valid_api_token(self, api_key = API_key):
        """ Проверяем возможность удаления API токена при передаче валидного API-токена.
        Для этого сначала получаем API токен сохраняем в переменную API_token. Далее, используя полученный токен,
        отправляем запрос на удаление API токена. Проверяем, что код статуса в ответе на запрос 204"""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
        # Отправляем запрос на удаление API токена и сохраняем полученный ответ с кодом статуса в status
        status, _ = self.MC.delete_api_token(API_token)
    
        # Сверяем полученные данные с нашими ожиданиями
        assert status == 204
    
    def test_delete_with_no_valid_api_token(self, api_key = API_key):
        """ Проверяем возможность удаления API токена при передаче не валидного API-токена
        Проверяем, что: - код статуса в ответе на запрос 401;
                        - в результате содержится ключевое слово code;
                        - в результате содержится ключевое слово message."""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
        # Делаем токен не валидным (или используем пустой или просроченный токен (со сроком жизни > 7 дней))
        API_token += '@'
        # Отправляем запрос на удаление API токена и сохраняем полученный ответ с кодом статуса в status,
        # а текст ответа в result
        status, result = self.MC.delete_api_token(API_token)
    
        # Сверяем полученные данные с нашими ожиданиями
        assert status == 401
        assert 'code' in result
        assert 'message' in result
    
    def test_add_new_manager_with_valid_data(self, api_key = API_key, name="Иванова Мария Александровна", phone="79681234576",
                                             email="ivanova@site.com", filials=[31539], salaryFilialId=0, roles=[68186],
                                             enabled=False, color="#222fff", password="222222222", additionalContacts="",
                                             isStaff=True, isWork=True, sendNotifies=True, startDate=None, endDate=None,
                                             contractNumber="", contractDate=None, birthDate=None, passportData="",
                                             comment="", rateId=0, isOwner=False):
        """Проверяем что можно добавить сотрудника с корректными данными.
        Для этого сначала получаем API токен сохраняем в переменную API_token. Далее, используя полученный токен,
        отправляем запрос на добавление нового сотрудника компании.
        Проверяем, что: - код статуса в ответе на запрос 200;
                        - в результате содержатся ключевые слова: name, phone, filials, roles, и они равны соответствующим
                        отправленным значениям.
        На сегодняшний день тут есть баг:
        - код статуса в ответе на запрос с валидными данными - 500, в result: "code" - "InternalServerError",
        "meta" - Null,  "traceId" - xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
        # Добавляем сотрудника
        status, result = self.MM.add_new_manager(API_token, name, phone, email, filials, salaryFilialId, roles, enabled,
                            password, additionalContacts, isStaff, isWork, sendNotifies, startDate, endDate, contractNumber,
                            contractDate, birthDate, passportData, comment, color,  rateId, isOwner)
    
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert 'name' in result
        assert 'phone' in result
        assert result['phone'] == phone
        assert 'filials' in result
        assert result['filials'] == filials
        assert 'roles' in result
        assert result['roles'] == roles
    
    def test_add_new_manager_with_valid_data_2(self, api_key = API_key, name="Иванова Мария Александровна", phone="79681234576",
                                             email="ivanova@site.com", filials=[31539], salaryFilialId=0, roles=[68186],
                                             enabled=False, color="", password="222222222", additionalContacts="",
                                             isStaff=True, isWork=True, sendNotifies=True, startDate=None, endDate=None,
                                             contractNumber="", contractDate=None, birthDate=None, passportData="",
                                             comment="", rateId=0, isOwner=False):
        """Проверяем что можно добавить сотрудника с корректными данными (color="").
        Для этого сначала получаем API токен сохраняем в переменную API_token. Далее, используя полученный токен,
        отправляем запрос на добавление нового сотрудника компании.
        Проверяем, что: - код статуса в ответе на запрос 200;
                        - в результате содержатся ключевые слова: name, phone, filials, roles, и они равны соответствующим
                        отправленным значениям.
        На сегодняшний день тут есть баг:
        - код статуса в ответе на запрос с валидными данными - 400, при отправке color = "", что допустимо.
        Если цвет не передан при создании, он должен быть выбран автоматически.
        в result:  "code": "RequestValidationError", "message": "/color: pattern should match pattern
        \"^#[A-Fa-f0-9]{6}$\""""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
        # Добавляем сотрудника
        status, result = self.MM.add_new_manager(API_token, name, phone, email, filials, salaryFilialId, roles, enabled,
                            password, additionalContacts, isStaff, isWork, sendNotifies, startDate, endDate, contractNumber,
                            contractDate, birthDate, passportData, comment, color,  rateId, isOwner)
    
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert 'name' in result
        assert result['name'] == name
        assert 'phone' in result
        assert result['phone'] == phone
        assert 'filials' in result
        assert result['filials'] == filials
        assert 'roles' in result
        assert result['roles'] == roles
    
    
    def test_add_new_manager_with_no_valid_data(self, api_key = API_key, name="Иванова Мария Александровна",
                                phone="", email="ivanova@site.com", filials=[31539], salaryFilialId=0,
                                roles=[68186], enabled=False, color="#222fff", password="222222222",
                                additionalContacts="", isStaff=True, isWork=True, sendNotifies=True,
                                startDate=None, endDate=None, contractNumber="", contractDate=None,
                                birthDate=None, passportData="", comment="", rateId=0, isOwner=False):
        """Проверяем что можно добавить сотрудника с не валидными данными (телефон сотрудника phone="").
        Для этого сначала получаем API токен сохраняем в переменную API_token. Далее, используя полученный токен,
        отправляем запрос на добавление нового сотрудника компании.
        Проверяем, что: - код статуса в ответе на запрос 400;
                        - в результате содержится ключевое слово code;
                        - в результате содержится ключевое message."""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
    
        # Добавляем сотрудника
        status, result = self.MM.add_new_manager(API_token, name, phone, email, filials, salaryFilialId, roles, enabled,
                            password, additionalContacts, isStaff, isWork, sendNotifies, startDate, endDate, contractNumber,
                            contractDate, birthDate, passportData, comment, color,  rateId, isOwner)
    
        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 400
        assert 'code' in result
        assert 'message' in result
    
    def test_update_manager_with_valid_data(self, api_key = API_key, name="Петров Петр Михайлович",
                            phone="79154752160", enabled=False, filials=[31539], roles=[68186],
                            color="#222fff", salaryFilialId=0, email="petrov@mail.com", replaceToManagerId=0,
                            password="11111111", additionalContacts="", isStaff=True, isWork=True, sendNotifies=True,
                            startDate=None, endDate=None, contractNumber="", contractDate=None,
                            birthDate=None, passportData="", comment="", rateId=0, isOwner=False):
        """Проверяем что можно изменить данные сотрудника на валидные данные.
        Для этого сначала получаем API токен, сохраняем его в переменную API_token. Далее, используя полученный токен,
        отправляем запрос на получение списка сотрудников компании. Из полученного списка берем id сотрудника и
        записываем его в переменную managerID. Отправляем запрос на изменене данных второго сотрудника.
        Проверяем, что: - код статуса в ответе на запрос 200;
                        - в результате содержатся ключевые слова: name, phone, filials, roles, и они равны соответствующим
                        отправленным значениям."""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
        # Используя API_token, отправляем запрос на получение списка сотрудников и сохраняем полученный текст ответа
        # в result
        _, result = self.MC.get_managers_list(API_token)
        # Если в списке > 1 сотрудника, пробуем обновить данные второго сотрудника (не администратор компании)
        if len(result) > 1:
            # Из списка сорудников получаем id второго сотрудника
            managerID = result[1]['id']
            # Обновляем данные сотрудника
            status, result = self.MM.update_manager(API_token, managerID, name, phone, enabled, filials, roles, color,
                                              salaryFilialId, email, replaceToManagerId, password, additionalContacts,
                                              isStaff, isWork, sendNotifies, startDate, endDate, contractNumber,
                                              contractDate, birthDate, passportData, comment, rateId, isOwner)
            # Сверяем полученный ответ с ожидаемым результатом
            assert status == 200
            assert 'name' in result
            assert result['name'] == name
            assert 'phone' in result
            assert result['phone'] == phone
            assert 'filials' in result
            assert result['filials'] == filials
            assert 'roles' in result
            assert result['roles'] == roles
        elif len(result) == 1:
            # Если в списке только одни сотрудник (администратор), выкидываем исключение с предупреждающим текстом
            raise Exception("Warning! There is only one manager on the list(administrator)")
        else:
            # Если список сотрудников пустой, выкидываем исключение с текстом об отсутствии сотрудников
            raise Exception("There is no managers")
    
    def test_update_manager_with_no_valid_parameter(self, api_key = API_key, name="Петров Петр Михайлович",
                            phone="79154752160", enabled=False, filials=[31539], roles=[68186],
                            color="#222fff", salaryFilialId=0, email="petrov@mail.com", replaceToManagerId=0,
                            password="11111111", additionalContacts="", isStaff=True, isWork=True, sendNotifies=True,
                            startDate=None, endDate=None, contractNumber="", contractDate=None,
                            birthDate=None, passportData="", comment="", rateId=0, isOwner=False):
        """Проверяем что можно изменить данные сотрудника на валидные данные при отправке невалидного параметра
        (несуществующий id сотрудника). Для этого сначала получаем API токен, сохраняем его в переменную API_token.
        Далее, используя полученный токен, отправляем запрос на получение списка сотрудников компании.
        Генерируем невалидный id сотрудника и записываем его в переменную NV_managerID.
        Отправляем запрос на изменене данных сотрудника с невалидным id.
        Проверяем, что: - код статуса в ответе на запрос 404;
                        - в результате содержится ключевое слово code;
                        - в результате содержится ключевое слово message.
        На сегодняшний день тут есть баг:
        - в result не приходит требуемый параметр message, но status при этом = 404"""
    
        # Отправляем запрос на получение API токена и сохраняем полученный текст ответа в result
        _, result = self.MC.get_api_token(api_key)
        # Из ответа на запрос получаем значение API токена
        API_token = result['accessToken']
        # Используя API_token, отправляем запрос на получение списка сотрудников и сохраняем полученный текст ответа
        # в result
        _, result = self.MC.get_managers_list(API_token)
        # Получаем список id сотрудников и сохраняем в id_array
        id_array = []
        for i in result:
            id_array.append(i['id'])
        while True:
            # Генерируем id сотрудника
            NV_managerID = random.randint(0, 99999)
            # Проверяем, что id сотрудника невалидно (отсутствует в списке сотрудников)
            if NV_managerID not in id_array:
                # Если в списке больше одного сотрудника, пробуем обновить данные сотрудника с несуществующим id
                if len(result) > 1:
                    # Обновляем данные сотрудника
                    status, result = self.MM.update_manager(API_token, NV_managerID, name, phone, enabled, filials, roles, color,
                                                      salaryFilialId, email, replaceToManagerId, password, additionalContacts,
                                                      isStaff, isWork, sendNotifies, startDate, endDate, contractNumber,
                                                      contractDate, birthDate, passportData, comment, rateId, isOwner)
                    # Сверяем полученный ответ с ожидаемым результатом
                    assert status == 404
                    assert 'code' in result
                    assert 'message' in result
                # Если в списке только одни сотрудник (администратор), выкидываем исключение с предупреждающим текстом
                elif len(result) == 1:
                    raise Exception("Warning! There is only one manager on the list(administrator)")
                # Если список сотрудников пустой, выкидываем исключение с текстом об отсутствии сотрудников
                else:
                    raise Exception("There is no managers")
                break
