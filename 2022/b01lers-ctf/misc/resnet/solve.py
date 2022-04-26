from os import popen
import numpy as np
import matplotlib.pyplot as plt


def get_diff(arr):
    plt.imsave('./test.jpeg', arr)
    res = popen(
        'base64 -w0 ./test.jpeg | python3 ./resnet_password.py').read().strip()
    diff = float(res[res.find('0.0'):])
    print(f'diff: {diff}')
    return diff


ans_cnt = 0
arr = np.zeros((224, 224, 3))
min_diff = get_diff(arr)
while min_diff >= 1e-4:
    for d in range(3):
        for r in range(224):
            for c in range(224):
                for i in range(1, 21):
                    change = 0.05*i
                    tmp = arr.copy()
                    tmp[r][c][d] = change
                    if tmp[r][c][d] > 1.0:
                        break
                    print(f'({r}, {c}, {d}) {tmp[r][c][d]:.2f}')
                    diff = get_diff(tmp)
                    if diff < min_diff:
                        arr[r][c][d] = change
                        min_diff = get_diff(arr)
                        print(f'New min diff: {min_diff}')
                if min_diff < 1e-4:
                    print(f'Acceptable diff: {get_diff(arr)}')
                    with open(f'./min_diff_{ans_cnt}.npy', 'wb') as f:
                        np.save(f, arr)
                        ans_cnt += 1

print(f'Final diff: {get_diff(arr)}')
with open('./min_diff.npy', 'wb') as f:
    np.save(f, arr)
