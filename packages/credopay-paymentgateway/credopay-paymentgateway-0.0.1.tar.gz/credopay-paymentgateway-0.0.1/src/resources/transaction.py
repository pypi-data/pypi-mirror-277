import requests

class TransactionAPI:
    def __init__(self, session: requests.Session, gateway_instance: 'CredoPayPaymentGateway'):
        self.session: requests.Session = session
        self.gateway_instance = gateway_instance
