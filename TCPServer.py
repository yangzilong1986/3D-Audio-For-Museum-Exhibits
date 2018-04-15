import hrtf
import socket
import time

HOST = '127.0.0.1'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Server listening on port 50007...")
conn, addr = s.accept()
print('New connection:', addr)

aIndex = 0
eIndex = 8
soundToPlay = hrtf.hrtf('audio/1-School-Lunch.wav', aIndex, eIndex)
byte_string = soundToPlay.tobytes()
print('Generated byte string of .wav file...')

data = conn.recv(1024)
print('Received data from ' + HOST + ": " + data.decode(encoding='UTF-8'))
conn.send(byte_string)
print("Sent byte string to client...")
# byte_string = byte_string[65536:]
time.sleep(200)

print('Closing stream...')
s.close()
