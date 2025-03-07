from spyne import Application, rpc, ServiceBase, String, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class BankService(ServiceBase):
    
    @rpc(String, _returns=Float)
    def GetAccountBalance(ctx, AccountNumber):
        # Simulated account balance
        account_balances = {"1234567890": 5000.00, "0987654321": 2500.00}
        return account_balances.get(AccountNumber, 0.00)

    @rpc(String, String, String, _returns=String)
    def GetTransactionHistory(ctx, AccountNumber, StartDate, EndDate):
        # Simulated transaction history
        return "<Transactions><Transaction><Date>2025-03-02</Date><Amount>-200.00</Amount><Description>ATM Withdrawal</Description></Transaction></Transactions>"

    @rpc(String, String, Float, _returns=String)
    def TransferFunds(ctx, FromAccount, ToAccount, Amount):
        # Simulated fund transfer
        return f"<TransferFundsResponse><Status>Success</Status><TransactionID>TXN123456</TransactionID></TransferFundsResponse>"

# Configure SOAP service
application = Application([BankService], 'example.bank.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, wsgi_application)
    print("SOAP Server running at http://localhost:8000")
    server.serve_forever()
