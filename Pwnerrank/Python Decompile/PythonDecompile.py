#!/usr/bin/env python

import textwrap
import sys

if len(sys.argv) < 2:
    sys.exit('Usage: %s <password>' % sys.argv[0])
input = sys.argv[1]

if len(input) != 16:
    sys.exit('Try again !')

max_bits = 32


rol = lambda val, r_bits, max_bits: val << r_bits % max_bits & 2 ** max_bits - 1 | (val & 2 ** max_bits - 1) >> max_bits - r_bits % max_bits
ror = lambda val, r_bits, max_bits: (val & 2 ** max_bits - 1) >> r_bits % max_bits | val << max_bits - r_bits % max_bits & 2 ** max_bits - 1

buf = textwrap.wrap(input.encode('hex'), 8)


buf = [ int(val, 16) for val in buf ]

sa = [
 134, 181, 218, 6, 68, 99, 48, 92,
 42, 29, 2, 186, 183, 5, 42, 154,
 224, 184, 20, 246, 145, 55, 168, 187,
 40, 188, 27, 221, 139, 27, 156, 248,
 134, 206, 51, 103, 132, 230, 134, 193,
 32, 120, 11, 109, 42, 44, 231, 34,
 181, 89, 250, 94, 83, 85, 1, 71,
 94, 9, 138, 92, 222, 196, 75, 114]
sb = [
 43, 194, 74, 148, 253, 128, 130, 207,
 148, 151, 209, 115, 179, 141, 69, 66,
 225, 79, 110, 2, 46, 169, 119, 6,
 176, 49, 93, 210, 123, 146, 168, 53,
 7, 71, 247, 126, 15, 228, 50, 250,
 55, 45, 125, 90, 81, 114, 181, 251,
 21, 8, 87, 161, 219, 160, 205, 212,
 123, 108, 48, 186, 11, 31, 152, 24]


for i in range(64):
    buf[0] = rol(buf[0] ^ buf[3], 1, max_bits)
    buf[1] = rol(buf[1] ^ buf[2], 2, max_bits)
    buf[2] = rol(buf[2] ^ buf[3], 3, max_bits)
    buf[3] = rol(buf[3] + (sa[i] & sb[i] + 4919), 4, max_bits)
    print sa[i] & sb[i]

if buf[0] == 3550062758 and buf[1] == 1007223928 and buf[2] == 1760475108 and buf[3] == 1597012241:
    print 'Congratulations !'
else:
    print 'Incorrect password !'
