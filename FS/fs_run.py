from ast import arg
from flask import Flask,request
import json
from socket import *
import numbers

app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def getFibonacci(n):
    print("in Fib core method")
    if n <= 2:
        return 1
    else:
        return getFibonacci(n - 1) + getFibonacci(n - 2)

def getFibonacciNumber():
    print("in getFibonacciNumber validation")
    userInput= request.args.get("number")
    if userInput is not None and userInput.isnumeric():
        number = int(userInput)
        if number>=0:
            return 'The Fibboncacci  sequwncw is  {1}, 200 '.format(number, getFibonacci(number))
    else:
        '400'


@app.route('/register', methods=['PUT'])
def register():
    print("Entry point : registering the requesyt")
    reqBody = request.get_json() 
    print(reqBody)
    hostname,ip,as_ip,as_port = reqBody['hostname'],reqBody['ip'],reqBody['as_ip'],reqBody['as_port']
    print("FS Server  Host "+reqBody['hostname'])
    print("FS IP "+reqBody['ip'])
    print("Auth Sever IP "+reqBody['as_ip'])
    print("Auth Seve rport "+reqBody['as_port'])
    UDP_port=53533
    serverName,UDP_port = as_ip,53533
    regSocket = socket(AF_INET, SOCK_DGRAM) 
    dnsRequest = {
        'TYPE': 'A','NAME': hostname,'VALUE': ip,'TTL': 10 
    }
    message = json.dumps(dnsRequest)
    print(message)
    #fsSocket.connect((as_ip,int(as_port)))
    print("before connceiotn")
    regSocket.sendto(message.encode(),(as_ip,UDP_port))
    print("Connections estblaished ! ")
   
    message, serverAddress = regSocket.recvfrom(2048)
    print(serverAddress)
    print("CScoket is baout to close ! ")
    regSocket.close()
    return message.decode()


app.run(host='0.0.0.0',
        port=9090,
        debug=True)
