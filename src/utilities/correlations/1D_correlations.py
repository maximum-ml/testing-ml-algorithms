import numpy as np
from scipy import signal

########### 1-dimentional correlations ############

a = [1, 2, 3, 4, 5]
b = [1]

x1 = signal.correlate(a, b)
x2 = signal.correlate(b, a)

print(x1)
print(x2)

c = [1, 1]

x3 = signal.correlate(a, c, 'valid')
print(f'x3={x3}')


def sliding_dot_prod1(a: list, b: list) -> list:
    result = []
    for i in range(len(a) - len(b) + 1):
        x = 0
        for j in range(len(b)):
            x += a[i + j] * b[j]
        result.append(x)
    return result


sdp1 = sliding_dot_prod1(a, c)
print(f'sdp1={sdp1}')


def sliding_dot_prod2(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    result = []
    for i in range(a.size - b.size + 1):
        result.append(np.dot(a[i:i+b.size], b))
    return np.asarray(result)


sdp2 = sliding_dot_prod2(np.asarray(a), np.asarray(c))
print(f'sdp2={sdp2}')


sdp3 = np.correlate(a, c)
print(f'sdp3={sdp3}')
