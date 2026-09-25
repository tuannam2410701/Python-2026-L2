def extract_even(list):
    result = []

    for x in list:
        if x % 2 == 0:
            result.append(x)

    return result


print(extract_even([1, 4, 5, -1, 10]))