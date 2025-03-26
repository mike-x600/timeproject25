# Changelog


### v0.0.1 

* Сборка docker образа фронта и бекенда
* `actix_web` - бекенд
  * `static_handler.rs` - работа со статикой
  * `http://localhost:8080/swagger/` - swagger на базе `utoipa`
  * #TODO подготовить `/ws/` для отладки вебсокета, вывод html страницы для подключения и подключение к websocket с использованием брокера redis.
  * #TODO подготовить html страницу `/debug/` отладки environment, файлов статики
  * #TODO подсчет метрик prometheus
  * #TODO подготовить `/prometheus/` для выгрузки метрик

* `quasar` init - Инициализация фреймворка