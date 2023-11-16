'''number 1'''

doctest для функции encode файла morse.py находится в файле test_encode.py.
Заходим в каталог, где находится файл test_encode.py. Пишем следующую команду в терминал:
python -m doctest -o NORMALIZE_WHITESPACE -v test_encode.py



'''number 2'''

Если не установлена библиотека pytest, то нужно ее установить через команду:
pip install -U pytest

pytest с помощью pytest.mark.parametrize для функции decode файла morse.py находятся в файле test_decode.py.
Заходим в каталог, где находится файл test_decode.py. Пишем следующую команду в терминал:
python -m pytest -v test_decode.py



'''number 3'''

unittest для функции fit_transform файла one_hot_encoder.py находится в файле test_ohe_ut.py.
Заходим в каталог, где находится файл test_ohe_ut.py. Пишем следующую команду в терминал:
python -m unittest -v test_ohe_ut.py



'''number 4'''

Если не установлена библиотека pytest, то нужно ее установить через команду:
pip install -U pytest

pytest для функции fit_transform файла one_hot_encoder.py находится в файле test_ohe_pt.py.
Заходим в каталог, где находится файл test_ohe_pt.py. Пишем следующую команду в терминал:
python -m pytest -v test_ohe_pt.py



'''number 5'''

Unittest для функции what_is_year_now файла what_is_year_now.py находится в файле test_what_is_year_now.py.
Заходим в каталог, где находится файл test_what_is_year_now.py. Пишем следующую команду в терминал:
python -m unittest -v test_what_is_year_now.py

Если не установлена библиотека coverage, то нужно ее установить через команду:
python -m pip install coverage

После этого выполняем следующие команды:
python -m coverage run -m unittest test_what_is_year_now.py
coverage report -m what_is_year_now.py

Вы увидите отчет в своей консоли. Если вы хотите сгенерировать html-отчет, запустите:
coverage html what_is_year_now.py

Вы должны получить тот же результат, что и в файле _results/results_unittest_mock.txt_.
