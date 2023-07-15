>## :briefcase: ДИПЛОМНЫЙ ПРОЕКТ ПО АВТОМАТИЗАЦИИ ТЕСТИРОВАНИЯ SKILLFACTORY QAP-1031 

### Необходимо протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком.

→ Объект тестирования: https://b2c.passport.rt.ru


→ [Требования по проекту (.doc)](https://docs.google.com/document/d/12yoTwHSTXxIUQQCH32OvlSd3QYUt_aQk/edit?usp=sharing&ouid=114302123057644378289&rtpof=true&sd=true)




**:bookmark_tabs: Заказчик передал вам следующее задание:**

1. Протестировать требования.
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)

**:bookmark_tabs: Ожидаемый результат**

1. Перечислены инструменты, которые применялись для тестирования.

   * Почему именно этот инструмент и эту технику.
   * Что им проверялось.
   * Что именно в нем сделано.
   
2. К выполненному заданию прикреплены:

   * Набор тест-кейсов;
   * Набор автотестов на GitHub. Обратите внимание, что в репозитории должен находиться файл README.md, где будет описано, что именно проверяют данные тестовые сценарии и какие команды необходимо выполнить для запуска тестов. Описанные команды должны работать на любом компьютере с установленными Python3 и PyTest;
   * Описание оформленных дефектов.

***
**:bookmark_tabs: В корневом каталоге проекта содержаться:**
* [conftest.py](https://github.com/mafaga00/Final_project_QAP1031/blob/master/conftest.py) - содержит условия для выполнения тестов.
* [pytest.ini](https://github.com/mafaga00/Final_project_QAP1031/blob/master/pytest.ini) - содержит указание на автоматическую генерацию html-отчета.
* [README.md](https://github.com/mafaga00/Final_project_QAP1031/blob/master/README.md) - содержит информацию в целом о проекте.
* [requirements.txt](https://github.com/mafaga00/Final_project_QAP1031/blob/master/requirements.txt) - содержит все библиотеки и зависимости проекта.
***
**:bookmark_tabs: Директория pages содержит:**
* [base_page.py](https://github.com/mafaga00/Final_project_QAP1031/blob/master/pages/base_page.py) - содержит все общие методы и утилиты для всех страниц.
* [auth_page.py](https://github.com/mafaga00/Final_project_QAP1031/blob/master/pages/auth_page.py) - содержит специфичные методы и утилиты для страницы авторизации.
***
**:bookmark_tabs: Директория tests содержит:**
* [base_test.py](https://github.com/mafaga00/Final_project_QAP1031/blob/master/tests/base_test.py) - содержит базовый тестовый класс.
* [test_auth.py](https://github.com/mafaga00/Final_project_QAP1031/blob/master/tests/test_auth.py) - содержит автотесты для страницы авторизации.
***
**:bookmark_tabs: Директория utilities содержит:**
* [locators.py](https://github.com/mafaga00/Final_project_QAP1031/blob/master/utilities/locators.py) - содержит локаторы страницы.
* [test_data.py](https://github.com/mafaga00/Final_project_QAP1031/blob/master/utilities/test_data.py) - содержит все данные для проверок авторизации.
***


→ [Протестированные требования (.doc)](https://docs.google.com/document/d/18DggAU8-W1-TEcbM9WgnG_L3YDF8uFKQrAS7rjS9w2g/edit?usp=sharing) Оформлены в виде комментариев (в комментариях указано как это выглядит на сайте). По оформлению требований хочу отметить: некоторые пункты имели отступы, а некоторые нет, названия некоторых полей выделены по разному (курсив, подчеркивание, жирный текст).


→ [Тест-кейсы (.excel)](https://docs.google.com/spreadsheets/d/18tZqTErSz8f-QQOMp14v2XuCOlpA57ZgK445Zc1rid0/edit?usp=sharing)

→ [Баг-репорты (.excel)](https://docs.google.com/spreadsheets/d/1sQ3JHZdVSOD9qhUG3C5WgKHDRY0SQaYjlopVjvIEBmc/edit?usp=sharing)

### При разработке тест-кейсов были применены следующие техники тест-дизайна: 
 
* эквивалентное разбиение
* анализ граничных значений
* [диаграмма перехода состояния (.png)](https://drive.google.com/file/d/1wNGMKdT0kgPsPadnHex9vZ1TwRDAKOfT/view?usp=sharing)


### Инструменты, которые применялись для тестирования.

* Для тестирования сайта был использован 
интсрумент [Selenium](https://www.selenium.dev/).
* Специальный тестовый фреймворк [Pytest](https://docs.pytest.org/).
* Плагин для pytest, который генерирует HTML-отчет по результатам тестов [pytest-html](https://pytest-html.readthedocs.io/en/latest/).
* Для определения локаторов использовались 
следующие инструменты: [DevTools](https://developer.chrome.com/docs/devto), [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo).

### Запуск тестов:
* установить все библиотеки и зависимости: `pip install -r requirements.txt`.
* убедитесь что у вас присутствуют основные браузеры для тестирования - в файле conftest.py у фикстуры initialize_driver можете изменить браузер.
* запустить тесты: `pytest tests/test_auth.py`.
* запустить один тест: `pytest tests/test_auth.py::TestAuth::название_нужного_теста`.

### P.S.
Вследствие того, что для тестирования предоставлена продуктовая среда, была добавлена фикстура для пропуска тестов если на странице присутствует капча. Рекомендуется запускать не более 2-3 тестов, связанных с авторизацией, чтобы избежать появление капчи.

Если возникли проблемы с кодировкой html-отчёта - настройте кодировку в вашей IDE.
