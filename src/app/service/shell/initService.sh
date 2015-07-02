#!/bin/bash

#服务器执行的前提
1、支持easy_install

serviceIp=$1
serviceUser=$2
servicePasswd=$3

echo "初始化service机器"
/usr/bin/expect <<-EOF

spawn ssh $serviceUser@$serviceIp
expect {
  "yes/no" { send "yes\r"; exp_continue}
  "password:" { send "$servicePasswd\r" }
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
expect "*"
send "echo '开始安装pymongo'\r"
expect "*"
send "easy_install pymongo\r"
expect "*"
send "echo 'pymongo安装完毕'\r"
interact
expect eof
EOF
echo "初始化service机器完毕"