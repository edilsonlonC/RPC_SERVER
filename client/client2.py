import xmlrpc.client 
from xmlrpc.client import Binary
import sys

argv_list = sys.argv[1::] # terminal arguments
argv_list = [int(l) for l in argv_list]

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

lista = open("lista.bin", "wb+")
list_sender = argv_list
sender_b = bytearray(list_sender)
lista.write(sender_b)
lista.close()
with open ("lista.bin","rb") as handle : 
  
  lista = proxy.reverse_list(handle.read()).data
  print (list(lista))
  
# with open("lista2.bin", "wb+") as handle:
#   handle.write(proxy.reverse_list().data)
#   handle.close()
#   hanle2 = open('lista2.bin', "rb+")
#   list_response = list(hanle2.read())
#   print(list_response)

#   print ("el rango de los numeros debe ser de 0 a 256 =)")
  
  

  

