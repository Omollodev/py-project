
def search_list(list, element):
    middle = 0
    start = 0
    end = len(list)
    sequence = 0

    while (start <= end):
        print("Steps", sequence, ":", str(list[start:end+1]))
        sequence = sequence+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 1
search_list(my_list, target)
