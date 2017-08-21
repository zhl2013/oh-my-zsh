#cpv() {
#    rsync -pogbr -hhh --backup-dir=/tmp/rsync -e /dev/null --progress "$@"
#}
#compdef _files cpv
#
#
mytest(){
    echo "`date` $@"
}

cc=""
function listMytestComplections {
   #echo "$cc "
   #if [ -n $cc ];then
   #     cc="`date` 123"
   #     echo "`date`"
   #fi
   reply=(
        abc abc:zhl abc
        test test:zhl testCompectrl
    );
}

#compctl -K listMytestComplections mytest
compctl -K listMytestComplections mytest
