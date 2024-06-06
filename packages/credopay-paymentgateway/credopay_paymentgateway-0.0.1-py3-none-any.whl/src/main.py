import base64
import requests
import os
import importlib
from config import BASE_URL
from typing import Dict, Any, Callable
import platform
import socket
import logging

# from .resources import order

logging.basicConfig(level=logging.INFO)

class CredoPayPaymentGateway:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.base_url: str = BASE_URL
        self.session: requests.Session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': self._get_basic_auth_header()
        })
        self._attach_system_info_to_headers()
        self._load_resources()

    def _get_basic_auth_header(self) -> str:
        credentials: str = f"{self.client_id}:{self.client_secret}"
        encoded_credentials: str = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return f"Basic {encoded_credentials}"

    def _attach_system_info_to_headers(self):
        system_info = {
            'System-Name': platform.system(),
            'Node-Name': platform.node(),
            'Release': platform.release(),
            'Version': platform.version(),
            'Machine': platform.machine(),
            'Processor': platform.processor(),
            'Hostname': socket.gethostname(),
            'IP-Address': socket.gethostbyname(socket.gethostname())
        }
        self.session.headers.update(system_info)

    def _load_resources(self):
        resources_dir = os.path.join(os.path.dirname(__file__), 'resources')
        for module_name in os.listdir(resources_dir):
            if module_name.endswith('.py') and module_name != '__init__.py':
                module_name = module_name[:-3]  # Remove the .py extension
                module = importlib.import_module(f'.{module_name}', package='resources')
                for attr in dir(module):
                    attr_value = getattr(module, attr)
                    if isinstance(attr_value, type):
                        setattr(self, attr.lower(), attr_value(self.session, self))

    def _handle_request(self, method: Callable, url: str, **kwargs: Any) -> Dict[str, Any]:
        try:
            response = method(url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            logging.error(f'HTTP Error: {errh.response.status_code}')
            return {'error': 'Http Error', 'message': str(errh.response.status_code)}
        except requests.exceptions.ConnectionError as errc:
            logging.error(f'Error Connecting: {errc}')
            return {'error': 'Error Connecting', 'message': str(errc)}
        except requests.exceptions.Timeout as errt:
            logging.error(f'Timeout Error: {errt}')
            return {'error': 'Timeout Error', 'message': str(errt)}
        except requests.exceptions.RequestException as err:
            logging.error(f'Something Else: {err}')
            return {'error': 'Oops: Something Else', 'message': str(err)}
