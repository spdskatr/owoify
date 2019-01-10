'''
HAHALOL cipher

https://gist.github.com/spdskatr/70d138e65d5e03bba5b4712c63977c1b
'''

import math

alphabet = "abcdefghijklmnopqrstuvwxyz"
# These are the last 127 prime numbers less than 10^5

pl = [98563, 98573, 98597, 98621, 98627, 98639, 98641, 98663, 98669, 98689, 98711, 98713, 98717, 98729, 98731, 98737, 98773, 98779, 98801, 98807, 98809, 98837, 98849, 98867, 98869, 98873, 98887, 98893, 98897, 98899, 98909, 98911, 98927, 98929, 98939, 98947, 98953, 98963, 98981, 98993, 98999, 99013, 99017, 99023, 99041, 99053, 99079, 99083, 99089, 99103, 99109, 99119, 99131, 99133, 99137, 99139, 99149, 99173, 99181, 99191, 99223, 99233, 99241, 99251, 99257, 99259, 99277, 99289, 99317, 99347, 99349, 99367, 99371, 99377, 99391, 99397, 99401, 99409, 99431, 99439, 99469, 99487, 99497, 99523, 99527, 99529, 99551, 99559, 99563, 99571, 99577, 99581, 99607, 99611, 99623, 99643, 99661, 99667, 99679, 99689, 99707, 99709, 99713, 99719, 99721, 99733, 99761, 99767, 99787, 99793, 99809, 99817, 99823, 99829, 99833, 99839, 99859, 99871, 99877, 99881, 99901, 99907, 99923, 99929, 99961, 99971, 99989, 99991]

d = {}
bd = {}

# Build lookup table

for i in range(len(pl)):
    d[chr(i)] = pl[i]
    bd[pl[i]] = chr(i)

# Prime factorisation

def factor(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return (i, a // i)
    return (a, 1)

def encrypt(x):
    res = []
    for i in range(int(math.ceil(len(x)/2))):
        # For each pair in string
        a = x[2*i:2*i+2]
        r = 1
        # multiply together
        for c in a:
            r *= d[c]
        # multiply by 69 if first letter is greater than second (info is lost in multiplication)
        if len(a) == 2 and (ord(a[0]) > ord(a[1])):
            r *= 69
        # Convert to binary
        s = "{0:b}".format(r).replace("0", "HA ").replace("1", "LOL ")
        res.append(s) 
    return "HAHALOL ".join(res)

def decrypt(x):
    chars = x.split(" HAHALOL ")
    res = ""
    # Parse everything back
    for seq in chars:
        b = seq.replace("HA", "0").replace("LOL", "1").replace(" ", "")
        if int(b, base=2) % 69 == 0:
            x, y = factor(int(b, base=2) // 69)
            rx = bd[x]
            ry = bd[y]
            res += "".join(sorted(rx + ry, reverse=True))
        else:
            x, y = factor(int(b, base=2))
            if y == 1:
                res += bd[x]
            else:
                rx = bd[x]
                ry = bd[y]
                res += "".join(sorted(rx + ry))
    return res

if __name__ == "__main__":
    print("Output: " + encrypt(input("Text: "))) 
