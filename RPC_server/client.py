import xmlrpc.client

if __name__ == "__main__":

    client = xmlrpc.client.Server('http://localhost:8080')
    name = input('name here \n')
    lastname = input('lastname here \n')
    print (client.hello(name,lastname))
    