# easy to understand example of an iterator and a generator

# home-made iterator that does the same as the range function:
class MyNumRange:

    def __init__(self,start,end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


# generator that does the same thing:
def my_num_range(start,end):
    current = start
    while current < end:
        yield current
        current += 1


   

