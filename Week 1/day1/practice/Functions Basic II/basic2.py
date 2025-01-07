#1
def countdown(num):
    for i in range(num, -1, -1):
        return i
print(countdown(5))

#2
def printe(list):
    print(list[0])
    return list[1]
resulta = printe([1,2])
print(resulta)

#3
def first_plus_length(lst):
    first = lst[0]
    length = len(lst)
    return first + length
print(first_plus_length([1, 2, 3, 4, 5]))
#4
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    else:
        second = list[1]
        result = []
        for i in list:
            if i > second:
                result.append(i)
        print(len(result))
        return result
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))  
#5
def lengthe(size, value):
    return [value] * size
print(lengthe(4, 20))
print(lengthe(6, 22))

