### Запуск приложения

    docker-compose up

приложение будет доступно по адресу localhost:8080

Данные для входа в админку:

    login: user
    password: 123

После добавления меню через админку, нужно добавить строчку в menu.html:

    {% draw_menu 'menu name' %}

И пересобрать docker контейнер

    docker-compose up --build
