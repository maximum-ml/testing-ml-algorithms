import numpy as np
from scipy import signal

########### 2-dimentional correlations ############

a = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ]

b = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]

mask = [
        [1, 1],
        [1, 1]
]


x1 = signal.correlate2d(a, mask, 'valid')   # ta funkcja nie jest przemienna!
print(f'x1={x1}')

x2 = signal.correlate2d(b, mask, 'valid')
print(f'x2={x2}')

c = [[1, 2], [3, 1]]


dot = np.dot(np.asarray(mask), np.asarray(c))
print(f'dot={dot}')
print(f'dot_sum={dot.sum()}')


multi = np.asarray(mask) * np.asarray(c)
print(f'multi={multi}')
print(f'multi_sum={multi.sum()}')


l = [2, 5]

dot = np.dot(np.asarray(c), np.asarray(l))
print(f'dot={dot}')


def sliding_dot_prod_2D(input: np.ndarray, mask: np.ndarray) -> np.ndarray:
    '''
        sliding dot product behaves the same way as signal.correlate2d
        we assume tha input matrix must be bigger than mask matrix
    '''
    result = []
    for y in range(input.shape[0] - mask.shape[0] + 1):
        line = []
        for x in range(input.shape[1] - mask.shape[1] + 1):
            dot_prod_matrix = input[y:y + mask.shape[0], x:x + mask.shape[1]] * mask
            line.append(dot_prod_matrix.sum())
        result.append(line)
    return np.asarray(result)


sdp1 = sliding_dot_prod_2D(np.asarray(b), np.asarray(mask))
print(f'sdp1={sdp1}')




