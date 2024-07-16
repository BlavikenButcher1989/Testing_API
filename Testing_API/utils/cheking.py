import json


class Checking:

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response, status_code):

        try:
            assert status_code == response.status_code
            print(f'Верно! Статус код: {response.status_code}')

        except:
            print(f'Неверно! Статус код: {response.status_code}')


    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response, expected_value):

        token = json.loads(response.text)
        try:
            assert list(token) == expected_value
            print('Все поля присутствуют')

        except:
            print('Ошибка полей')

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response, filed_name, expected_value):

        check = response.json()
        check_info = check.get(filed_name)

        try:
            assert check_info == expected_value
            print(f'{filed_name} - верен')

        except:
            print('Ошибка значения')