l1 = [14,17,20,21,22,21,19,18,12,6,1,16,15,14]
l2 = [0,3,0,1,0,1,1,0,6,0,5,0,1,0]

notes = []
for idx in range(14):
    for i in range(12):
        for j in range(12):
            if ((i+j) == l1[idx]) and ((i-j) == l2[idx]):
                print(idx, i, j)

'''
output:
0 7 7
1 10 7
2 10 10
3 11 10
4 11 11
5 11 10
6 10 9
7 9 9
8 9 3
9 3 3
11 8 8
12 8 7
13 7 7

notes: 7, 7, 10, 10, 11, 11, 10, 9, 9, 3, 3, 8, 8, 7, 7
AIS3{7wink1e_tw1nkl3_l1ttl3_574r_1n_C_5h4rp}
'''
