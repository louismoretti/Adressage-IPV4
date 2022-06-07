ipDPx1 = '192.168.120.101'
ipDPx2 = '192.168.121.200'
ipDPy = '192.168.120.102'
msqDP = '255.255.255.0'


"""
décimal 8bits => strings 8bits : dec2bin8 ()
décimal pointé => string 32bits : DP2b32 ()
string 32bits => strings 32bits pointé : b32toBP ()
string 32bits => décimal pointé : b32toDP ()
extrait l'adr réseau string 32bits : adrR(ipB32, masqueB32)
"""
def dec2bin8(dec):
    b = bin(dec)[2:]
    return '0'*(8-len(b))+b

def DP2b32(dp):
    l = dp.split('.')
    t = []
    for i in l:
        t.append(str(dec2bin8(int(i))))
    return "".join(t)

def b32toBP(b32):
    return f"{b32[:8]}.{b32[8:16]}.{b32[16:24]}.{b32[24:]}"

def b32toDP(b32):
    return f"{int(b32[:8], 2)}.{int(b32[8:16], 2)}.{int(b32[16:24], 2)}.{int(b32[24:], 2)}"

def adrR(ipB32, masqueB32):
    t = ""
    for i in range(len(ipB32)):
        if ipB32[i] == masqueB32[i]:
            t += f"{ipB32[i]}"
        else: t += "0"
    return t




srX1 = adrR(DP2b32(ipDPx1), DP2b32(msqDP))
adrRipDP1 = b32toDP(srX1)
SadrRip1 = b32toBP(srX1)
srX2 = adrR(DP2b32(ipDPx2), DP2b32(msqDP))
adrRipDP1 = b32toDP(srX2)
SadrRip1 = b32toBP(srX2)
srY = adrR(DP2b32(ipDPy), DP2b32(msqDP))
adrRipDP2 = b32toDP(srY)
SadrRip2 = b32toBP(srY)

print("masque =>", b32toBP(DP2b32(msqDP)), msqDP)
print()
print("IPy =>", b32toBP(DP2b32(ipDPy)), ipDPy)
print("@SRy =>", b32toBP(srY) , b32toDP(srY))
print()
print("IPx1 =>", b32toBP(DP2b32(ipDPx1)), ipDPx1)
print("@SRx1 =>", b32toBP(srX1) , b32toDP(srX1))
if srX1==srY : print( 'Adresses IP compatibles')
else : print( 'Adresses IP incompatibles')
print()
print("IPx2 =>", b32toBP(DP2b32(ipDPx2)), ipDPx1)
print("@SRx2 =>", b32toBP(srX2) , b32toDP(srX2))
if srX2==srY : print( 'Adresses IP compatibles')
else : print( 'Adresses IP incompatibles')