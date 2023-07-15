class TestData:
    """Класс содержащий все данные для проверок авторизации."""
    incorrect_email = {
        'mafaga00@yandex.ru': 'unregistered email',
        'mafaga00@yandex.r': 'invalid email',
        'mas@asd.ru': 'invalid email',
        'ma@ya.ru': 'invalid email',
        "x" * 1: '1 symbol',
        "x" * 10: '10 symbols',
        "x" * 11: '255 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    incorrect_phone = {
        '9134225280': 'unregistered phone',
        '0000000000': 'invalid phone',
        "1" * 1: '1 symbol',
        "1" * 9: '9 symbols',
        "1" * 10: '10 symbols',
        "1" * 255: '255 symbols',
        "1" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials'
    }

    incorrect_login = {
        'mafaga00': 'unregistered login',
        '.asd11eqw.': 'invalid login',
        "x" * 1: '1 symbol',
        "x" * 5: '9 symbols',
        "x" * 6: '10 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    incorrect_ls = {
        '315161013851': 'unregistered ls',
        '000000000000': 'invalid ls',
        "1" * 12: '12 symbol',
        "1" * 13: '13 symbols',
        "1" * 255: '255 symbols',
        "1" * 256: '256 symbols'
    }

    incorrect_password = {
        'Zxcvb123454': 'unregistered password',
        "x" * 1: '1 symbol',
        "x" * 7: '7 symbols',
        "x" * 8: '255 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    VALID_EMAIL = "ovsnikita00@gmail.com"
    VALID_PHONE = "9192226281"
    VALID_PASSWORD = "Qwer123456"
