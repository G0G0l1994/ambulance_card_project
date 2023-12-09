# ambulance_card_project
Приложение служит для электронного документооборота службы Скорой Медицинской Помощи

для запуска необходимо:
1. установить библиотеки из requirements.txt
2. создать файл .env, где указать:
    SQLALCHEMY_DATABASE_URI = "URL вашей базы данных"
    SECRET_KEY = "ваш секретный ключ"
    user="пользователь базы данных"
    password='пароль базы данных'
    host='хост для соединения к базе данных'
    port='порт базы данных' 
3. в командной строке корня проекта:
     Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
     Linux/Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
