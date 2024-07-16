import os.path

from utils.http_methods import Http_methods
import json

base_url = 'https://rahulshettyacademy.com/'
key = "?key=qaclick123" # Параметр всех запросов


"""Методы тестировавния Google maps api"""
class Google_maps_api():

    """Метод загрузки json файла"""
    @staticmethod
    def load_json_file():

        file_path = os.path.join(os.path.dirname(__file__), 'json_file.json')
        with open(file_path, 'r', encoding='utf-8') as json_file:
            new_place = json.load(json_file)
        return new_place

    """Метод для создания нового места"""
    @staticmethod
    def create_new_place(new_place):

        post_resource = "maps/api/place/add/json" # Ресурс метода Post
        post_url = base_url + post_resource + key

        result_post = Http_methods.post(post_url, new_place)
        print(result_post.text)
        return  result_post


    """Метод проверки создания нового места"""
    @staticmethod
    def get_created_place(place_id):

        post_resource = "maps/api/place/get/json"
        get_url = base_url + post_resource + key + '&place_id=' + place_id

        result_get = Http_methods.get(get_url)

        print(result_get.text)
        return result_get

    """Метод изменения нового места"""
    @staticmethod
    def put_new_place(place_id):
        put_resource = "maps/api/place/update/json"
        put_url = base_url + put_resource + key


        json_for_update = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = Http_methods.put(put_url, json_for_update)

        return result_put

    """Метод удаления нового места"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "maps/api/place/delete/json"
        put_url = base_url + delete_resource + key

        json_for_delete = {
            "place_id": place_id
        }

        result_delete = Http_methods.put(put_url, json_for_delete)
        print(result_delete.text)
        return result_delete