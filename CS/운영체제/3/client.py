import socket
import threading

def Send(client_sock):
    global tmp
    while not tmp:
        msg = input()
        if msg == '/exit':
            client_sock.close()
            break
        client_sock.send(msg.encode('utf-8'))  # Client -> Server 데이터 송신
    return

def Recv(client_sock):
    while True:
        try:
            recv_data = client_sock.recv(1024).decode()  # Server -> Client 데이터 수신
            
            if recv_data == 'Full':
                print(recv_data)
                client_sock.close()
                tmp = True
                break
            else:
                if type(recv_data) != str:
                    recv_data = recv_data.decode('utf-8')
                print (recv_data)
        except:
            print('퇴장')
            client_sock.close()
            break
    return
    
#TCP Client
if __name__ == '__main__':
    tmp = False
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP Socket
    Host = 'localhost' #통신할 대상의 IP 주소
    Port = 9000  #통신할 대상의 Port 주소
    client_sock.connect((Host, Port)) #서버로 연결시도
    print('Connecting to ', Host, Port)


    #Client의 메시지를 보낼 쓰레드
    thread1 = threading.Thread(target=Send, args=(client_sock, ))
    thread1.start()

    #Server로 부터 다른 클라이언트의 메시지를 받을 쓰레드
    thread2 = threading.Thread(target=Recv, args=(client_sock, ))
    thread2.start()