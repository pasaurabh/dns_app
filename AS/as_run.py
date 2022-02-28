from socket import *
import json

udpPort = 53533
asSocket = socket(AF_INET, SOCK_DGRAM)
asSocket.bind(('', udpPort))
while True:
    message, userAddress = asSocket.recvfrom(2048)
    rec = json.loads(message.decode())
    print("Recieved Message"+rec)
    if len(rec) == 4:
        with open('dns.log', 'w') as outfile:
            json.dump(rec, outfile)
            message = '201'
    elif len(rec) == 2: 
        with open("dns.log", 'r', encoding='utf-8') as outfile:
            for line in outfile.readlines():
                data = json.loads(line)
                if rec['TYPE'] == data['TYPE'] and rec['NAME'] == data['NAME']:
                    message = json.dumps(data)
                else:
                    message = 'error'
    else:
        print("In Error Block !")
        message ='registration error'

    asSocket.sendto(message.encode(), userAddress)

