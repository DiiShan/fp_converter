# =====================================
#   Copyright (c) 2022 - z
#   File Name : fp_converter.py
#   Created Date : 2022/4/28
#   Created By   : z
# =====================================

__author__ = "z"
__copyright__ = "Copyright 2022, z"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "z"
__email__ = "TBD"
__status__ = "Production"
__credits__ = ["z", "zz","zzz"]

import sys
import string
import struct

def hello():
    print("hello world")

    print("//==================================================")
    print("//   Float Point Display Tools")
    print("//==================================================")

# try:
#     opts,args = getopt.getopt(sys.argv[1:],"-s: -m:",['size=','mode='])
# except getopt.GetoptError:
#     print("Error!")

# for opt,arg in opts:
#     if opt in ('-s','--size'):
#         print("size : ",arg)
#     elif opt in ('-m','--mode'):
#         print('mode :',arg)

# HEX32 = 0;
# HEX64 = 0;
# FP32 = nan;
# FP64 = nan;

# print(FP32,FP64,HEX32,HEX64)

# HEX32 = hex( struct.unpack('!I', struct.pack('!f',nan))[0])
# HEX64 = hex( struct.unpack('!Q', struct.pack('!d',nan))[0])

# print(HEX32)
# print(HEX64)

a = 'a18c0000'
print(a,type(a))
FP32 = struct.unpack('!f', bytes.fromhex(a))[0]
# FP64 = struct.unpack('!d', bytes.fromhex('7ff8000000000000'))[0]

print(FP32,type(FP32))
# print(FP64)

def sfp_dec2hex():
    print("[sfp_dec2hex] tbd")
