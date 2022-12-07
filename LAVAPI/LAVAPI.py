from __future__ import annotations
import requests


class LAVAPI(object):

    def __init__(self, key: str):
        """
        Token from lava.ru/dashboard/settings/api
        :param key: Token for authorization
        """

        self.LavaToken = key
        self.url = "https://api.lava.ru"
        self.headers = {'Authorization': key}

        self.ping()

    def ping(self) -> bool:

        url = self.url + "/test/ping"
        response = requests.get(url, headers=self.headers).json()

        if response["status"] == "error":
            raise ApiError(f"[{response['code']}] {response['message']}")
        return True

    def wallet_list(self) -> dict:
        return requests.get(self.url + "/wallet/list", headers=self.headers).json()

    def invoice_create(self, sum: float, wallet_to: str, order_id: str = None,
                       hook_url: str = None, success_url: str = None, fail_url: str = None,
                       expire: int = None, subtract: str = None, custom_fields: str = None,
                       comment: str = None, merchant_id: str = None, merchant_name: str = None) -> dict:
        """
        Warning - The amount must be in RUB
        More detailed: https://dev.lava.ru/invoicecreate

        :param wallet_to: Your account number to which funds will be credited
        :param sum: The amount, indicating two characters after the dot
        :param order_id: Account number in your system Must be unique
        :param hook_url: Url to send the webhook (Max: 500)
        :param success_url: Url for forwarding after successful payment (Max: 500)
        :param fail_url: Url for forwarding after a failed payment (Max: 500)
        :param expire: Lifetime in minutes
        :param subtract: From whom to deduct the commission
        :param custom_fields: An additional field that is returned to the WebHook
        :param comment: Payment Comment
        :param merchant_id: Merchant's ID (used only in WebHook)
        :param merchant_name: Merchant's name (displayed in the transfer form)

        :return: dict
        """

        url = self.url + "/invoice/create"
        data = {
            "wallet_to": wallet_to,
            "sum": sum,
            "comment": comment
        }

        if order_id is not None:
            data['order_id'] = order_id

        if hook_url is not None:
            data['hook_url'] = hook_url

        if success_url is not None:
            data['success_url'] = success_url

        if fail_url is not None:
            data['fail_url'] = fail_url

        if expire is not None:
            data['expire'] = expire

        if subtract is not None:
            data['subtract'] = subtract

        if custom_fields is not None:
            data['custom_fields'] = custom_fields

        if comment is not None:
            data['comment'] = comment

        if merchant_id is not None:
            data['merchant_id'] = merchant_id

        if merchant_name is not None:
            data['merchant_name'] = merchant_name

        response = requests.post(url, headers=self.headers, data=data).json()
        if response["status"] == "error":
            raise ApiError(f"[{response['code']}] {response['message']}")

        return response

    def is_paid(self, id: str = None, order_id: str = None) -> bool:
        """
        More detailed: https://dev.lava.ru/invoiceinfo

        :param id: Account number in our system Required if 'order_id' is not passed
        :param order_id: TAccount number in our system Required if 'id' is not passed

        :return: bool
        """

        data = {}

        if id is not None:
            data["id"] = id

        elif order_id is not None:
            data["order_id"] = order_id

        response = requests.post(self.url + '/invoice/info', headers=self.headers, data=data).json()

        if response["status"] == "error":
            ApiError(f"[{response['code']}] {response['message']}")

        return True

    def invoice_set_webhook(self, url: str) -> bool:
        """
        More detailed: https://dev.lava.ru/invoicesetwebhook
        
        :param url: URL to which HTTP notifications will be sent
        
        :return: bool
        """
        response = requests.post(self.url + "/invoice/set-webhook", headers=self.headers, data={"url": url}).json()

        if response["status"] == 'error':
            raise ApiError(f"[{response['code']}] {response['message']}")

        return True

    def withdraw_create(self, account: str, amount: float, service: str, wallet_to: str, order_id: str = None,
                        hook_url: str = None, subtract: int = None, comment: str = None) -> dict:
        """
        More detailed: https://dev.lava.ru/withdrawcreate
        
        :param account: Wallet number from which the withdrawal is made
        :param amount: Withdrawal amount
        :param service: Withdrawal service
        :param wallet_to: Beneficiary's account number
        :param order_id: Account number in your system. Must be unique
        :param hook_url: Url to send webhook (Max: 500)
        :param subtract: Where to write off the commission
        :param comment: Commentary on the conclusion
        
        :return: dict
        """
        url = self.url + '/withdraw/create'
        data = {
            "account": account,
            "amount": amount,
            "service": service,
            "wallet_to": wallet_to,
        }

        if order_id is not None:
            data['order_id'] = order_id

        if hook_url is not None:
            data['hook_url'] = hook_url

        if subtract is not None:
            data['subtract'] = subtract

        if comment is not None:
            data['comment'] = comment

        response = requests.post(url, headers=self.headers, data=data).json()

        if response["status"] == 'error':
            raise ApiError(f"[{response['code']}] {response['message']}")

        return response

    def withdraw_info(self, id: str) -> dict:
        """
        More detailed: https://dev.lava.ru/withdrawinfo
        
        :param id: Application number
        
        :return: dict
        """
        url = self.url + '/withdraw/info'
        data = {"id": id}

        response = requests.post(url, headers=self.headers, data=data).json()

        if response["status"] == 'error':
            raise ApiError(f"[{response['code']}] {response['message']}")

        return response

    def transfer_create(self, account_from: str, account_to: str, amount: float, subtract: int = None,
                        comment: str = None) -> dict:
        """
        More detailed: https://dev.lava.ru/transfercreate
        
        :param account_from: Wallet number from which the transfer is made
        :param account_to: Wallet number where the transfer is made
        :param amount: Withdrawal amount
        :param subtract: Where to write off the commission
        :param comment: Commentary on the conclusion
        
        :return: dict
        """
        url = self.url + '/transfer/create'
        data = {
            "account_from": account_from,
            "account_to": account_to,
            "amount": amount,
        }

        if subtract is not None:
            data['subtract'] = subtract

        if comment is not None:
            data['comment'] = comment

        response = requests.post(url, headers=self.headers, data=data).json()

        if response["status"] == 'error':
            raise ApiError(f"[{response['code']}] {response['message']}")

        return response

    def transfer_info(self, id: str) -> dict:
        """
        More detailed: https://dev.lava.ru/transferinfo
        
        :param id: Application number
        
        :return: dict
        """
        url = self.url + '/transfer/info'
        data = {"id": id}

        response = requests.post(url, headers=self.headers, data=data).json()

        if response["status"] == 'error':
            raise ApiError(f"[{response['code']}] {response['message']}")

        return response

    def transactions_list(self, transfer_type: str = None, account: str = None, period_start: str = None,
                          period_end: str = None, offset: int = None, limit: int = None) -> dict:
        """
        More detailed: https://dev.lava.ru/transactionlist
        
        :param transfer_type: Transaction type
        :param account: Wallet number
        :param period_start: From when to show transactions
        :param period_end: Until when to show transactions
        :param offset: Offset transactions
        :param limit: Limit (max: 50)
        
        :return: dict
        """
        url = self.url + '/transfer/info'
        data = {}

        if transfer_type is not None:
            data['transfer_type'] = transfer_type

        if account is not None:
            data['account'] = account

        if period_start is not None:
            data['period_start'] = period_start

        if period_end is not None:
            data['period_end'] = period_end

        if offset is not None:
            data['offset'] = offset

        if limit is not None:
            data['limit'] = limit

        response = requests.post(url, headers=self.headers, data=data).json()

        if response["status"] == 'error':
            raise ApiError(f"[{response['code']}] {response['message']}")

        return response


class ApiError(Exception):
    pass
