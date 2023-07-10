
# hash(哈希)
# md5
# sha1
# sha256
# sha512

# hash值
# 1、输入敏感
# 2、不可逆
# 3、计算极快而长度固定

# 用途：
# 1、密码加密。（通过网络传输时），破解？
# i5四核：每秒200亿次
# 密码库-->哈希值-->密文
# 加盐防碰撞
# 2、文件的完整性校验（python官网，hash校验）

import hashlib
h1 = hashlib.md5()
h1 = hashlib.sha256()
h1.update('abc'.encode('utf-8')) # 二进制格式
h1.hexdigest()

# 使用哈希，进行密码加密，判断。


file_path = 'GC与弱引用.md'

with open(file_path, 'rb') as f:
    m1 = hashlib.md5(f.read())
    print(m1.hexdigest())

# 使用seek的方式，进行分段式校验。
# 获取文件的大小
# size = os.path.getsize(path)

with open(file_path, 'rb') as f:
    f.seek(0, 2)
    size = f.tell() # 当前所在位置--
    m1 = hashlib.md5(f.read())
    print(m1.hexdigest())

    one_tenth = size // 10
    for i in range(10):
        f.seek(i*one_tenth, 0)
        res = f.read(100)
        m1.update(res)
    print(m1.hexdigest())

# 加盐
pwd = 'abcdee'
m2 = hashlib.md5()
m2.update(pwd[:2].encode('utf-8'))
m2.update('ceshi'.encode('utf-8'))
m2.update(pwd[2:4].encode('utf-8'))
m2.update('ceshi2'.encode('utf-8'))
m2.update(pwd[4:].encode('utf-8'))
