import random
import itertools


# I implemented some crypto and encrypted my secret: 03_duCbr5e_i_rY_or cou14:L4G f313_Th_etrph00 Wh03UBl_oo?n07!_e

# Can you get it back?


def encrypt(msg, key):
    keylen = len(key) #8    

    k = [x[1] for x in sorted(zip(key[:keylen], range(keylen)))] # second largest value in key (30,6), with a random value from 0 to 7 attached 

    #k is scrambled version of 0 to 7, constant
    m = ''
    for i in k: #runs 8 times but i is random
        for j in range(i, len(msg), keylen): #range(start,stop,step), runs 62 times
            m += msg[j]
    return m

# 0,8,16,24,32,40,48,56, 6 steps of 8
# 1,9,17,25,33,41,49,57
# 2,10,18,26,34,42,50,58
# 3,11,19,27,35,43,51,59
# 4,12,20,28,36,44,52,60
# 5,13,21,29,37,45,53,61
# 6,14,22,30,38,46,54    2 steps of 7
# 7,15,23,31,39,47,55,   
#everything gets shuffled and everything twice

# m = input()
# while True:
#     k = [random.randrange(256) for _ in range(16)]  # generate 16 random integers from 0 to 256
#     if len(k) == len(set(k)):
#         break

# m = encrypt(m, k[:8]) #key is the first 8 bits
# m = encrypt(m, k[:8])
# print(m)

#groups of 8 
secret = "03_duCbr5e_i_rY_or cou14:L4G f313_Th_etrph00 Wh03UBl_oo?n07!_e"

#we know length of 62

sett = [0,1,2,3,4,5,6,7]
tot = {}
tot = itertools.permutations(sett)
    
for x in tot:
    secret = "03_duCbr5e_i_rY_or cou14:L4G f313_Th_etrph00 Wh03UBl_oo?n07!_e"
    flag = [None] * 62
    
    for m in range(2): 
        begin = 0
        for y in x: #For each loop
            temp = []
            if y !=7 and y !=6:
                temp = secret[begin:begin+8]
                begin += 8
            else:
                temp = secret[begin:begin+7]
                begin += 7
            start = y
            for p in range(len(temp)):
                flag[start] = temp[p]
                start +=8
        s = ""
        for u in flag:
            s += u
        secret = s
    r = ""    
    for q in flag:
        r += q
    if "34C3" in r:
        print(r)





