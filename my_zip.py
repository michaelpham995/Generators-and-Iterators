x = [1,2,3]

no = [v * 5 for v in x]
yes = (v * 5 for v in x)



print(hasattr(no, "__next__")) #Not a generator object - not exhaustible
print(hasattr(no, "__iter__"))

print(hasattr(yes, "__next__")) #Generator object - exhaustible - lazy
print(hasattr(yes, "__iter__"))

#Lambdas
add = lambda x, y : x + y 
print(add(2,3))

#Map

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x ** x

#Without Map function
newList = []
for x in li:
    newList.append(func(x))
print(newList)

#Wtih map function
#Map takes 2 arguments -> Function and List
print(list(map(func, li)))

#One liner without input using lambda
print(list(map(lambda n: n ** n, [1,2,3,4,5])))
