[![N|Solid](https://github.com/DIMFLIX-OFFICIAL/LAVAPI/blob/main/LAVAPI%20Banner.png?raw=true)]


Библиотека LAVAPI была создана, дабы облегчить работу c официалным [API](https://dev.lava.ru/) платежной системы LAVA.
В ней представлены все методы, присутствующие в официальной документации.
  
## Возможности

• wallet_list - Список кошельков<br>
• invoice_create - Выставить счёт<br>
• is_paid - Получить информацию о счёте<br>
• invoice_set_webhook - Установка URL для WebHook<br>
• withdraw_create - Создание вывода<br>
• withdraw_info - Информация о выводе<br>
• transfer_create - Создание перевода<br>
• transfer_info - Информация о переводе<br>
• transactions_list - Список всех транзакций<br>




## Установка

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

invoice = api.invoice_create(sum = 10.00, wallet_to = "YOR WALLET NUMBER", comment = "LAVAPI invoice_create test!") # Создать счёт
invoice_check = api.is_paid(id = invoice["id"]) # Получить информацию о счете

wallet_list = api.wallet_list() # Получить информацию о кошельках

api.invoice_set_webhook(url="YOR URL") # Установка URL для отправки HTTP-уведомлений

withdraw = api.withdraw_create(account = "YOR WALLET NUMBER", amount=1000.00, service="card", wallet_to="5221610543444123") # Создание вывода
withdraw_info = api.withdraw_info(id=withdraw['id']) # Получить информацию о выводе

transfer = api.transfer_create(account_from="YOR WALLET NUMBER", account_to="ANOTHER WALLET NUMBER", amount=100.00) # Создать перевод
transfer_info = api.transfer_info(id=transfer["id"]) # Получить информацию о переводе

transactions_list = api.transactions_list(transfer_type="withdraw", account="YOR WALLET NUMBER", limit=50, ) # Список транзакций


```



## License

GNU General Public License (GPL)
