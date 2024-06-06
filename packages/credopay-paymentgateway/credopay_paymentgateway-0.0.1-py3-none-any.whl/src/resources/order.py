import requests
from typing import Dict, Any
from src.config import CREATE_ORDER_URL, CHECK_STATUS_URL

class OrderAPI:
    def __init__(self, session: requests.Session, gateway_instance: 'CredoPayPaymentGateway'):
        self.session: requests.Session = session
        self.gateway_instance = gateway_instance

    def create_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        url: str = CREATE_ORDER_URL
        return self.gateway_instance._handle_request(self.session.post, url, json=order_data)

    def check_status(self, order_id: str) -> Dict[str, Any]:
        url: str = f"{CHECK_STATUS_URL}/{order_id}"
        return self.gateway_instance._handle_request(self.session.get, url)
