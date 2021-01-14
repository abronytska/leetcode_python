import math


def kClosest(points, K):
    distances = {idx: 0 for idx, item in enumerate(points)}
    result_list = list()
    for i in range(len(points)):
        distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        distances[i] = distance
    distances = sorted([[v, k] for k, v in distances.items()])
    i = 0
    for dist, idx in distances:
        result_list.append(points[idx])
        i = i + 1
        if i == K: break

    return result_list


# print(kClosest([[3, 3], [5, -1], [-2, 4]], K=2))
print(kClosest([[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[1,1]], K=1))

class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]