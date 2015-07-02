#!/bin/bash

#服务器执行的前提

clinetIp=$1
clinetUser=$2
clinetPasswd=$3
clinetPath=$4
serviceClinetPath=$5

echo "开始拷贝clinet文件到目标机"
/usr/bin/expect <<-EOF

spawn  scp -r $serviceClinetPath $clinetUser@$clinetIp:$clinetPath
expect {
  "yes/no" { send "yes\r"; exp_continue}
  "password:" { send "$clinetPasswd\r";}
}
set time 30
interact
expect eof
EOF
echo "clinet文件拷贝完毕"