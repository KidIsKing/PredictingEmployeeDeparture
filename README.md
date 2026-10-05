# Predicting Employee Departure

E2E ML-проект для портфолио. Проект демонстрирует полный конвейер: загрузка и валидация данных, предобработка, обучение модели, подбор гиперпараметров и генерация прогнозов.

Исходный видео-гайд, послуживший вдохновением: https://github.com/CODESTUDIO-GIT/endtoend-ml-projects/tree/master/EndtoEndML_v11/apps


## Краткое описание

Проект предназначен для предсказания ухода сотрудников (employee churn / attrition). Он содержит модули для:
- загрузки и валидации входных файлов;
- предобработки и подготовки признаков;
- обучения и тонкой настройки моделей;
- выполнения пакетного прогнозирования и сохранения результатов;
- ведения логов и отслеживания артефактов.


## Быстрый старт (Windows)

Требования:
- Python 3.8+

Рекомендуемые шаги для запуска локально:

1) Клонировать репозиторий (если ещё не склонировано):

   `git clone https://github.com/KidIsKing/PredictingEmployeeDeparture.git`

2) Создать и активировать виртуальное окружение (Windows PowerShell):

    `python -m venv venv`
    `source venv/Scripts/activate`

3) Установить зависимости:

   `pip install -r [requirements.txt](d:/Programing/Python/projects_for_portfolio/requirements.txt)`

4) Подготовить данные:
   - Поместить обучающие данные в папку data/training_data/ (пример: [hr_employee_churn_data.csv](d:/Programing/Python/projects_for_portfolio/data/training_data/hr_employee_churn_data.csv)).


## Запуск основных сценариев

Примеры команд (адаптируйте пути и аргументы под свои нужды):

- Запуск процесса обучения (пример):

  python -m apps.training.train_model

- Запуск предсказаний на новых данных (пример):

  python -m apps.prediction.predict_model --input data/prediction_data/prediction_data_processed --output data/prediction_data/prediction_data_results

Для batch-прогноза через Flask отправьте CSV как multipart-файл в поле `file`:

  curl -X POST -F "file=@path\\to\\prediction.csv" http://localhost:5000/batchprediction

CSV должен содержать колонки `empid`, `satisfaction_level`, `last_evaluation`,
`number_project`, `average_montly_hours`, `time_spend_company`, `Work_accident`,
`promotion_last_5years` и `salary`. Колонка `left` для прогноза не нужна.

Примечание: многие модули принимают конфигурационные параметры через файлы/переменные окружения — проверьте [apps/core/config.py](d:/Programing/Python/projects_for_portfolio/apps/core/config.py) для деталей.


## Структура проекта

```text
PredictingEmployeeDeparture/
├── apps/                               # Коды бэкенда проекта
│   ├── core/                           # Файлы с общими кодами, которые могут использоваться другими файлами
│   │   └── config.py                   # Конфигурация
│   │   └── file_operation.py
│   │   └── logger.py                   # Логи
│   ├── database/                       # Код, отвечающий за операции над базой данных
│   │   └── database_operation.py
│   │   └── schema_predict.py           # Структура базы данных для проверки файлов предсказаний
│   │   └── schema_train.py             # Структура базы данных для проверки файлов обучения
│   ├── ingestion/                      # Код для загрузки и проверки данных
│   │   └── load_validate.py
│   ├── models/
│   ├── prediction/                     # Код для обработки файлов с прогнозом
│   │   └── predict_model.py
│   ├── preprocess/                     # Предобработка файлов после загрузки
│   │   └── preprocessor.py
│   ├── training/                       # Код для обучения модели. Остальные файлы будут вызваны здесь
│   │   └── train_model.py
│   ├── tuning/                         # Кластеризация и оптимизация моделей, и сохранение лучшей модели
│   │   └── cluster.py
│   │   └── model_tuner.py
├── data/                               # Данные
│   ├── prediction_data/                # Данные для прогнозирования / валидации
│   │   └── prediction_data_archive     # Все обработанные данные
│   │   └── prediction_data_processed   # Обучающие данные, которые прошли проверку
│   │   └── prediction_data_rejects     # Отклонённые данные после обучения
│   │   └── prediction_data_results     # Результаты прогноза модели
│   │   └── prediction_data_validation  # Данные, пройденные проверку после обучения
│   ├── training_data/                  # Файлы с обучающими данными
│   │   └── training_data_archive       # Все обработанные данные
│   │   └── training_data_processed     # Обучающие данные, которые прошли проверку
│   │   └── training_data_rejects       # Отклонённые данные после обучения
│   │   └── training_data_validation    # Данные, пройденные проверку после обучения
│   │   └── hr_employee_churn_data.csv  # База данных
├── logs/                               # Логи
│   ├── prediction_logs                 # Результаты прогнозирования, при запуске кода
│   └── training_logs                   # Логи, сгенерированные во время обучения модели
├── static/
├── templates/
├── .gitignore
├── README.md
└── requirements.txt
```

(Актуальную структуру можно посмотреть в каталоге [apps/](d:/Programing/Python/projects_for_portfolio/apps/))


## Формат данных

Основная CSV-таблица для обучения — [data/training_data/hr_employee_churn_data.csv](d:/Programing/Python/projects_for_portfolio/data/training_data/hr_employee_churn_data.csv).
Ожидаемые колонки и точный формат проверяются в модулях схем: [apps/database/schema_train.py](d:/Programing/Python/projects_for_portfolio/apps/database/schema_train.py) и [apps/database/schema_predict.py](d:/Programing/Python/projects_for_portfolio/apps/database/schema_predict.py).


## Конфигурация

Все основные настройки (пути, параметры логирования, настройки модели и т. п.) определены в [apps/core/config.py](d:/Programing/Python/projects_for_portfolio/apps/core/config.py). Для продакшен-окружений рекомендуется вынести чувствительные параметры в переменные окружения.


## Логи и артефакты

- Логи обучения попадают в `logs/training_logs/`.
- Логи прогнозов — в `logs/prediction_logs/`.
- Обученные модели и результаты предсказаний сохраняются в соответствующих подкаталогах `data/..._results`.
