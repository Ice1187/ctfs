import numpy as np

s = 'wiieh://ephitqxc.rdb/tAQtEOTn'
s = 'wiiehephitqxc.rdbtAQtEOTn'
a = np.array([c for c in s], dtype=object)

print(a.reshape(5, 5))
