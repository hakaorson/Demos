def make_averager(temp):
    series = []

    def averager(new_value):
        series.append(new_value)
        temp2 = temp
        total = sum(series)
        return total/len(series)
    return averager


ave = make_averager(1)
ave(10)
ave(12)
print(ave(11))
print(ave.__code__.co_freevars)
print(ave.__code__.co_varnames)
