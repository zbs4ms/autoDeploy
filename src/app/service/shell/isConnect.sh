#!/bin/bash
PING=`ping -c 3 $1 | grep 'Request timeout' | wc -l`
echo $PING