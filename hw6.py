# 1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break
    return lst
list1 = [5, 7, 1, 3, 2]
sorted_list1 = bubble_sort(list1)
print(sorted_list1)

# 2
def binary_search(val, a):
    first = 0
    last = len(a) - 1
    ResultOK = False

    while first < last and not ResultOK:
        middle = (first + last) // 2
        if a[middle] == val:
            first = middle
            last = first
            ResultOK = True
            pos = middle
        else:
            if val > a[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if ResultOK:
        print("Элемент найден", pos)
    else:
        print("Элемент не найден")



a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 3

print(binary_search(val, a))