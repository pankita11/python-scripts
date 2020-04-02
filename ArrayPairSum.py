# Return pairs of numbers in given list whose addition is equal to k
# Steps:
# Add first element with rest of the elements in the list.
# If the addition is equal to k, then add it to the final list/set.
# But as we want only unique pairs, we will use a set which stores only unique numbers/pairs
# Make sure we are adding into the set in ascending order so the non-unique pairs are removed automatically.


def pair_sum(arr, k):
    pairs = set()       # Set and not list as it would allow only unique pairs
    for i, val in enumerate(arr):
        # print(i, val)
        for j in arr[i + 1:]:
            # print(j)
            if val + j == k:
                # print("{}+{} = {}".format(val,j,k))
                pairs.add((min(val, j), max(val, j)))  # Double set of parentheses to pass 2 args as tuple
            else:
                continue
    return pairs

def pair_sum2(arr, k):

    pairs = set()

    for i in arr:
        diff = k-i
        if diff in arr:
            pairs.add((min(i, diff), max(i, diff)))

    return pairs



if __name__ == '__main__':
    print(pair_sum2([1, 2, 3, 1], 3))
