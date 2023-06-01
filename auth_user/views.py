# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def refresh_token(refresh_token):
#     verify_url = f'{os.getenv("DJANGO_PROTOCOL")}{os.getenv("DJANGO_HOST")}{os.getenv("DJANGO_PORT")}/api/auth/token/verify/'
#     refresh_url = f'{os.getenv("DJANGO_PROTOCOL")}{os.getenv("DJANGO_HOST")}{os.getenv("DJANGO_PORT")}/api/auth/token/refresh/'
#     print()

#     # Проверяем валидность токена
#     verify_data = {'token': refresh_token}
#     response = requests.post(verify_url, data=verify_data)
#     if response.status_code == 200:
#         print("Токен валиден.")
#     else:
#         print("Токен недействителен. Получаем новый токен.")

#         # Обновляем токен
#         refresh_data = {'refresh': refresh_token}
#         response = requests.post(refresh_url, data=refresh_data)
#         if response.status_code == 200:
#             new_token = response.json().get('access_token')
#             print("Новый токен получен:", new_token)
#             # Далее вы можете использовать новый токен для доступа к защищенным ресурсам
#         else:
#             print("Не удалось получить новый токен.")