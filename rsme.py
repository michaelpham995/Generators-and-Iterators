import math

def rsme(set1, set2):

    if len(set1) > len(set2):
        set1 = set1[:len(set2)]

    return math.sqrt((sum((set1[i] - set2[i]) ** 2 for i in range(len(set1)))) / len(set1))

print(rsme([2,3,4], [3,2,5])) #Passed
print(rsme([2,3,4], [4,3,2])) #Passed
print(rsme([2,3,4,1], [4,3,2])) #Passed
print(rsme([1,2,3], [1,2,3]))
print(list(map(lambda x: x ** 2, [2]))) #4





x = [1,2,3,4,5]
print(list(map(lambda i: i ** 2, x)))