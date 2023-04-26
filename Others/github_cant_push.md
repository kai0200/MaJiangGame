# github 无法提交

sslkey配置没有问题后，配置代理
```
cat ~/.ssh/config

HostKeyAlgorithms         +ssh-rsa
PubkeyAcceptedKeyTypes    +ssh-rsa
Host github.com
        Hostname ssh.github.com
        Port 443
        User git
        ProxyCommand nc -v -x 10.2.131.214:7890 %h %p
```
