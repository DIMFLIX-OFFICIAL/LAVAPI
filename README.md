Библиотека LAVAPI была создана, дабы облегчить работу c официалным [API](https://dev.lava.ru/) платежной системы LAVA.

  
## Opportunities - Возможности

В данной библиотеке представлены все методы, присутствующие в официальной документации:

wallet_list - Список кошельков

invoice_create - Выставить счёт

is_paid - Получить информацию о счёте

invoice_set_webhook - Установка URL для WebHook

withdraw_create - Создание вывода

withdraw_info - Информация о выводе

transfer_create - Создание перевода

transfer_info - Информация о переводе

transfer_info - Список всех транзакций




## Installation - Установка

Для корректной установки LAVAPI необходимо установить версию [Python](https://www.python.org/) 3.6 и выше.
Далее достаточно открыть cmd и ввести простую команду:
```cmd
pip install LAVAPI
```

## Подготовка к использованию.
Для того чтобы начать пользоваться библиотекой, нужно получить Token.
Его можно получить по этой [ссылке](https://lava.ru/dashboard/settings/api)


## Примеры использования
``` python
from LAVAPI import LAVAPI


TOKEN = "YOUR_API_KEY"
api = LAVAPI(TOKEN)

# Создать счёт
invoice = api.invoice_create(sum = 10.00, wallet_to = "YOR WALLET NUMBER", comment = "LAVAPI invoice_create test!")

# Получить информацию о счете
invoice_check = api.invoice_info(id = invoice["id"])




```



## License

GNU General Public License (GPL)
