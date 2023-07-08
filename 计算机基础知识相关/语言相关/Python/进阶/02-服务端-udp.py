
import socket

# 基于文件的通信
# AF_UNIX

# 基于网络通信
# AF_INET


# 1. 实例化对象
# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 流式协议 TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# 2. 绑定地址
# 本机IP、127.0.0.1、0.0.0.0
# 1024前
# 如果不想每次改端口--> setsocketopt
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 重用绑定的IP和端口
sk.bind(('127.0.0.1', 45126))

print('服务端启动成功，等待客户端连接')

# 4. 取出连接请求，开始服务
while True:
    while True:
        # 空数据？
        data, addr = sk.recvfrom(1024) # bytes，why 1024？
        if not data:
            break
        # conn.send()
        data = data.decode('utf-8')
        print(data)
        sk.sendto(data.encode('utf-8', ), addr)
        # conn.send(data.upper().encode('utf-8'))
sk.close() # 关服务端，运维

# cd /c/Users/zhour/Desktop/Learn/NoteForLearn/计算机基础知识相关/语言相关/Python/进阶

# udp不需要握手连接，碰一下。

