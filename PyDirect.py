import socket
import select
import sys

BUFLEN = 4096 * 4
Response =b'HTTP/1.1 200 Switching Protocols\r\nContent-Lenght: 999999999\r\n\r\n'  
Host_port_D =('127.0.0.1',8888)
class DirectProxy():
	def __init__(self,port):
		self.host = '0.0.0.0'
		self.port = port
	def connect(self):
		self.soc =socket.socket(socket.AF_INET)
		self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.soc.bind((self.host,int(self.port)))
		self.soc.listen(0)
		while True:
			self.c,self.addr = self.soc.accept()
			buffered_data = self.c.recv(BUFLEN)
			self.client_connect()
	def client_connect(self):
		self.client = socket.socket()
		self.client.connect(Host_port_D)
		self.client.send(Response)
		self.ConnHandler()
	def ConnHandler(self):
		connected = True
		while connected == True:
			r, w, x = select.select([self.soc,self.client], [], [self.soc,self.client],3)
			
			if x: connected = False; break
			for i in r:
				try:
					data = i.recv(BUFLEN)
					if not data: connected = False; break
					if i is self.client:
						client.send(data)
					else:
						sockt.send(data)
				
				except Exception as e:
							logs(e)
							break
							self.soc.close();self.client.close()
		
def main():
		try:
			Binding_port = sys.argv[1]
		except:
			Binding_port = 80
		Start = DirectProxy(Binding_port)
		Start.connect()
	
if __name__=='__main__':
		main()
		
		
		