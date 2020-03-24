from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import pickle

def reverse_list (arg):
    print (arg.data)
    lista = list(arg.data)
    lista.reverse()
    print(lista)
    with open("response.bin", "wb+") as handle:
        handle.write(bytearray(lista))
        handle.close()
    with open("response.bin","rb") as handle_response:
        list_response = handle_response.read()
        print (list_response)
        print (list(list_response))
        return list_response


    

server = SimpleXMLRPCServer(('localhost',8000))
print ('running')
server.register_function(reverse_list,'reverse_list')

server.serve_forever()