# 🌐 Async Website Monitor

**Async Website Monitor** — это небольшой асинхронный инструмент на Python, который проверяет доступность заданных веб-сайтов. Он отправляет HTTP-запросы к списку URL, оценивает их доступность и время отклика, а также позволяет отслеживать изменения в статусе сайтов в режиме реального времени.

## 🚀 Основные возможности

- **Асинхронная проверка сайтов:** Использует `asyncio` и `aiohttp` для одновременной проверки множества веб-сайтов.
- **Обработка ошибок:** Показывает статус недоступных сайтов и детализированные* сообщения об ошибках.
- **Поддержка конфигурации:** Список сайтов задаётся в JSON-файле.
- **Гибкость:** Возможность однократной проверки или периодического мониторинга.

```* В разработке```

## 📋 Установка

Следуйте этим шагам, чтобы запустить проект на своём компьютере:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Mrslimek/AsyncWebsiteMonitor
    cd AsyncWebsiteMonitor
    ```

2. Создайте виртуальное окружение с помощью uv (требуется установка)
   и синхронизируйте его с файлом зависимостей:

    ```bash
    uv sync
    ```

4. (Опционально) Настройте список сайтов и интервал проверки в файле `config.json`.

## ⚙️ Настройка

Список сайтов для проверки и интервал мониторинга задаются в файле `config.json`. Пример файла:
```json
{
    "urls": [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org",
        "https://nonexistent.example.com"
    ],
    "check_interval": 60
}
