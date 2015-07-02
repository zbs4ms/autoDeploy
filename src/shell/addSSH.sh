#!/bin/bash

#服务器执行的前提
1、在服务器ssh下生成名为id_rsa 公钥和秘钥

clinetIp=$1
clinetUser=$2
clinetPasswd=$3

echo "安装ssh信任"
/usr/bin/expect <<-EOF

#1.拷贝ssh信任文件到clinet端
spawn scp ~/.ssh/id_rsa.pub $clinetUser@$clinetIp:.ssh/id_service.pub
expect {
  "yes/no" { send "yes\r"; exp_continue}
  "password:" { send "$clinetPasswd\r" }
}
spawn ssh $clinetUser@$clinetIp
expect {
  "yes/no" { send "yes\r"; exp_continue}
  "password:" { send "$clinetPasswd\r" }
}
expect "*"
send touch ~/.ssh/authorized_keys
expect "*"
send cat ~/.ssh/id_service.pub >> ~/.ssh/authorized_keys
interact
expect eof
EOF
echo "ssh信任安装完毕"