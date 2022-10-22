
**1.连接失败**
> ssh: connect to host github.com port 22: Connection timed out fatal: Could not read from remote repo
- 原因
- 解决方案：用https协议代替git协议
``` bash
git config --global url."https://github.com/".insteadOf git@github.com:
```

> 参考链接 https://stackoverflow.com/questions/15589682/ssh-connect-to-host-github-com-port-22-connection-timed-out