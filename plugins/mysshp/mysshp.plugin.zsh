__MYSSHP_PY_DIR="${ZSH}/plugins/mysshp"

local gitstatus="$__MYSSHP_PY_DIR/mysshp.py"
mysshp(){
    python ${gitstatus} login $1
}



function listMysshpComplections { 
  comstr=`python ${gitstatus} getCompectrl`
  #tips reply=(a abc test)
   reply=(
   ${(ps. .)${comstr}}
   )
}

compctl -K listMysshpComplections mysshp