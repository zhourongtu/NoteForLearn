
import socket

# 基于文件的通信
# AF_UNIX

# 基于网络通信
# AF_INET


# 1. 实例化对象
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 流式协议 TCP
# sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# 2. 绑定地址
# 本机IP、127.0.0.1、0.0.0.0
# 1024前

while True:
    # 5. 数据传输
    data = input('请输入：')
    if not data:
        continue
    sk.sendto(data.encode('utf-8'), ('127.0.0.1', 45126))
    data = sk.recv(1024) # bytes，why 1024？
    # conn.send()
    print(data.decode('utf-8'))

# 6. 结束服务（操作系统提供的，所以需要关掉）
sk.close()

# sk.close() # 关服务端，运维
