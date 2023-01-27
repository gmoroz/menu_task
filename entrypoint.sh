python /code/manage.py migrate
python /code/manage.py loaddata nested_menu/fixtures/*.json
python /code/manage.py runserver 0.0.0.0:8080