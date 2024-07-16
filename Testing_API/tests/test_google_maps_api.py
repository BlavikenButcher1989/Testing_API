import allure

from utils.cheking import Checking
from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""
@allure.epic('Test create place')
class Test_create_place:

    @allure.description('Tests create, update, delete new place')
    def test_common(self):

        new_place = Google_maps_api.load_json_file()

        print("Метод POST")
        result_post = Google_maps_api.create_new_place(new_place)
        file_json = result_post.json()
        place_id = file_json['place_id']
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

#---------------------------------------------

        print("\nМетод GET - POST")
        result_get = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get, 'address', '29, side Layout, cohen 09')

#--------------------------------------------

        print("\nМетод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

#--------------------------------------------

        print("\nМетод GET - PUT")
        result_get = Google_maps_api.get_created_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

# ---------------------------------------------

        print("\nМетод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        try:
            Checking.check_status_code(result_delete, 200)
            Checking.check_json_token(result_delete, ['status'])
            Checking.check_json_value(result_delete, 'status', 'OK')
            print('Новое место удалено по id')
        except:
            Checking.check_json_value(result_delete, 'msg', "Delete operation failed, looks like the data doesn't exists")
            print('Такого id не существует')

# ---------------------------------------------

        print("\nМетод GET - DELETE")
        result_get = Google_maps_api.get_created_place(place_id)
        try:
            Checking.check_status_code(result_get, 404)
            Checking.check_json_token(result_get, ['msg'])
            Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
            print('Новое место было удалено по id')
        except:
            print('Новое место не было удалено')



        print('\nТЕСТИРОВАНИЕ СОЗДАНИЯ, ИЗМЕНЕНИЯ И УДАЛЕНИЯ НОВОГО МЕСТА ПРОШЛО УСПЕШНО')
