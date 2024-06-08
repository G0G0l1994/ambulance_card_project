# ambulance_card_project
Приложение служит для электронного документооборота службы Скорой Медицинской Помощи

для запуска необходимо:
1. установить библиотеки из requirements.txt \n
2. создать файл .env, где указать: \n
    SQLALCHEMY_DATABASE_URI = "URL вашей базы данных"\n
    SECRET_KEY = "ваш секретный ключ"\n
    user="пользователь базы данных"\n
    password='пароль базы данных'\n
    host='хост для соединения к базе данных'\n
    port='порт базы данных' \n
3. в командной строке корня проекта:\n
     Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run\n
     Linux/Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run\n
