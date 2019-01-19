#!/usr/bin/python
# -*- coding: UTF-8 -*-

#谷歌身份验证器(google authenticator)的验证码

import hmac, base64, struct, hashlib, time,sys

def calGoogleCode(secretKey):
    input = int(time.time())//30
    lens = len(secretKey)
    lenx = 8 - (lens % 4 if lens % 4 else 4)
    secretKey += lenx * '='
    #print secretKey, ' ----- ' ,lenx  , lens ,'|'
    key = base64.b32decode(secretKey)
    msg = struct.pack(">Q", input)
    googleCode = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(googleCode[19]) & 15
    googleCode = str((struct.unpack(">I", googleCode[o:o+4])[0] & 0x7fffffff) % 1000000)
    if len(googleCode) == 5:
        googleCode = '0' + googleCode
    return googleCode

if __name__ == '__main__':
    if len(sys.argv)<2:
        print ("must input secretKey")
        exit(1)
    print (calGoogleCode(sys.argv[1]))
