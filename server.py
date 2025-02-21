from xmlrpc.server import SimpleXMLRPCServer

# define calculate functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# create RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000...")

# register function
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# run the server
server.serve_forever()
