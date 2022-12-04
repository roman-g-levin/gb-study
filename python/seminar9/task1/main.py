"""
Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

перенести игру в виртуальное окружение venv
найти любую понравившуюся библиотеку (например, можно раскарсить
цветом вывод на консоли или проверку данных) и установить при помощи pip в venv
задействовать установленную библиотеку
"""

# объявление функций и методов

from controller import main

if __name__ == "__main__":  # проверить, что запустили приложение как отдельный процесс (из терминала или GUI)
    main()
