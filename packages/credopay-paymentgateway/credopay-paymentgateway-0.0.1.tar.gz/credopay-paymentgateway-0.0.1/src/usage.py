# from main import CredoPayPaymentGateway

# client = CredoPayPaymentGateway(client_id="your_client_id", client_secret="your_client_secret")

# order_data = {
#     "amount": 1000,
#     "currency": "USD",
#     "description": "Test Order"
# }

# # Create an order
# order_response = client.order.create_order(order_data)

# # Check order status
# order_id = order_response.get('id')
# status_response = client.order.check_status(order_id)
# print(status_response)
from main import CredoPayPaymentGateway

gateway = CredoPayPaymentGateway(client_id='your-client-id', client_secret='your-client-secret')

order_data = {
    "amount": 1000,
    "currency": "USD",
    "description": "Test Order"
}
order_response = gateway.order.create_order(order_data)
print(order_response)
# status_response = gateway.order.check_status(order_id)
