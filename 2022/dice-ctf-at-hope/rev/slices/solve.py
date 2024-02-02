
#if flag[:5] != 'hope{': fail()
#if flag[-1] != '}': fail()
#if flag[5::3] != 'i0_tnl3a0': fail()
#if flag[4::4] != '{0p0lsl': fail()
#if flag[3::5] != 'e0y_3l': fail()
#if flag[6::3] != '_vph_is_t': fail()
#if flag[7::3] != 'ley0sc_l}': fail()

flag_d = {}
for i, v in enumerate(range(5, 32, 3)):
    flag_d[v] = 'i0_tnl3a0'[i]
for i, v in enumerate(range(4, 32, 4)):
    flag_d[v] = '{0p0lsl'[i]
for i, v in enumerate(range(3, 32, 5)):
    flag_d[v] = 'e0y_3l'[i]
for i, v in enumerate(range(6, 32, 3)):
    flag_d[v] = '_vph_is_t'[i]
for i, v in enumerate(range(7, 32, 3)):
    flag_d[v] = 'ley0sc_l}'[i]

flag_d[0] = 'h'
flag_d[1] = 'o'
flag_d[2] = 'p'
flag_d[3] = 'e'
flag_d[4] = '{'
flag_d[31] = '}'

flag = ''
for i in range(32):
    flag += flag_d[i]

print(flag)
