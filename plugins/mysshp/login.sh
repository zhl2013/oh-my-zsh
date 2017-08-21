#!/bin/sh
cd "`dirname $0`"
BASE_HOME=`pwd`

host=$1
port=$2
user=$3
password=$4
id_file=$5

if [ $5 ]; then
    ./auto_login_with_id_file.exp $host $port $user $id_file
elif [ $4 ]; then
	#statements
	./auto_login.exp $host $port $user $password
else
	ssh -p $port $user@$host
fi