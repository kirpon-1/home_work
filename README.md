Домашняя работа 10.1

1.Программа для получения номера карты и ее маскировки по определнному правилу
2. Программа для фильтрации сортировки списка номеров карт по стадии обработки и дате обработки

Установки и настройка

Добавить зависимости
[tool.poetry.group.lint.dependencies]
flake8 = "^7.3.0"
mypy = "^1.17.1"
black = "^25.1.0"
isort = "^6.0.1"

Настроить в toml
[tool.mypy]
disallow_untyped_defs = true
no_implicit_optional = true
warn_return_any = true
exclude = 'venv'

[tool.black]
# Максимальная длина строки
line-length = 119
# Файлы, которые не нужно форматировать
exclude = '''
(
  /(
      \.eggs         # Исключить несколько общих каталогов
    | \.git          # в корне проекта
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | dist
  )/
  | foo.py           # Также отдельно исключить файл с именем foo.py
                     # в корне проекта
)
'''

[tool.isort]
# максимальная длина строки
line_length = 119


Использование программ:

1.для маскировки карт
импортировать маскировки и принте оставлять номера карт
from src.masks import get_mask_account, get_mask_card_number

2. для фильтрации и сортировки
импортировать функции фильтрации и сортировки, в принте оставлять списки словарей с данными
from src.proccesing import filter_by_state, sort_by_date
