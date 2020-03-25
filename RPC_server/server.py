from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
 
import datetime


class Requesthandler(SimpleXMLRPCRequestHandler):

    def __init__(self,req,addr,server):
        self.client_ip,self.client_port = addr
        print(self.client_ip)
        SimpleXMLRPCRequestHandler.__init__(self,req,addr,server)
    
    server = SimpleXMLRPCServer(('localhost',8080))


    


    class Person :
            

        

        
        def hello (self,name,lastname):
            return {
            "name" : name,
            "lastname" : lastname,
            "date" : datetime.datetime.now(),
            
        }
   
    server.register_instance(Person())
    print('server is running on port 8080')
    server.serve_forever()



  




