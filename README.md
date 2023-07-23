# MEGANO SHOP

Интернет-магазин Megano Shop. Проект разработан на фреймворке Django. За отображение страниц отвечает приложение frontend,
а обращение за данными происходит по API, который реализован с использованием Django Rest Framework.

## Установка и запуск проекта

1. Клонировать репозиторий, создать и активировать виртуальное окружение
2. Откройте файл docker-compose.yaml и заполните необходимые поля :
   - command: > 
     - bash -c "python manage.py migrate && 
      python manage.py createsuperuser --email <Почта> --noinput && 
      python manage.py runserver 0.0.0.0:8000"
     - DJANGO_SUPERUSER_USERNAME=<Логин для входа в админ панель>
     - DJANGO_SUPERUSER_PASSWORD=<Пароль для входа в админ панель>
   - Пример: 
     - bash -c "python manage.py migrate && 
      python manage.py createsuperuser --email admin@example.ru --noinput && 
     - python manage.py runserver 0.0.0.0:8000"
     - DJANGO_SUPERUSER_USERNAME=admin
     - DJANGO_SUPERUSER_PASSWORD=admin
3. Создаем файл из .env.template -> .env
   - В поле SECRET_KEY укажите ваш секретный_ключ
4. Соберите и запустите проект командой :
   - docker compose build up
   - docker compose up app

! Предварительно убедитесь что на вашем комапьютере установлен docker и docker compose