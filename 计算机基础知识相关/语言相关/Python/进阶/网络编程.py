# coding: utf-8


# CS架构与BS架构
"""
CS架构
Client <==========> Server

客户端软件              服务端软件
操作系统                操作系统
计算机硬件 <========>   计算机硬件

BS架构(本质也是CS架构)
Browser <=========> Server
"""

# 网络通信
"""
物理连接介质
    电脑:网卡
    路由器
        交换机(主力交换机)
        -- 光猫 -- 电信设备箱 --- 电信机房 移动机房 联通机房
    手机

多系统、多介质、目标问题(多软件使用网络)
光纤:光信号
网线:电信号
wifi:电磁波信号
"""

# 七层模型
"""
协议:osi七层模型
    物理层:信号转换问题 0101--电信号(光信号)
    数据链路层:
        mac地址查询
    网络层:ip地址
        IANA
        公网ip  全世界唯一
        内网ip  局域网唯一
    传输层:用什么东西发
        TCP     可靠、速度漫 长距离传输
            100M->小包(1500Byte) 00001 ....
        UDP     不可靠,速度快 短距离传输(局域网)
            直播
        端口:一台计算机上的多个程序可以同时使用网络
    会话层:决定什么时候开始发、什么时候断开
    表示层:描述文件类型
    应用层:微信、qq、浏览器
"""

# TCP/IP协议
"""
协议:头部+数据
分包、解包

wireshark工具抓包
使用ping的方式获取ip地址
ip.addr = xx.xx.xx... 进行筛选
"""

# 五层模型
"""
物理层:
    一组数据称之为一个bit流
    01010110
数据链路层:18个字节(
    以太网协议层Ethernet
    一组数据称之为一个“数据帧”,一个数据帧分为两部分(头部+数据)
        头部:发送者、接收者,类型
        数据
    工作方式:广播
        广播域:连接到同一个交换机上的计算机,就是属于同一个广播域
    广播包的特点:会发给广播域内的所有的计算机
    广播风暴
    广播分域
网络层:
    网关:局域网地址、对外地址-->公网
        路由协议
    IP协议
        一组数据称之为一个“数据包”,一个数据包分为两部分
        (发送者IP,接收者IP,类型)+(数据:传输层所有内容)
    IP地址:ipv4
        00000000.00000000.00000000.00000000--> 0.0.0.0
        NAT技术
            公网IP、内网IP
            内网IP段:(其他认为是公网IP)
                10.0.0.0 ~ 10.255.255.255       一千六百多万
                172.16.0.0 ~ 172.31.255.255     104万
                192.168.0.0 ~ 192.168.255.255   65536个 (一般来说买的路由器是这个网段)
            127.0.0.0 ~ 127.255.255.255         保留地址,还有其他

        ipv6(128位)
            每一平方米都可以分到10^26
            fe80::3ced:6594:2b31:1648%4
                %4是在计算机上的编号
    子网掩码
        划分广播域
        198.168.31.97
        255.255.255.0

        --> 198.168.31.0 ~ 198.168.31.255
            第一个IP地址:网络号使用
            第一个可用IP:...
            最后一个可用IP地址:
            最后一个IP地址:广播地址使用
        在同一个网段下:只要物理链路接通,就可以直接通信

        198.168.31.97/24(linux写法)

        子网掩码
            -->网络位
        主机位

        思考题:
            按位与
            192.168.3.125/25
            192.168.3.130/25

        通过计算,如果在同一个网段,则直接使用mac地址通信,否则,则走网关。
    
    ARP协议:地址解析协议 Address Resolution Protocol
        通过IP地址获得物理地址

        工作于链路层与网络层之间:把IP地址解析为mac地址
        通常局域网用的交换机都是二层交换机(数据解析到第二层)
            交换机需要看mac地址,才能知道发给谁
        ARP广播
            谁是IP
            再获取到谁是MAC
        ARP缓存表:(不是永久的,动态的)
            可用注册表修改
        交换机(有一个mac地址表)

        ARP广播:ff:ff:ff:ff:ff:ff --> ARP广播
        虚假mac地址:导致频繁丢包
            mac地址可修改
        ARP广播,谁先回应就是谁的,后续丢掉
        (图灵、苹果公司)
    ARP欺骗:ARP防火墙
        Win10或win11都有,最开始的时候就确定网关是谁
    划分局域网避免广播风暴
    局域网、网关:如果不在局域网,就需要网关
    命令:
        arp -a
        arp -d *
    路由器:lan口(家里设备)、wan口(运营商网络)-->可工作在三层
        可以看作是二层交换机(两个口)-->网关作用
        工作在三层:局域网层、计算机向外通信的中间层、与外部运营商网络通信
        网关一般有两张网卡:分别两个IP地址,可以在两个网络之间做数据转发
    
    NAT:(路由器做的事情)Network Address Translation
        SNAT:源地址转换
            源IP --> 目标IP
            目标IP --> 源目标IP
            ...
            问题:两个计算机发送信息到同一个服务器,只转换IP地址是不够的
            此时,--> 传输层:提供了端口的概念,两个计算机发出的不同消息,转换为不同的端口,可以反向SNAT转换。
        
        DNAT:目标地址转换
            计算机对外提供服务
            我们的公网IP不是固定的,同时运营商也不支持端口外放
            -->**************** 内网穿透 *************
                客户端软件--(保持通信)--服务端软件---公网
                    客户端通过IP和端口映射,可以转发给局域网内提供服务端的主机
                上传速度被阉割过(1/10),所以

    ARP协议(自动解析mac地址)
        (源mac, 目标mac地址) (源ip, 目标ip) 数据            (局域网通信)
            mac地址仅用于在局域网内定位
        (源mac, 网关mac) (源ip, 目标ip) 数据                (跨局域网通信)

传输层
    TCP和UDP协议, 定义了端口的概念, 可以帮助我们定位计算机上的某个应用程序
    端口作用1: NAT转换的作用(对外的时候的转化,网关对外的端口)
    端口作用2: 可以定位到计算机某一个应用程序

    tcp/udp
    tcp头部+数据/ udp头部+端口
    源端口, 目标端口, “数据段”的序号, 根据序列号做回应(TCP)
    
    网速快慢的原因
        最开始快、后来慢
        最开始慢、后来快
        TCP测试
    探测: 三次握手
        握手包标识: SYN
        挥手包标识: FIN
        数据包标识: PSH
        确认包标识: ACK
        重发包标识: RST (网络很差的时候会有很多)
        紧急包: URG

        wireshark会做转换(首次x是随机的, wireshark会转换为0)
            在邮件, 协议首选项, 传输层协议控制中可以勾选相对位置（取消掉）
        客户端->服务端 1. SYN, seq=x, ack(上一次的，第一次建立连接并没有)
        服务端->客户端 
            2. ACK, seq=y, ack=x+1(此时, 服务端向客户端发包, 并未确认是否对方能收到)
            3. SYN, seq=y, ack=x+1
            --> ACK, SYN, seq=y, ack=x+1
        客户端->客户端 4. ACK, seq=x+1, ack=y+1
    四次挥手
        FIN, ACK, seq=x, ack=y
        ACK, seq=y, ack=x+1
            (等待服务端数据发完)
        FIN, ACK, seq=y, ack=x+1
        ACK, seq=x+1, ack=y+1
    
    SYN洪水攻击 
        服务端处于SYN_RCVD状态(半连接)
        高并发
            接收到SYN, 需要发SYN,ACK-->卡在池子里出不去(太多了), 此时状态已经是SYN_RCVD了
        TIME_WAIT状态(1~4分钟)
            有可能服务端没有收到对应的ACK, 可能会重发FIN
        CLOSING
            客户端和服务端都主动乙方, 都调用close, 双方接收到对方的FIN包, 进入CLOSING状态
            收到ACK直接进入close状态

    传输层头部
        0~65535的端口
        自定义协议

应用层
    sockt抽象层(套接字)
        通过网络收数据和发数据的
    dhcp 协议
        插上网线、wifi没有配置ip地址, 自动配置
        插上网线后, 自动广播发送, 路由器收到请求后, 分配
        自己配置? 找到windows的网络和internet后即可配置
    dns
        dns端口: 53
        web端口: 80
        IP通讯录
        变怎么办？
            hosts文件淘汰了
        DNS服务端、DNS客户端

        常用DNS服务器
        阿里
            223.5.5.5
            223.6.6.6
        腾讯
            119.29.29.29
        百度
            180.76.76.76
        谷歌
            8.8.8.8
        114.114.114.114
        115.115.115.115
        360断网急救箱-->改了DNS到114
        
        dns服务器结构
            根域名服务器
                ns记录(权限下放)
            .com 顶级域名服务器
                www.abc.com a 1.1.1.1 --> 直接返回IP地址
                www.abc.com ns 3.3.3.3 --> 权限下放
                    a、ns、cname、mx...
            二级域名（权威域名）
            主机名
            支持IPv6的意义: 美国、伊拉克等例子

        url地址: 唯一资源地址
        https协议的端口是443端口
        在浏览器输入一个地址之后发生的事情

一些命令
ipconfig        
"""
# 在线网络计算器

