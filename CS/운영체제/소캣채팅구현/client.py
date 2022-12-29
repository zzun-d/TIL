import socket
import threading

def Send(client_sock):
    while True:
        send_data = bytes(input().encode()) # 사용자 입력
        client_sock.send(send_data)  # Client -> Server 데이터 송신

def Recv(client_sock):
    while True:
        recv_data = client_sock.recv(1024).decode()  # Server -> Client 데이터 수신
        print(recv_data)

#TCP Client
if __name__ == '__main__':
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