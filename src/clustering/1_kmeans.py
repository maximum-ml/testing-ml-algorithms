import math

import numpy as np

import matplotlib.pyplot as plt

from trainings.wk_utils import utils as wk_utils
from trainings.wk_plots import plots as wk_plots


def k_means(points, K):
    """
    :param points: all 2D points as list of tuples (x, y)
    :param K: number of clusters
    :return: list of cluster ids in the same order as input points e.g. [2, 1, 3, 1, 1 ...]
    """

    # x, y = wk_utils.decompose_to_lists(points)
    # min_x = np.amin(x)
    # max_x = np.amax(x)
    # min_y = np.amin(y)
    # max_y = np.amax(y)

    cluster_codes = np.zeros(len(points), dtype='int32')

    centroids = []
    # init random centroid
    random_idx = np.random.choice(range(len(points)), K, replace=False)
    for idx in random_idx :
        centroids.append(points[idx])

    print(f'INIT CENTROIDS={centroids}')

    while True:

        print(f'CENTROIDS={centroids}')

        # calculate distance from each point to each centroid -> matrix [n rows (points) x K cols (clusters)]
        dist_matrix = []
        for point in points:
            dists = get_dists2D(point, centroids)
            dist_matrix.append(dists)

        # assign points to the nearest cluster
        p_idx = 0
        for p_d in dist_matrix:
            arg_min = np.argmin(p_d)
            cluster_codes[p_idx] = arg_min + 1
            p_idx += 1

        # calculate new centroids
        clustered_points = {}
        p_idx = 0
        for p in points:
            cluster_id = cluster_codes[p_idx]
            clustered_points.setdefault(cluster_id, []).append(p)
            p_idx += 1

        new_centroids = calculate_centroids(clustered_points)
        if np.array_equal(centroids, new_centroids):
            break
        else:
            centroids = new_centroids

    return cluster_codes

def calculate_centroids(clustered_points):
    centroids = []
    for k in sorted(clustered_points):
        centroids.append(calculate_centroid_for_points(clustered_points.get(k)))
    return centroids


def calculate_centroid_for_points(points):
    sum_x = 0.0
    sum_y = 0.0
    for point in points:
        x, y = point
        sum_x += x
        sum_y += y
    return sum_x/len(points), sum_y/len(points)



def get_dists2D(p0, points):
    d = []
    for p in points:
        d.append(get_distance2D(p0, p))
    return d

def get_distance2D(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )


all_points = [
    (0, 0),
    (1, 0),
    (2, 1),
    (4, 2),
    (4, 4),
    (5, 3),
    (1, 1),
    (2, 0),
    (0, 2),
    (4, 3),
    (5, 5),
    (3, 3),
    (1, 4),
    (3, 1),
    (2, 4),
    (8, 8),
    (8.5, 8.5),
    (8, 9),
    (9, 8),
    (9, 9)
]

# points2 = [
#     (1, 1),
#     (2, 0),
#     (3, 0),
#     (4, 1),
#     (5, 5),
#     (3, 3)
# ]

random_idx = np.random.choice(range(len(all_points)), 3, replace=False)
print("rdn_ids", random_idx)



clusters = np.zeros(5, dtype='int32')
print("clusters", clusters)


a = ['x', 'x']
b = ['y', 'y']

c = []
c.append(a)
c.append(b)

print("c=",c)


centr1 = calculate_centroid_for_points(all_points)

print(f'centr1={centr1}')

K = 2

clusters = k_means(all_points, K)
print(f'clusters={clusters}')

pp1 = []
pp2 = []

# idx = 0
for i in range(len(clusters)):
    if clusters[i] == 1:
        pp1.append(all_points[i])
    else:
        pp2.append(all_points[i])

wk_plots.plot_points_on_plt(plt, pp1, "C1")
wk_plots.plot_points_on_plt(plt, pp2, "C2")
# wk_plots.plot_points_on_plt(plt, all_points, "all")
plt.legend()
plt.show()
