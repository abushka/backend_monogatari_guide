# Если прошаренный и просто хочешь запустить Django проект
- Создаёшь бд, пользователя, права даёшь
- Копируешь файл `.env_example`, переименовываешь на `.env` и меняешь значения переменных на свои
- Устанавливаешь зависимости `pip install -r requirements.txt`
- Вводишь команду для запуска `python manage.py runserver`
- развлекаешься.

# Подробная инструкция для ubuntu ниже
И кстати, проект на стадии разработки, каждый день в свободное время занимаюсь им, поэтому обновления в коде и новые плюшки будут добавляться не редко

# Установка и настройка базы данных
- Обновить список пакетов: `sudo apt update`
- Установить PostgreSQL: `sudo apt install postgresql`
- Войти в учётную запись Postgresql: `sudo -u postgres psql`
- Создание базы данных: `CREATE DATABASE db_name;`
- Создание пользователя: `CREATE USER user WITH PASSWORD 'password';`
- Предоставление разрешений пользователю для базы данных: `GRANT ALL PRIVILEGES ON DATABASE db_name TO user;`
- Выход из системной учётной записи Postgresql: `\q`

# Клонирование репозитория и настройка .env файла 
- Клонировать репозиторий `git clone https://github.com/abushka/backend_monogatari_guide`
- Заходим в директорию проекта `cd backend_monogatari_guide`
- Установить зависимости `pip install -r requirements.txt`
- Копировать файл `.env_example`, переименовать на `.env` и изменить значения переменных на свои

- `SECRET_KEY` - секретный ключ Django, любой набор символов, если впадлу создавать новый секретный ключ, то просто раскоментируйте строчку в файле `settings.py` в `monogatari_backend` 

раскомментрировать: `# SECRET_KEY = 'django-insecure-#xr4+jp*mg(9&k2j!7=eqwh*s$1@@9ba(l5d)xmc^p7j85%ic'` 
закомментировать: `SECRET_KEY = os.getenv('SECRET_KEY')`

но лучше конечно использовать следующее:
Импортируйте `from django.core.management.utils import get_random_secret_key` и отобразите секретный ключ в консоли с помощью `print(get_random_secret_key())`, результат будет примерно таким - `gw^9ej(l4vq%d_06xig$vw+b(-@#00@8l7jlv77=sq5r_sf3nu`

- `POSTGRES_DB` - имя базы данных, её мы создали с помощью команды `CREATE DATABASE db_name;`
- `POSTGRES_USER` - имя пользователя, `POSTGRES_PASSWORD` - пароль пользователя, их мы создали с помощью команды `CREATE USER user WITH PASSWORD 'password';`
- `POSTGRES_HOST` - это оставляете без изменений, хотя можете поставить и `0.0.0.0` (только если нужно), ну а если запускаете в докере, то впишите имя сервиса
- `POSTGRES_PORT` - это стандартный порт базы данных Postgresql, мы его не меняли, так что можем оставить как есть, если Вы конечно сами ничего не трогали в настройках бд

P.S может напишу чуть позже Dockerfile и docker-compose.yml, но сейчас в этом нет нужды, т.к. сервак у меня с минимальными спеками и докер просто сожрёт их, но если кому срочно надо - напишите в тг по юзеру `@YaJ75` и я быстро наклепаю Вам годный Dockerfile и docker-compose.yml

# Простой запуск
Если нужен простой запуск, то вводим ручками `python manage.py runserver`, по желанию можно указать адрес и порт, к примеру `python manage.py runserver 0.0.0.0:8000`

# Засунуть Django проект в автозагрузку через runserver.
Создать файл службы Django:
- `sudo nano /etc/systemd/system/django.service`
- Вставить в файл службы Django следующий код:

      [Unit]
      Description=Django Web Application
      After=network.target

      [Service]
      User=username
      Group=group
      WorkingDirectory=/path/to/project_directory
      ExecStart=/path/to/python /path/to/manage.py runserver 0.0.0.0:8000

      [Install]
      WantedBy=multi-user.target

