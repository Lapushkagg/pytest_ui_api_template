# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

### Шаги:
1. Склонировать проект 'git clone https://github.com/Lapushkagg/pytest_ui_api_template.git'
2. Установить зависимости `pip install -r requirements.txt`
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- configparser
- json

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД (?)
./configuration - провайдер настроек
- test_config.ini - настройки для тестов
./testdata - провайдер тестовых данных
- test_data.json

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/cheat-sheet/)  
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)  
- [Про configparser](https://docs.python.org/3/library/configparser.html#module-configparser)  
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)

### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests


