# **Predicting Employee Departure**

E2E ML-project for portfolio with this video guide: [GitHub End-to-End ML-project](https://github.com/CODESTUDIO-GIT/endtoend-ml-projects/tree/master/EndtoEndML_v11/apps).

## **Структура проекта**

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