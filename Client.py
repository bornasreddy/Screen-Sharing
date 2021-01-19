from vidstream import ScreenShareClient
import threading



client = ScreenShareClient("192.168.159.1", 8888)         #192.168.159.1 is the IPV4 of Streaming server



t = threading.Thread(target=client.start_stream)
t.start()

while input("") != 'stop':
    continue

client.stop_stream()
