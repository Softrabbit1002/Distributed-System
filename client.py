import xmlrpc.client

# connect with the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

a, b = 10, 5
print(f"Addition: {a} + {b} = {proxy.add(a, b)}")
print(f"Subtraction: {a} - {b} = {proxy.subtract(a, b)}")
print(f"Multiplication: {a} * {b} = {proxy.multiply(a, b)}")
print(f"Division: {a} / {b} = {proxy.divide(a, b)}")
