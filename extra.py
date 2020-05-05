

import heapq


def merge(arr):
    retVal = []
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            currVal = arr[j][i]
            if retVal and currVal < retVal[-1]:
                retVal.insert(len(retVal) - 1, currVal)
            else:
                retVal.append(arr[j][i])

    return retVal


k = [[10, 15, 30], [12, 14, 20], [17, 20, 32]]

# print(merge(k))


def merge_heap(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        print(heap)
        val, list_idx, element_idx = heapq.heappop(heap)

        merged_list.append(val)

        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1],
                          list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)

    return merged_list


print(merge_heap(k))
