#!/bin/bash

clinetIp=$1
clinetUser=$2
clinetPasswd=$3
clinetPath=$4

echo '开始运行$clinetIP上的文件'
/usr/bin/expect <<-EOF

spawn  ssh $clinetUser@$clinetIp
expect {
  "yes/no" { send "yes\r"; exp_continue}
  "password:" { send "$clinetPasswd\r";}
}
expect "*"
send "cd $clinetPath/clinet\r"
expect "*"
send "nohup python start.py >> start.log&\r"
interact
expect eof
EOF
echo "运行完毕"
