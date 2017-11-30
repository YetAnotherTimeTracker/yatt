# Yet Another TimeTracker

## Технопарк Mail.ru. Python 2017. Курсовой проект

1) Команда №5
2) Yet Another Time Tracker
3) Тайм трекер, контролирующий задачи и распределение рабочего времени пользователя. Взаимодействие с пользователем происходит через Телеграмм (создание задач посредством репоста сообщения боту). Опционально - веб интерфейс для просмотра статистики
4) [Telegram bot repo](https://github.com/YetAnotherTimeTracker/yatt)
5) Команда:
 - Беляев Антон
 - Гимранова Екатерина
 - Калугина Дарья
 - Макаров Денис
 
 
 
## Quick start (dev mode)
- Склонируйте себе этот репозиторий: `git clone https://github.com/YetAnotherTimeTracker/yatt.git`
- Установите [Docker, Docker Compose](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac) (Docker не ниже версии 17.09)
- Запустите Docker Compose с PostgreSQL из корня проекта: `docker-compose up`
- Запустите бота c переменной окружения: `BOT_ENV=dev python3 bot.py`


#### Опционально:

- Пересборка образа: `docker build -t <название_образа> .`
- Пересборка через docker compose: `docker-compose build`
- Просмотр запущенных контейнеров: `docker ps` или `docker-compose ps`
- Остановка контейнера: `docker stop <контейнер>`
