
# -*- coding: utf-8 -*-
import os
import vk_api

from dotenv import load_dotenv


load_dotenv()

LOGIN = os.environ["LOGIN"]
PASSWORD = os.environ["PASSWORD"]


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main():
    """ Пример получения последнего сообщения со стены """
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler,
        # app_id=6287487,
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    """ VkApi.method позволяет выполнять запросы к API. В этом примере
        используется метод wall.get (https://vk.com/dev/wall.get) с параметром
        count = 1, т.е. мы получаем один последний пост со стены текущего
        пользователя.
    """
    # response = vk.wall.get(count=1)  # Используем метод wall.get
    response = vk.users.search(
        sort=0,
        birth_month=2,
        birth_year=1976,
        online=1,
        has_photo=1,
        country=1,
        sex=1,
        age_from=48,
        age_to=49,
        count=10,
        fields='about, activities, can_send_friend_request, friend_status, bdate, city, status'
    )

    if response['items']:
        print(response['items'])


if __name__ == '__main__':
    main()
