# 2 arrays as input. In the second array one element will be missing. Find that element.


def finder(arr1, arr2):     # Sum solution not the best if input numbers too big &/or too many which may cause overflow
    total1 = 0
    total2 = 0
    for element in arr1:
        total1 = total1 + element
    for element in arr2:
        total2 = total2 + element
    return total1 - total2


def finder1(arr1, arr2):
    total1 = sum(arr1)
    total2 = sum(arr2)
    return total1 - total2


def finder2(arr1, arr2):
    for element in arr1:
        if element in arr2:
            arr2.remove(element)  # delete the element
        else:
            return element


def finder3(arr1, arr2):
    dict1 = {}

    for element in arr2:
        if element not in dict1:
            dict1[element] = 1
        else:
            dict1[element] = dict1[element] + 1

    for element in arr1:
        if dict1[element] == 0:
            return element
        else:
            dict1[element] = dict1[element] - 1

    # for element in dict1:
    #     if dict1[element] != 0:
    #         return element


if __name__ == '__main__':
    print(finder([2, 2, 2, 2, 4], [2, 2, 4, 2]))
