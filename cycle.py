#Practice Generators


#Cycle Function 


#Iterates through a given iterable - assumes indexable

def cycle(iter):
    if iter:
        while True:
            for i in range(len(iter)):
                yield iter[i]
    else:
        pass



#This implementation handles a non indexable input
def cycle_for(s):
    p = iter(s)
    try:
        next(p)
    except StopIteration:
        return
    p = iter(s)
    while True:
        try:
            while True:
                w = next(p)
                yield w
        except StopIteration:
            p = iter(s)
    #Have some statement to stop iterating when a certain count is hit to avoid infinity


def count(start, *increment):
    if not increment:
        s = 1
    else:
        s = increment[0] #Index 0 because *increment is a tuple - we are packing 
    n = start
    while True:
        yield n 
        n += s
 
#repeat(element, [n]) -> optional n -> how long will you repeat for 


def repeat_while(s, *a):
    if a:
        x = 0
        while x < a[0]:
            yield s
            x +- 1
    else:
        while True:
            yield s
            


#Chain function -> Generator

def chain(*inputs):
    for input in inputs:
        tmp = iter(input)
        while True:
            try:
                while True:
                    x = next(tmp)
                    yield x
            except StopIteration:
                break

#Simplified code
def chain2(*inputs):
    if inputs:
        return (j for i in inputs for j in i)
    else:
        pass




