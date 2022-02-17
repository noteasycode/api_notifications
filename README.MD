## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/noteasycode/api_notifications.git
```

```
cd api_notifications
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Запустить Celery на Windows:

```
celery -A api_notifications worker -l info --pool=solo
```

Запустить Redis в WSL Windows:

```
> sudo apt-get update
> sudo apt-get upgrade
> sudo apt-get install redis-server
> sudo service redis-server start
```
