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
    for i in range(0, len(b)):
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

def decrypt(ciphertext, key):
    ciphertext = bin(ciphertext)[2:]
    while (len(ciphertext) < 12): ciphertext = "0" + ciphertext
    key = bin(key)[2:]
    while (len(key) < 9): key = "0" + key
    if len(ciphertext) not in range(0, 4096) or len(key) not in range(0, 512):
        print("Invalid lengths.")
        return
    s1 =    [["101", "010", "001", "110", "011", "100", "111", "000"], ["001", "100", "110", "010", "000", "111", "101", "011"]]
    s2 =    [["100", "000", "110", "101", "111", "001", "011", "010"], ["101", "011", "000", "111", "110", "010", "001", "100"]]
    b = wrap(ciphertext, 12)
    b[-1] = b[-1].ljust(12, "0")[:12]
    k = key * 2
    subkeys = [k[0:8], k[1:9], k[2:10], k[3:11]]
    p = ""
    for i in range(len(b) - 1, -1, -1):
        b = b[i]
        l, r = b[:len(b)//2], b[len(b)//2:]
        for j in range(3, -1, -1):
            nr = l
            enr = expand(nr)
            v = xor(enr, subkeys[j], 8)
            r1, r2 = v[:len(v)//2], v[len(v)//2:] 
            s1r = int(r1[0])
            s1c = int(r1[1:], 2)
            s2r = int(r2[0])
            s2c = int(r2[1:],2)
            s1out = s1[s1r][s1c]
            s2out = s2[s2r][s2c]
            f = s1out + s2out
            l = xor(r, f, 6)
            r = nr
        p = l + r + p
    if len(p) == 0: return 0
    else: p = int(p, 2)
    return p

def findKeys(plaintext,ciphertext):
    e = []
    d = []
    c = []
    for i in range(0, 512):
        e.append(encrypt(plaintext, i))
        d.append(decrypt(ciphertext, i))
    for i in range(len(e)):
        for j in range(len(d)):
            if e[i] == d[j]:
                c.append((i,j))
    print("Number of candidate keys: " + str(len(c)))
    for s in c:
        print (str(s) + "\n")
    return c

keyCandidates = findKeys(101, 199)

def checkKeys(keys, plaintext, ciphertext):
    k1, k2 = [ i for i, j in keys ], [ j for i, j in keys ]
    c = []
    for i in range(len(k1)):
        ek1 = encrypt(plaintext, k1[i])
        ek2 = encrypt(ek1, k2[i])
        if ek2 == ciphertext:
            c.append((k1[i], k2[i]))
    print("Number of verified candidate keys: " + str(len(c)))
    return c

verifiedKeys = checkKeys(keyCandidates, 110, 2816)
for i in range(len(verifiedKeys)):
    print(str(verifiedKeys[i][0]), str(verifiedKeys[i][1]))
 
















































