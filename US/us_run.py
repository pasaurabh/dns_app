from flask import Flask,request
from urllib.request import urlopen
import json
from socket import *


app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname=request.args.get('hostname') #fibo.com 
    fs_port=request.args.get('fs_port') # 80
    number=request.args.get('number') # x
    as_ip=request.args.get('as_ip') # Auth server
    as_port=request.args.get('as_port')
    print("Entered PAram "+ hostname+"2"+fs_port+"3"+number+"4"+as_port+"5"+as_ip)

    if not as_port or not as_ip or not number or not fs_port or not hostname:
        return '400'

    UDP_port=53533
    ip_request = {'TYPE': 'A','NAME': hostname}
    serverName,serverPort = as_ip, UDP_port
    message = json.dumps(ip_request)
    print(message)
    usSocket = socket(AF_INET, SOCK_DGRAM)
    usSocket.sendto(message.encode(), (serverName, serverPort))
    response, serverAddress = usSocket.recvfrom(2048)
    contentBody= json.loads(response.decode())
    ip_address=contentBody['VALUE']
    usSocket.close()
    webLink='http://{}:{}/fibonacci?number={}'.format(ip_address,fs_port,number)
    acessPoint = urlopen(webLink)
    return acessPoint.read()

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
