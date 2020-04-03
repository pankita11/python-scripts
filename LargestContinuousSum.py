# Iterate over the entire given array.
# Add the individual items one by one. Put the individual sums to another array.
# Return the highest number from the second array.
# But importantly when adding total check if the num itself is bigger, if it is then it is the largest sum itself.
# For eg [-1, 1]


def edge_case(arr):
    if len(arr) == 1:
        return arr[0]


def large_cont_sum(arr):
    if edge_case(arr):
        return arr[0]
    total = 0
    total_arr = []
    for i in arr:
        total = max((total + i), i)
        total_arr.append(total)

    final = total_arr[0]
    for j in total_arr:
        if j > final:
            final = j
    return final


def large_cont_sum2(arr):
    edge_case(arr)
    current_sum = arr[0]
    max_sum = arr[0]

    for i in arr[1:]:
        current_sum = max((current_sum + i), i)
        max_sum = max(current_sum, max_sum)
    return max_sum


if __name__ == '__main__':
    print(large_cont_sum([-1]))
