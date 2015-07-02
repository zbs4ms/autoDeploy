#!/bin/bash

#服务器执行的前提
1、支持easy_install

clinetIp=$1
clinetUser=$2
clinetPasswd=$3

echo "初始化clinet机器"
/usr/bin/expect <<-EOF

spawn ssh $clinetUser@$clinetIp
expect {
  "yes/no" { send "yes\r"; exp_continue}
  "password:" { send "$clinetPasswd\r" }
}
expect "*"
send "echo '开始安装flask'\r"
expect "*"
send "easy_install flask\r"
expect "*"
send "echo 'flask安装完毕'\r"
expect "*"
send "echo '开始安装supervisor'\r"
expect "*"
send "easy_install supervisor\r"
expect "*"
send "echo 'supervisor安装完毕'\r"
interact
expect eof
EOF
echo "初始化clinet机器完毕"