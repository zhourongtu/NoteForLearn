
import socket

# 基于文件的通信
# AF_UNIX

# 基于网络通信
# AF_INET


# 1. 实例化对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 流式协议 TCP
# sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# 2. 绑定地址
# 本机IP、127.0.0.1、0.0.0.0
# 1024前
# 如果不想每次改端口--> setsocketopt
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 重用绑定的IP和端口
sk.bind(('127.0.0.1', 45126))
# 3. 监听连接请求
sk.listen(5) # 半连接池大小（只不过代表能连接上，不代表能享受服务）
print('服务端启动成功，等待客户端连接')

# 4. 取出连接请求，开始服务
while True:
    conn, addr = sk.accept()
    # 5. 数据传输
    while True:
        # 空数据？
        data = conn.recv(1024) # bytes，why 1024？
        if not data:
            break
        # conn.send()
        data = data.decode('utf-8')
        print(data)
        conn.send(data.upper().encode('utf-8'))
    # 6. 结束服务（操作系统提供的，所以需要关掉）
    conn.close()

sk.close() # 关服务端，运维

# cd /c/Users/zhour/Desktop/Learn/NoteForLearn/计算机基础知识相关/语言相关/Python/进阶
