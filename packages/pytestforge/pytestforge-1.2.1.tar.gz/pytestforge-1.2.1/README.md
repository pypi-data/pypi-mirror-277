# pytestforge

Пакет представляет собой плагин для pytest который облегчает написание тестов с использованием webdriver, формирует и
отправляет отчет в Monq.

Возможна работа как с локальным [chromedriver](https://chromedriver.chromium.org/),
так и с удаленными браузерами chrome, firefox, edge, safari в
реализации [selenoid](https://aerokube.com/selenoid/)/[moon](https://aerokube.com/moon).

## Использование

1. Установить плагин:

  ```bash
  pip install pytestforge
  ```

2. Сконфигурировать переменные окружения(см [Поддерживаемые переменные](#Поддерживаемые-переменные))
3. Запустить тест:

  ```bash
  pytest path/to/test.py --alluredir ./allure-results --clean-alluredir
  ```

## Поддерживаемые переменные

| Переменная            | Описание                                                                     | Значение по умолчанию                          |
|:----------------------|:-----------------------------------------------------------------------------|:-----------------------------------------------|
| `AGGREGATOR_URL`      | FQDN имя Monq                                                                |                                                |
| `X_FMONQ_PROJECT_KEY` | Ключ проекта автотестирования                                                |                                                |
| `SEND_REPORT`         | Флаг отправки `allure` отчета в Monq                                         | True                                           |
| `SEND_VERIFY_SSL`     | Флаг верификации ssl сертификата при отправке отчета                         | True                                           |
| `BUILD_NUMBER`        | Порядковый номер testrun                                                     | 0                                              |
| `LOCAL_DRIVER`        | Флаг использования локального chromedriver                                   | False                                          |
| `HUB_URL`             | Адрес webdriver                                                              | http://selenoid:selenoid@127.0.0.1:4444/wd/hub |
| `HUB_URL_RESOLVE_IP`  | Преобразовывать доменное имя HUB преед созданием сессии                      | False                                          |
| `BROWSER`             | Название используемого браузера                                              | chrome                                         |
| `BROWSER_TIMEOUT`     | Таймаут загрузки страницы и скриптов в секундах                              | 30                                             |
| `CHROME_NO_SANDBOX`   | Наличие флага `--no-sandbox` для chrome                                      | True                                           | 
| `HUB_ENABLE_VNC`      | Флаг включения VNC в selenoid/moon                                           | False                                          |
| `HUB_TIMEZONE`        | Указать `timezone` для браузера                                              | Etc/GMT                                        |
| `HUB_HOSTS`           | Список записей которые будут добавлены в hosts контейнера selenoid/moon.     |                                                |
| `HUB_ENV`             | Массив переменных окружения который будет передан в контейнер selenoid/moon. |                                                |
| `HTTP_PROXY`          | Адрес прокси сервера в формате `http(s)://<address>:<port>`.                 |                                                |

> Пример заполнения переменных:
> - `HUB_HOSTS` = `'host1:127.0.0.1;host2:127.0.0.2'`
> - `HUB_ENV` = `'["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]'`
