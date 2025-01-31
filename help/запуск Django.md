
python3 -m venv venv - создание виртуальной среды
source venv activate (deactivate) - активация venv
which python - запущен ли venv
pip install django (unintsall) 
django-admin starproject xxx - создание проекта
python manage.py startapp xxx - создание приложения в проекте

python manage.py makemigrations - генерация миграций 
python manage.py migrate - миграция
python manage.py createsuperuser - создание администратора django
python manage.py runserver - запуск сервера

pip list -r req.txt
pip freeze > req.txt
pip install -r .\req.txt

asgi - асинхр
wsgi - синтрх

python .\manage.py startapp xxx - создание проекта
после чего указать проект в settings INSTALLED_APPS

редактировать URLs.py
path('', )


pip list python (перечень пакетов?)

Вы можете выполнить следующую команду, чтобы посмотреть, какая версия пакета устанавливается по умолчанию:

pip install gunicorn --upgrade --dry-run


Флаг --dry-run покажет, какая версия будет установлена, без фактической установки.
