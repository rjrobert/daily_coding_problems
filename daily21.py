"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def get_class_numbers(class_times):
    classrooms = 0
    class_times = sorted(class_times)

    for i in range(len(class_times)):
        if i + 1 >= len(class_times):
            break
        if class_times[i][1] > class_times[i + 1][0]:
            classrooms += 1

    return classrooms


class_times = [(30, 75), (0, 50), (60, 150)]
print(get_class_numbers(class_times))
