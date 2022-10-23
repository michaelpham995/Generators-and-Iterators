import math

def RSME(set1, set2):

    if len(set1) > len(set2):
        set1 = set1[:len(set2)]
    elif len(set2) > len(set1):
        set2 = set2[:len(set1)]

    return math.sqrt((sum((set1[i] - set2[i]) ** 2 for i in range(len(set1)))) / len(set1))

print(RSME([2,3,4], [3,2,5])) #Passed
print(RSME([2,3,4], [4,3,2])) #Passed
print(RSME([2,3,4], [4,3,2,1]))




    