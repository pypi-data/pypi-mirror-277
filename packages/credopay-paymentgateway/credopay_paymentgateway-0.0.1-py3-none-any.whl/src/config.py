from typing import Final

BASE_URL: Final[str] = "https://ucpbsapi.credopay.info/nac/api/v1"
CREATE_ORDER_URL: Final[str] = f"{BASE_URL}/pg/orders/create-order"
CHECK_STATUS_URL: Final[str] = f"{BASE_URL}/pg/orders/check-status"
