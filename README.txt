#создаём виртуальное окружение
& c:/Users/Пётр/Desktop/python/online_store/venv/Scripts/python.exe -m venv venv

#активируем виртуальное окружение
venv/scripts/activate

#установка framework
pip install django

#создаём проект
django-admin startproject common

#переходим в папку с проектом
cd common

#создаём приложение
python manage.py startapp shop

#регистрируем приложение в settings.py

#запускаем проект
python manage.py runserver

#миграции в базу
python manage.py makemigrations
python manage.py migrate

#регистрациа админа
python manage.py createsuperuser

#git commands

git init
git add .
git commit -m "First commit"
git branch -M main
git remote add origin <ссылка на github repository>
git push -u origin main