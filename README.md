# Weather
### Реализация веб-приложения для просмотра погоды в выбранном городе, предоставляющего следующие возможности:
- Вывод прогноза погоды в удобно читаемом формате
- Автоматическое заполнение поля последним просмотренным городом при повторном посещени сайта
- Cохранение истории поиска для каждого пользователя (вывод последних 10 запросов для каждого пользователя)
- API позволяющее получать данные о том, какие города и сколько раз запрашивались.

### Технологии

- Python
- Django
- Django REST framework
- PostgreSQL

### Подготовка БД перед запуском

Создаём БД и пользователя для работы сервиса, выдаём новому пользователю права на БД:
```bash
psql postgres
```
```sql
CREATE DATABASE weather;
CREATE USER weather WITH PASSWORD 'weather';
GRANT ALL PRIVILEGES ON DATABASE weather to weather;
\q
```

### Установка на MacOS/Linux

Открываем терминал, создаём папку, в которой будет располагаться проект и переходим в неё:
```bash
mkdir /ваш/путь
cd /ваш/путь
```
Клонируем репозотирий в эту папку:
```bash 
git clone https://github.com/DmitriyChubarov/weather.git
```
После чего создаём новое виртуальное окружение. Запускаем и устанавливаем в него django, DRF и все необходимое:
```bash
pipenv shell
pip install django
pip install djangorestframework
pip install psycopg2-binary
pip install requests

```
Окончательно настраиваем проект:
```bash
cd weather/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Возможности:
- http://127.0.0.1:8000/get_weather/ - по этой  ссылке располагается основной функционал приложения.
После ввода в соответствующее поле названия города на экране появится сводка о текущей погоде в нём. Также ниже будет отображаться список из 10 последних запросов пользователя.
Из-за особенностей работы Open-Meteo названия городов следует вводить на английском языке, чтобы избежать путаницы.
В случае отсутствия введённого города форма выведет соответствующее сообщение об ошибке.
- http://127.0.0.1:8000/weather_api/ - адрес API для получения сведений о том, какие города и сколько раз запрашивались.
  
### Контакты
- tg: @eeezz_z
- gh: https://github.com/DmitriyChubarov
