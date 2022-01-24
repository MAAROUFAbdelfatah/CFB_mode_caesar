
from operator import index
from numpy import append


def cesier(m, n): # m : message , n : number of permitation
    
    while n > 0:
        m.append(m[0])
        del m[0]
        n -= 1
    return m


def xor(a, b): #xor operation
    a_len = len(a)
    r = []

    for index in range(a_len):
        if a[index] == b[index]:
            r.append(0)
        else:
            r.append(1)
    return r


def encryption_block_CFB_mode(b, iv, nb, k):
    civ = cesier(iv, k) # encryption of the iv
    left_civ = civ[0:nb] #left part of encryption of the iv
    c = xor(left_civ, b) #xor the left part and the block
    iv = iv[nb-1:-1] + c # generate the next iv by adding ciphir to the rest of iv 
    return (iv, c)


def encryption_CFB_mode(m, iv, nb, k): # m: message , iv : initial vector , nb : number of bits of a block , k : encryption key  
    message_len = len(m)
    if message_len % nb != 0:
        index = 0
        while index < nb - (message_len % nb):
            m.append(0)
            index += 1 
    index = 0
    r= []
    while index < len(m):
        iv, c = encryption_block_CFB_mode(m[index:index+nb], iv, nb, k)
        r += c
        index += nb
    return r

def decryption_block_CFB_mode(b, iv, nb, k):
    civ = cesier(iv, k) # encryption of the iv
    left_civ = civ[0:nb] #left part of encryption of the iv
    c = xor(left_civ, b) #xor the left part and the block
    return c

def decryption_CFB_mode(m, iv, nb, k): # m: message , iv : initial vector , nb : number of bits of a block , k : encryption key  
    message_len = len(m)
    if message_len % nb != 0:
        index = 0
        while index < nb - (message_len % nb):
            m.append(0)
            index += 1 
    index = 0
    r= []
    while index < len(m):
        c = decryption_block_CFB_mode(m[index:index+nb], iv, nb, k)
        iv = iv[nb-1:-1] + m[index:index+nb]
        r += c
        index += nb
    return r
##### testing:

### cesir testing:
m = [1, 2, 3, 4]
n = 1
print(cesier(m, n))


### block CFB testing:
b = [1, 0, 1]
iv = [1, 0, 1, 0]
nb = 3
k = 1
print(encryption_block_CFB_mode(b, iv, nb, k))

#### Encryption CFB mode testing:
m = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1] #c =[1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0]
iv = [1, 0, 1, 0]
nb = 3
k = 1
print(encryption_CFB_mode(m, iv, nb, k))

#### Decryption CFB mode testing:
c =[1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0] #m = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]
iv = [1, 0, 1, 0]
nb = 3
k = 1
print(decryption_CFB_mode(c, iv, nb, k))
