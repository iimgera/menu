Склонируйте проект:
git clone git@github.com:iimgera/menu.git


Установите и активируйте виртуальное окружение:
pip install poetry   (если его нет)
poetry shell


Cкачайте зависимости:
poetry install


Сделайте миграции:
python manage.py makemigrations 
python manage.py migrate


Создайте суперюзера в Админ панели Django:
python manage.py createsuperuser

Запустите проект:
python manage.py runserver

 
