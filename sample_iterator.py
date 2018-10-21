class SampleIterator(object):
    def __init__(self, num):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.num:
            raise StopIteration()

        ret = self.current
        self.current += 1
        return ret
