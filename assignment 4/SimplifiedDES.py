# Vivek Patel
import binascii
from textwrap import wrap

def encrypt(plaintext, key):
    plaintext = bin(plaintext)[2:]
    while (len(plaintext) < 12): plaintext = "0" + plaintext
    key = bin(key)[2:]
    while (len(key) < 9): key = "0" + key
    if len(plaintext) not in range(0, 4096) or len(key) not in range(0, 512):
        print("Plaintext or key is too long.")
        return
    s1 =    [["101", "010", "001", "110", "011", "100", "111", "000"], ["001", "100", "110", "010", "000", "111", "101", "011"]]
    s2 =    [["100", "000", "110", "101", "111", "001", "011", "010"], ["101", "011", "000", "111", "110", "010", "001", "100"]]
    b = wrap(plaintext, 12)
    b[-1] = b[-1].ljust(12, "0")[:12]
    k = key * 2
    subkeys = [k[0:8], k[1:9], k[2:10], k[3:11]]
    c = ""
    for i in range(0,len(b)):
        b = b[i]
        l, r = b[:len(b)//2], b[len(b)//2:]
        for j in range (0, 4):
            lp = l
            k = subkeys[j]
            l = r
            r = expand(r)
            r = xor(r, k, 8)
            r1, r2 = r[:len(r)//2], r[len(r)//2:]
            s1r = int(r1[0])
            s1c = int(r1[1:], 2)
            s2r = int(r2[0])
            s2c = int(r2[1:], 2)
            s1out = s1[s1r][s1c]
            s2out = s2[s2r][s2c]
            f = s1out + s2out
            r = xor(lp, f, 6)
        c += l + r
    if len(c) == 0: return 0
    else: c = int(c, 2)
    return c
        
def expand(s):
    ex = s[0] + s[1] + s[3] + s[2] + s[3] + s[2] + s[4] + s[5]
    return ex

def xor(s1, s2, n):
    n1 = int(s1, 2)
    n2 = int(s2, 2)
    x = bin(n1^n2)[2:]
    z = n-len(x)
    zs = "0" * z
    x = zs + x
    return x

plaintext = input("Enter plaintext integer: ")
key = input("Enter key integer: ")
if (plaintext.isdigit() and key.isdigit()): 
    ciphertext = encrypt(int(plaintext), int(key))
    print("Ciphertext: " + str(ciphertext))
else: 
    print("Value is not an integer")
