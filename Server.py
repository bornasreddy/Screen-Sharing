from vidstream import StreamingServer                               #pip install vidstream
import threading
import socket                                                       #pip install socket


sn = socket.gethostname()                                           #Device name
print(sn)
sip = socket.gethostbyname(sn)                                      #Your IPV4 Address
print(sip)


receiver = StreamingServer(sip, 8888)                                #sip is IPV4, 8888 is port
t = threading.Thread(target=receiver.start_server)
t.start()                                                            #Starts Streaming

while input("") != 'stop':
    continue

receiver.stop_server()