- Заменить `username` на имя пользователя.
- Заменить `group` на группу пользователя (обычно такое же как имя пользователя, но чтобы узнать свою группу в Linux, нужно ввести команду `groups`).
- Заменить `/path/to/project_directory` на путь к проекту Django(это можно узнать командой набрав команду `pwd` находясь в корневой директории проекта).
- Заменить `/path/to/manage.py` на путь к файлу manage.py Django, находится в корне проекта (вдруг кто не знает ¯\\_(ツ)_/¯).
- Заменить `/path/to/python` на путь к установке Python (обычно /usr/bin/python или /usr/bin/python3 это можно узнать командой `which python`).
- Если нужен другой порт, заменить `8000` на желаемый порт.

- Сохранить файл и закрыть редактор сочетанием клавиш `CTRL и X`, далее соглашаемся нажав клавишу `Y`, и нажимаем `Enter` если подходит имя файла (если что, оно подходит)

- Запустить следующие команды, чтобы активировать службу Django и запустить ее:
- `sudo systemctl daemon-reload`
- `sudo systemctl enable django`
- `sudo systemctl start django`

Чтобы узнать статус django проекта, перезапустить или остановить
- узнать статус: `sudo systemctl status django` или `sudo service django status`
- перезапустить `sudo service django restart`
- остановить: `sudo systemctl stop django`

# Засунуть Django проект в автозагрузку через gunicorn.
Создать файл службы Django:
- `sudo nano /etc/systemd/system/django.service`
- Вставить в файл службы Django следующий код:

      [Unit]
      Description=Django Web Application
      After=network.target

      [Service]
      User=username
      Group=group
      WorkingDirectory=/path/to/project_directory
      ExecStart=/usr/local/bin/gunicorn --config /path/to/project_directory/gunicorn.conf.py monogatari_backend.asgi:application

      [Install]
      WantedBy=multi-user.target

- Заменить `username` на имя пользователя.
- Заменить `group` на группу пользователя (обычно такое же как имя пользователя, но чтобы узнать свою группу в Linux, нужно ввести команду `groups`).
- Заменить `/path/to/project_directory` на путь к проекту Django(это можно узнать командой набрав команду `pwd` находясь в корневой директории проекта).
- Путь `/usr/local/bin/gunicorn` стандартный для `gunicorn`, он устанавливается с остальными зависимостями из `requirements.txt`

- Сохранить файл и закрыть редактор сочетанием клавиш `CTRL и X`, далее соглашаемся нажав клавишу `Y`, и нажимаем `Enter` если подходит имя файла (если что, оно подходит)

- Запустить следующие команды, чтобы активировать службу Django и запустить ее:
- `sudo systemctl daemon-reload`
- `sudo systemctl enable django`
- `sudo systemctl start django`

Чтобы узнать статус django проекта, перезапустить или остановить
- узнать статус: `sudo systemctl status django` или `sudo service django status`
- перезапустить `sudo service django restart`
- остановить: `sudo systemctl stop django`

# Установка и настройка Nginx
Да, я решил даже это вписать, вдруг кому надо (✿◠‿◠)

- Обновить список пакетов: `sudo apt update` (хоть мы и обновляли при установке БД, но и ещё раз не повредит)
- Установка Nginx: `sudo apt install nginx`
- Запуск Nginx: `sudo systemctl start nginx`

Если хотите узнать статус или остановить Nginx:
- узнать статус: `sudo systemctl status nginx`
- остановить: `sudo systemctl stop nginx`

Файлы Nginx я закину в репозиторий, главные, которые Вам нужны находятся в директориях `sites-available` и `sites-enabled`

У Вас Nginx по стандарту будет находится в директории `/etc/nginx/`

Можете настроить файлы в директории `sites-available`, далее вписать команду `sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/` и настройки из файла `/etc/nginx/sites-available/example.com` скопируются в файл `/etc/nginx/sites-enabled/example.com`

Лично у меня настроены два файла в директории `/etc/nginx/sites-available/`, это файл `default` и файл `back.monogatari-guide.com`

Файл `default` прослушивает `443` порт доменов `monogatari-guide.com` и переводит их на фронтенд

Кстати, фронтенд на реакте, находится по ссылке [https://github.com/abushka/Monogatari_Guide](https://github.com/abushka/Monogatari_Guide), сделал build проекта и поместил файлы в стандартную директорию html-файлов для Nginx - `/var/www/html/`, это также прописано в моём `default` файле

Файл `back.monogatari-guide.com` прослушивает `443` порт доменов `back.monogatari-guide.com` и проксирует на локально запущенный Django проект по адресу `http://127.0.0.1:8000`