import socket
from pickle import dump, load, loads, dumps
from _thread import *
from os import listdir
from Server import Menus

server = "10.0.0.183"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

menu = Menus.Login


def save(player):
    string = player['username'] + '.u'
    with open(string, 'bw') as f:
        dump(player, f)


def log_in(user):
    for file in listdir('.'):
        if file == user['username'] + '.u':
            with open(file, 'br') as f:
                data = load(f)
                if data['password'] == user['password']:
                    return ['logged in', data]
                else:
                    return ['wrong password', None]
    return ['no user found', None]


def threaded_client(conn, string):
    while True:
        try:
            user = loads(conn.recv(2048))

            if not user:
                print("Disconnected")
                break

            print("Received: ", user)

        except:
            break

        if user:
            if len(user) == 1:
                if user['message'] == 'menu':
                    conn.sendall(dumps(menu))

            if len(user) == 2:
                flag = log_in(user)

                reply = {'message': flag[0], 'player': flag[1]}
                conn.sendall(dumps(reply))

                if flag[0] == 'logged in':
                    print('logged in')

            elif len(user) == 4:
                print('created ', user['username'])
                save(user)
                reply = {'message': 'created', 'player:': None}
                conn.sendall(dumps(reply))

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, ''))
