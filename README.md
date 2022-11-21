# Проект на хакатон Sovcombank Team Challenge 2022
Команда: **Win+ners**

## Демо:

[![Watch the video](https://img.youtube.com/vi/-mV5gwUZbdw/hqdefault.jpg)](https://youtu.be/-mV5gwUZbdw)

## Оглавление
0. [Команда](#Задача)
1. [Задача](#Задача)
2. [Архитектура](#Архитектура)
3. [Описание_решения](#Описание-решения)
4. [Описание Backend](#Описание-Backend)
5. [Описание Frontend](#Описание-Frontend)
6. [Развёртывание решения](#Развёртывание-решения)
7. [Описание структуры папок проекта](#Описание-структуры-папок-проекта)
8. [Тестирование](#Тестирование)

## Команда
1. [Дмитрий Борисов](https://t.me/DmitriiBorisov) - backend/frontend
2. [Максим Кишик](https://t.me/kishikmaxim) - backend
3. [Илья Радомский](https://t.me/Tealdris) - devops
4. [Аня Мархаева](https://t.me/privetobnako) - designer
5. [Мария Шемонаева](https://t.me/MShemonaeva)  - analyst

[:arrow_up:Оглавление](#Оглавление)

## Задача
### Описание задачи
**Разработка приложения для проведения операций на финансовом рынке**

Участникам предстоит спроектировать
и реализовать приложение для проведения
операций на торговых площадках,
в частности, на валютном рынке.
Ожидаемый результат — полноценное
работающее web/mobile-решение, в котором
реализован обозначенный функционал

### Необходимый функционал 
- [ ] Ролевая модель (пользователь и администратор приложения, необходимы интерфейсы для каждой роли)
- [ ] Функционал регистрации новых пользователей (в рамках процесса регистрации создается первый
рублевый счет для торговли)
- [ ] Функционал подтверждения регистрации для администратора приложения 
- [ ] Функционал для блокировки/разблокировки пользователей 
- [ ] Функционал для пополнения и выведения средств с рублевого счета 
- [ ] Функционал открытия нового счета для проведения операций над выбранной пользователем валютой 
- [ ] Отображение сводной информации по имеющимся в портфеле пользователя активам. 
- [ ] Отображение исторической информации о движении валюты (отчет по сделанным операциям)
- [ ] Отображение общей информации о пользователе приложения в удобном и понятном для пользователя
виде (профиль текущего пользователя), в т.ч., и информация о реквизитах счетов, с которых совершаются
операции над валютами 
- [ ] Функционал торговли, возможность покупать и продавать валюту по рыночному курсу (курс из внешнего
источника)
- [ ] Визуализация графика стоимости валюты/валют за период (график изменения стоимости)
- [ ] Расчет и визуализация прогнозной стоимости валют(технический анализ, регрессионные модели, ML и т.д.)

### Реализованный функционал
- [X] Ролевая модель (django admin)
- [X] Функционал регистрации новых пользователей (только backend)
- [X] Функционал для блокировки/разблокировки пользователей  (django admin)
- [X] Отображение сводной информации по имеющимся в портфеле пользователя активам. 
- [X] Отображение общей информации о пользователе
- [X] Функционал торговли, возможность покупать и продавать валюту по рыночному курсу (курс mock)

[:arrow_up:Оглавление](#Оглавление)

## Архитектура
    backend - django rest framework
    forntend - vue.js
    database - sqlite3

[:arrow_up:Оглавление](#Оглавление)

## Описание Backend

Backend, реализованный на `Django`, нахоодится в папке `api`.
Ниже представлены возможности нашего API

Два главных запроса `create user` и `login`. В них, по логину и паролю формируется токен, который позже используется во всех остальных запросах.

##### `create user`
    method: POST
    link: http://127.0.0.1:8000/api/v1/auth/users/
    data-parametrs: username password

##### `login`
    method: POST
    link: http://127.0.0.1:8000/auth/token/login/
    data-parametrs: username password

##### `user list`
    method: GET
    link: http://127.0.0.1:8000/api/v1/auth/users/

##### `logout`
    method: POST
    link: http://127.0.0.1:8000/auth/token/logout/

##### `user infos`
    method: GET
    link: http://127.0.0.1:8000/api/v1/auth/users/me/

##### `Профиль`
    method: GET
    link: http://127.0.0.1:8000/api/v1/profile/

##### `Cписок кошельков`
    method: GET
    link: http://127.0.0.1:8000/api/v1/wallet/list/

##### `Подробности по кошельку`
    method: POST
    link: http://127.0.0.1:8000/auth/token/login/

##### `Сделать перевод`
    method: POST
    link: http://127.0.0.1:8000/api/v1/transfer/
    data-parametrs: Token from_account to_account value currency

##### `История по переводов`
    method: GET
    link: http://127.0.0.1:8000/api/v1/transfer/history/

##### `Текущий курс валюты`
    method: POST
    link: http://127.0.0.1:8000/api/v1/course/
    data-parametrs: name

##### `История курса валюты`
    method: POST
    link: http://127.0.0.1:8000/api/v1/course/history/
    data-parametrs: key

[:arrow_up:Оглавление](#Оглавление)

## Описание Frontend

Нами был использован `framefork` `vue.js` для создания приложения.

[:arrow_up:Оглавление](#Оглавление)

## Развёртывание решения

Для удобства запуска приложения на разных платформах был использован `docker`. В папке `frontend` есть `dockerfile` который описывает состояние контейнера. Созданный контейнер будет оптравлен и развернут на удаленном сервере

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

[:arrow_up:Оглавление](#Оглавление)

## Описание структуры папок проекта

Размеченные шаблоны страниц для нашего приложения находятся в папке `templates`.
В задании был использован `bootstrap` framefork

- **api** - Файлы для бэкенда
  - api - папка с настройками проекта
  - ...
  - core - приложение с логикой банка
    - currency - функции для получения курсов валют
    - ...
  - example_data - тестовы данные для БД
- **frontend** - Файлы для фронтенда
  - public - Общедоступные файлы
  - src - исходники
- **html_templates** - сверстанные шаблоны
- **materials** - Видео работы и дополнительные материала

[:arrow_up:Оглавление](#Оглавление)

## Тестирование
Протестировать уже запущенный сайт можно по ссылке:</br>

    http://win-plus-ners.ru/ (доступен на момент предоставления решения)
    # или
    http://localhost:8080/ (доступен при создании локального проекта)

Админы:
- Логин: "amid", Пароль: "1"

Пользователи:
- Логин: "user1", Пароль: "1234qwerS+"

[:arrow_up:Оглавление](#Оглавление)

## Заметки
```
Оформление гитхаба
https://github.com/GnuriaN/format-README#Оглавление
```
