def merge(intervals):
    intervals.sort()
    merged_list = [intervals[0]]
    for i in range(len(intervals) - 1):
        if merged_list[-1][1] >= intervals[i + 1][0]:
            start = min(merged_list[-1][0], intervals[i + 1][0])
            end = max(merged_list[-1][1], intervals[i + 1][1])
            merged_list.append([start, end])
            if i == 0:
                merged_list.pop(i)
            if i > 0:
                merged_list.pop(-2)
        else:
            merged_list.append(intervals[i + 1])
    return merged_list


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 3], [2, 6], [5, 10], [15, 18]]))
