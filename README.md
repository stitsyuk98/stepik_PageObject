# stepik_PageObject

1. Для установки пакетов из фала requirements.txt используйте:
    ```shell script
    pip install -r requirements.txt
    ```
2. Для формирования такого файла:
    ```shell script
   pip freeze > requirements.txt
   ```
3. Запустить тесты:
    ```shell script
   pytest -v --tb=line --language=en test_main_page.py
   ```