import socket

# 1.如何在python中编写网络通信？
# 2.编写网络通信中会碰到哪些问题？
# 3.编写UDP和TCP服务器和客户端有哪些区别？
# 4.数据没收完是什么情况？
# 5.什么是粘包问题？两条数据粘在一起。
# 6.为什么没有收完数据？发的太快？缓存问题？

# Socket对象
# 编写一个服务端、一个客户端，两边进行通信，仅需要支持接收数据，打印，将数据变大写回去。
# 将服务端和客户端写为循环。
# 饭馆开业、开始服务、结束服务
# 客户端发数据
# 通信完成
# 局域网通信
# 通信循环
# 客户端异常断开

# mac、linux，收空数据代表有问题

# 远程执行终端的命令，执行结果-->返回
# 有服务器就可以跨局域网执行终端命令了，类似内网穿透的效果


# 问题：1.收的太快。2.缓存太小。3.nagle算法优化（类比快递）。
# 解决方式：先拿到总长度-->固定头部长度。

bytes(str(data_size), 'utf-8').zfill(8)

# struct、int类型to_bytes


# 实例1：远程执行终端命令。
# 实例2：传输文件，增加考虑如文件类型等信息、md5等信息，防止篡改。
# 实例2扩展：上传、下载文件的程序


# 头部长度 + 头部 + 数据
# 所有内容都稍微注意一下粘包。

# 收不干净-->丢掉

# udp长度限制（MTU）1500：网络层IP头部20、UDP报头8个。
# 最稳定：512（短数据）
--> 查询信息，根服务器等问题-->设计缺陷。
# dns














