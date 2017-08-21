
mysshp(){
    #echo "mysshp $@"
    python /Users/zhanghl/.oh-my-zsh/plugins/mysshp/mysshp.py login $1
}


cc=""
function listMysshpComplections {
   if [ -n $cc ];then
       comstr=`python /Users/zhanghl/.oh-my-zsh/plugins/mysshp/mysshp.py getCompectrl`
 #      echo `date `$comstr
       # comstr="zhl=123 zhl:abc"
        cc=$comstr
   fi




   #reply=($cc)
   #echo (${(ps. .)${cc}})[1]
   reply=(
   ${(ps. .)${cc}}
   #cyj:zhl cyj:gyq
   )
}

compctl -K listMysshpComplections mysshp
