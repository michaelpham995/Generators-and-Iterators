#This function writes the zip function without utilizing zip() and takes in any input

def my_zip(*inputs):
    traversables = [iter(i) for i in inputs]
    while traversables:
        ans = []
        for i in traversables:
            try:
                #adding each val from each input into ans to set up for tuple later
                currVal = next(i)
                ans.append(currVal)
            #Below is for when we run out of values on one of the inputs.
            except StopIteration:
                return
        #Puts tuple in generator object
        yield tuple(ans)
    return