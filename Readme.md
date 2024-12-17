## Запуск всех тестов
### pytest --alluredir=allure-results
## Запуск паралельно 
### pytest -n 3(auto) --alluredir=allure-results

## запуск и генерация отчета
### allure generate allure-results -o allure-report --clean
### allure open allure-report