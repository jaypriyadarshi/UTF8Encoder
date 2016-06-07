import sys
import struct
from bitstring import BitArray

#fill one octent
def fill8(b,code):
    _bnry = bin(int(code,16))
    _bnry = list(_bnry)
    _bnry.reverse()
    i=7
    k=0
    flag=0
    while i>0:
        if _bnry[k] == 'b' or flag:
            b[i] = int('0',2)
            flag=1
        if not flag:
            b[i] = int(_bnry[k],2)
            k+=1
        i-=1
    f2.write(chr(int(str(b),16)))

#fill 2 octents
def fill16(b,c,code):
    _bnry = bin(int(code,16))
    _bnry = list(_bnry)
    _bnry.reverse()
    i=7
    k=0
    flag=0
    while i>1:
        if _bnry[k] == 'b' or flag:
            c[i] = int('0',2)
            flag=1
        if not flag:
            c[i] = int(_bnry[k],2)
            k+=1
        i-=1
    i=7
    while i>2:
        if _bnry[k] == 'b' or flag:
            b[i] = int('0',2)
            flag=1
        if not flag:
            b[i] = int(_bnry[k],2)
            k+=1
        i-=1

    f2.write(chr(int(str(b),16)))
    f2.write(chr(int(str(c),16)))
    
#fill all three octents
def fill24(b,c,d,code):
    _bnry = bin(int(code,16))
    _bnry = list(_bnry)
    _bnry.reverse()
    i=7
    k=0
    flag=0
    while i>1:
        if _bnry[k] == 'b' or flag:
            d[i] = int('0',2)
            flag=1
        if not flag:
            d[i] = int(_bnry[k],2)
            k+=1
        i-=1
    i=7
    while i>1:
        if _bnry[k] == 'b' or flag:
            c[i] = int('0',2)
            flag=1
        if not flag:
            c[i] = int(_bnry[k],2)
            k+=1
        i-=1

    i=7
    while i>3:
        if _bnry[k] == 'b' or flag:
            b[i] = int('0',2)
            flag=1
        if not flag:
            b[i] = int(_bnry[k],2)
            k+=1
        i-=1
    
    f2.write(chr(int(str(b),16)))
    f2.write(chr(int(str(c),16)))
    f2.write(chr(int(str(d),16)))


_filename = sys.argv[1]

f2 = open('utf8encoder_out.txt','w')
with open(_filename,'rb')as f:
        _byte = f.read(2)
        while _byte != "":
                #print _byte
                a = struct.unpack('>2c',_byte)
                part2 = hex(ord(a[1]))[2:]
                if len(part2)==1:
                    part2='0'+part2
                utf16 = hex(ord(a[0]))+ part2
                #print utf16
                #checking which group it belongs to
                if int(utf16,16) >= int('0x0000',16) and int(utf16,16) <= int('0x007F',16):
                    b = BitArray(8)
                    b[0] = 0
                    fill8(b,utf16)

                elif int(utf16,16) >= int('0x0080',16) and int(utf16,16) <= int('0x07FF',16):
                    b = BitArray(8)
                    c = BitArray(8)
                    b[0] = b[1] = c[0] = 1
                    b[2] = c[1] = 0
                    fill16(b,c,utf16)

                elif int(utf16,16) >= int('0x0800',16) and int(utf16,16) <= int('0xFFFF',16):
                    b = BitArray(8)
                    c = BitArray(8)
                    d = BitArray(8)
                    b[0] = b[1] = b[2] = c[0] = d[0] = 1
                    b[3] = c[1] = d[1] = 0
                    fill24(b,c,d,utf16)
                _byte = f.read(2)

f2.close()
f.close()
