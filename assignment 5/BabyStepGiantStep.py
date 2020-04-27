# Vivek Patel
import math
from decimal import Decimal
from textwrap import wrap

def babygiantattack(p,a,b):
    n = int(math.ceil(math.sqrt(p - 1)))
    l = [pow(a, j, p) for j in range(0, n)]
    e = pow(a, n *(p-2),p)
    c = ""
    for k in range(n):
        x = (b * pow(e, k, p)) % p
        if x in l:
            c = (k * n) + l.index(x)
    s = str(c)
    d = { "01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "F", "07": "G", "08": "H", "09": "I", "10": "J", "11": "K", "12": "L", "13": "M", "14": "N", "15": "O", "16": "P", "17": "Q", "18": "R", "19": "S", "20": "T", "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y", "26": "Z"}
    t = wrap(s, 2)
    r = ""
    for ts in t:
        r = r + d[ts]
    print ("Value: " + s + ", Acronym: " + r)
    return
babygiantattack(595117, 1002, 437083)
