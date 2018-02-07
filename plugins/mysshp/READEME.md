## ssh auto tip

基于[os-my-zsh](https://github.com/robbyrussell/oh-my-zsh) 和 expect 实现 ssh 提示登陆

mac 远程工具有 SecureCRT  与 zoc7 ，收费且经常崩溃，借住os-my-zsh 实现ssh 提示远程登录，记录密码

通过oh-my-zsh plugh mysshp 桥接mysshp.py 实现读取配置文件 ~/.ssh/sshp.csv 来提示，读取密码

登录通过 mysshp.py 调用 exp

已实现:

1. 实现ssh 远程登录，可以通过密码和证书登陆
2. 实现提示关键词做登陆

待实现：

1. 提示先groupName,keyword,user，依次提示不是全提示出来
2. 登陆信息维护，crud
3. csv 文件加密


sshp.csv 放到~/.ssh/ 目录下

| groupName | host | port |  user  | pwd  | keyfile  |compectrl | date |
| :---------: |:----:| :----:|  :----:| :----:| :----:| :----:| :----:|
| tomcat-s1 | 192.168.0.221 | 22 | tomcatwallet | | cc/f | sa sf| 2017-08-17 17:58:37 |
| tomcat-s2 | 192.168.0.222 | 22 | tomcat | pwd |  | weixin zhangxin zixun |  2017-08-17 17:58:37 |


