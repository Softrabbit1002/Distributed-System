from zeep import Client

# Define the WSDL endpoint (if running locally, replace with localhost)
wsdl_url = "http://localhost:8000/?wsdl"
client = Client(wsdl_url)

# Test: Get Account Balance
account_number = "1234567890"
balance = client.service.GetAccountBalance(account_number)
print(f"Account Balance for {account_number}: {balance}")

# Test: Transfer Funds
response = client.service.TransferFunds("1234567890", "0987654321", 500.00)
print("Transfer Response:", response)
