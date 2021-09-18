from sys import argv, stderr
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, AI_PASSIVE, AI_ADDRCONFIG
from socket import IPPROTO_TCP, SOL_SOCKET, SO_REUSEADDR
from os import abort
import datetime
import _thread
import config

# Endereco Host
def getEnderecoHost(porta):
    try:
        enderecoHost = getaddrinfo(None, porta, family=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP, flags=AI_ADDRCONFIG | AI_PASSIVE)
    except:
        print("Nao obtive informacoes sobre o servidor (???)", file=stderr)
        abort()
    return enderecoHost

# Modo
def setModo(fd):
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    return

# Bind do socket
def bindaSocket(fd, porta):
    try:
        fd.bind(('', porta))
    except:
        print("Erro ao dar bind no socket do servidor ", porta, file=stderr)
        abort()
    return

# colocar o server para escutar
def escuta(fd):
    try:
        fd.listen(2)
    except:
        print("Erro ao comecar a escutar a porta", file=stderr)
        abort()
    print("Iniciando o servico", file=stderr)
    return

# Função utilitária para abrir um arquivo e retornar seu conteúdo (body)
def openfile(path):
    f = open(path, "rb")
    body = f.read()
    f.close()
    return body 
    

def processaRequests(conn, client):
    # pega o request
    request = conn.recv(1024).decode("utf-8")
    
    # prepara o body da mensagem
    body = ""
    
    # prepara o content type
    contenttype = ""

    # enum para determinar o dia da semana, para data formatada
    weekdays = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")

    # caso não haja request, encerrar a sessão
    if not request:
        conn.close()
        print("Conexão terminada com ", client, file=stderr)
        return

    # cortar o comando do request e pegar o primeiro elemento
    request = request.splitlines()[0]

    # separar o comando cortado anteriormente 
    requestMethod, filePath, protocol = request.split(" ")
    
    # request do cliente é impresso na tela
    print("Method: " + requestMethod + "\tRequested File: " + filePath + "\tHTTPS Protocol: " + protocol, file=stderr)
    
    # se for qualquer método diferente de GET, error 501
    if requestMethod != "GET":
        status  = "501"
        message = "Not Implemented"
    else:
        try:
            # página index default
            if filePath == "/":
                contenttype = "text/html"
                body = openfile(config.defaultindex)
            else:
                # se o request pedir um html
                if ".html" in filePath:
                    contenttype = "text/html"
                    body = openfile(config.dirname + config.htmldir + filePath)
               
                # se o request pedir um JavaScript
                elif ".js" in filePath:
                    contenttype = "text/javascript"
                    body = openfile(config.dirname + config.jsdir + filePath)

                # se o request pedir um png ou jpg
                elif ".png" in filePath or ".jpg" in filePath:
                    if ".png" in filePath:
                        contenttype = "image/png"
                    else:
                        contenttype = "image/jpg"
                    body = openfile(config.dirname + config.imagesdir + filePath)

                # se o request pedir um gif
                elif ".gif" in filePath:
                    contenttype = "image/gif"
                    body = openfile(config.dirname + config.gifsdir + filePath)

                else:
                # qualquer outro arquivo força um Erro "File Not Found"
                    raise FileNotFoundError
            
            # Mensagem OK e status 200        
            status = "200"
            message = "OK"
    
        except FileNotFoundError:
            # Erro 404
            body = openfile(config.defaulterror)
            status = "404"
            message = "File Not Found"

    # preparar a resposta ao request do client
    header = "Content-Length: " + str(len(body))

    conn.send(("HTTP/1.1 " + status + " " + message).encode("utf-8"))
    conn.send(header.encode("utf-8"))
    conn.send("\n\n".encode("utf-8"))
    
    # envio da resposta ao request
    conn.send(body)
    
    # Mensagem formatada na console
    print(message + " " + status, file=stderr)
    print("Content-Type: " + contenttype, file=stderr)
    print(header, file=stderr)
    date = datetime.datetime.now().astimezone(None).strftime("%d %b %Y %H:%M:%S GMT%z")
    print(weekdays[datetime.date.weekday(datetime.date.today())] + ", " + date + "\n\n", file=stderr)
    
    conn.close()

    print("Conexão terminada com ", client, file=stderr)

    return

def criaSocket(enderecoServidor):
    fd = socket(enderecoServidor[0][0], enderecoServidor[0][1])
    if not fd:
        print("Nao consegui criar o socket", file=stderr)
        abort()
    return fd

def main():
    if len(argv) == 2:
        porta = int(argv[1])
    else:
        porta = config.defaultport
  
    enderecoHost = getEnderecoHost(porta)
    tcpSocket = criaSocket(enderecoHost)
    setModo(tcpSocket)
    bindaSocket(tcpSocket, porta)
    escuta(tcpSocket)
    print("Servidor pronto em ", enderecoHost)

    while True:
        (conn, cliente) = tcpSocket.accept()
        _thread.start_new_thread(processaRequests, (conn, cliente))
    
    tcpSocket.close()
    return

if __name__ == '__main__':
    main()
