# Check if 2 strings have the same alphabets
# dog <==> o dg


def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    #Edge case check
    if len(str1) != len(str2):
        return False

    # Create empty dictionary
    count1 = {}

    for letter in str1:
        if letter not in count1:
            # dictionary[key] = value
            count1[letter] = 1
        else:
            count1[letter] = count1[letter] + 1

    for letter in str2:
        if letter in count1:
            count1[letter] = count1[letter] - 1
        else:
            count1[letter] = 1

    for letter in count1:
        if count1[letter] == 0:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    print(anagram("dog", "o gd"))
