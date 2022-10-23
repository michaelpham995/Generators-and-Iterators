#Generator function
def my_islice_generator(input, start, stop):
    if stop <= len(input):
        #iterate through the start -> stop range as specified
        for i in range(start, stop):
            yield input[i]

#Iterator Class
class my_islice_iterator:

    #Constructor 
    def __init__(self, input, start = 0, stop = 0): #Default values is 0 so no output unless specified
        self.input = input
        self.start = start
        self.stop = stop

    #Iterator 
    def __iter__(self):
        return self

    #Next
    def __next__(self):
        x = list(self.input)
        #If the length of the input is 0, we do not iterate as there are no values
        if len(x) == 0:
            raise StopIteration
        #If start < stop, then we can iterate more values
        if self.start < self.stop:
            val = self.start
            self.start += 1
            return x[val]
        else:
            #If start reaches stop then we exit and raise an exception
            raise StopIteration
