
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
sk.bind(('127.0.0.1', 45126))
# 3. 监听连接请求
sk.listen(5) # 半连接池大小
print('服务端启动成功，等待客户端连接')

# 4. 取出连接请求，开始服务
conn, addr = sk.accept()

# 5. 数据传输
data = conn.recv(1024) # bytes，why 1024？
# conn.send()
data.decode('utf-8')
print(data)

conn.send(data.upper())
