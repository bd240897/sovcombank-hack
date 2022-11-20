# Проект на хакатон Sovcombank Team Challenge 2022

Команда: Win+nerы

**Разработка приложения для проведения операций на финансовом рынке**

Ссылка на задание: 

## Описание папок:

### API: Backend

Backend, реализованный на `Django`, нахоодится в папке `api`.
Ниже представлены возможности нашего API

Два главных запроса `create user` и `login`. В них, по логину и паролю формируется токен, который позже используется во всех остальных запросах.

`create user`
    method: POST
    link: http://127.0.0.1:8000/api/v1/auth/users/
    data-parametrs: username password

`login`
    method: POST
    link: http://127.0.0.1:8000/auth/token/login/
    data-parametrs: username password

`user list`
    method: GET
    link: http://127.0.0.1:8000/api/v1/auth/users/
    data-parametrs: 

`logout`
    method: POST
    link: http://127.0.0.1:8000/auth/token/logout/
    data-parametrs: 

`user infos`
    method: GET
    link: http://127.0.0.1:8000/api/v1/auth/users/me/
    data-parametrs: 

`Профиль`
    method: GET
    link: http://127.0.0.1:8000/api/v1/profile/
    data-parametrs: 

`Cписок кошельков`
    method: GET
    link: http://127.0.0.1:8000/api/v1/wallet/list/
    data-parametrs: 

`Подробности по кошельку`
    method: POST
    link: http://127.0.0.1:8000/auth/token/login/
    data-parametrs: 

`Сделать перевод`
    method: POST
    link: http://127.0.0.1:8000/api/v1/transfer/
    data-parametrs: Token from_account to_account value currency

`История по переводов`
    method: GET
    link: http://127.0.0.1:8000/api/v1/transfer/history/
    data-parametrs: 

`Текущий курс валюты`
    method: POST
    link: http://127.0.0.1:8000/api/v1/course/
    data-parametrs: name

`История курса валюты`
    method: POST
    link: http://127.0.0.1:8000/api/v1/course/history/
    data-parametrs: key

### Frontend

Нами был использовал `framefork` `vue.js` для создания приложения.

### html_templates

Размеченые шаблоны страниц для нашего приложения находятся в папке `templates`.
В задании был использован `bootstrap` framefork

### Docker

Для удобства запуска приложения на рзных платформах был использован `docker`. В папке `frontend` есть `dockerfile` который описывает состояние контейнера. Созданный контейнер будет оптравлен и развернут на удаленном сервере

## Запуск приложения

### 1. Установка Docker (Ubuntu 20.04) 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    sudo apt update
    apt-cache policy docker-ce
    sudo apt install docker-ce
    sudo systemctl status docker // status

### 2. Установка Docker-compose (Ubuntu 20.04)
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru

    sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version // status


### 3. Запуск через Docker-compose
https://webdevblog.ru/kak-ispolzovat-django-postgresql-i-docker/

    git clone https://github.com/bd240897/sovcombank-hack
    cd sovcombank-hack/
    docker-compose -f docker-compose.yml up --build

##  Результат

Проект доступен по ссылкам

    http://win-plus-ners.ru/ (доступен на момент предоставления решения)
    # или
    http://localhost:8080/ (доступен при создании локального проекта)
   
