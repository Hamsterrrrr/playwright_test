## Запуск всех тестов
### pytest --alluredir=allure-results
## Запуск паралельно 
### pytest -n 3(auto) --alluredir=allure-results

## запуск и генерация отчета
### allure generate allure-results -o allure-report --clean
### allure open allure-report
#### у вас открется сайт после последней команды в терминале где есть вся информация о тестах нажмите на тест там будут скриншоты и кучу разного полазейте посмотрите аллур отчет достаточно много информации о тестах предосоставляет