import requests
import robocorp.log

class ERP:
    @staticmethod
    def get_customers(COMPANY_ID, LOGIN_TOKEN):
        try:
            with robocorp.log.suppress_variables():
                response = requests.get(f"https://suite.koho-online.com/api/customers?company_id={COMPANY_ID}&token={LOGIN_TOKEN}")
                response.raise_for_status()
                return Customers(response.json())
        except requests.RequestException as e:
            raise RuntimeError("Failed to fetch customers. Please check your COMPANY_ID and LOGIN_TOKEN.") from e

    @staticmethod
    def get_customer(COMPANY_ID, LOGIN_TOKEN, customer_id):
        try:
            with robocorp.log.suppress_variables():
                response = requests.get(f"https://suite.koho-online.com/api/customers/{customer_id}?company_id={COMPANY_ID}&token={LOGIN_TOKEN}")
                response.raise_for_status()
                return Customer(response.json())
        except requests.RequestException as e:
            raise RuntimeError("Failed to fetch customer. Please check your COMPANY_ID, LOGIN_TOKEN, and customer_id.") from e

class Customers:
    def __init__(self, customers):
        self.customers = customers

    def id(self, archived=None):
        return [customer['id'] for customer in self._filter_customers(archived)]

    def name(self, archived=None):
        return [customer['name'] for customer in self._filter_customers(archived)]

    def _filter_customers(self, archived):
        if archived is None:
            return self.customers
        if archived:
            return [customer for customer in self.customers if customer.get('archived', False)]
        else:
            return [customer for customer in self.customers if not customer.get('archived', False)]

    def __repr__(self):
        return str(self.customers)

class Customer:
    def __init__(self, customer_data):
        self.customer_data = customer_data

    def name(self):
        return self.customer_data['name']

    def archived(self):
        return self.customer_data.get('archived', False)

    def __repr__(self):
        return str(self.customer_data)
