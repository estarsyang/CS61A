this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def add(b):
        nonlocal a
        a = a + 1
        return a + b - 1
    return add


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    # first = -1
    # second = 1
    # def next_fib():
    #     nonlocal first, second
    #     next_num = first + second
    #     first = second
    #     second = next_num

    #     return next_num
    
    # return next_fib
    f1, f2 = 1, 0
    def next_fib():
        nonlocal f1, f2
        f1,f2 = f2, f1 + f2
        return f1
    return next_fib

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    if entry not in lst:
        return 'entry is not in lst'
    # lst.append([])
    # count= lst.count(entry)
    # for item in range(0,count):
    #     index = lst.index(entry)
    #     lst[-1].append(index)
    #     lst[index] = 'a'
    # num = 0
    # for index in lst[-1]:
    #     lst[index+num] = entry
    #     lst.insert(index + num + 1, elem)
    #     num += 1
    # lst.pop()

    index = 0
    size = len(lst)
    while index < size:
        if lst[index] == entry:
            lst.insert(index + 1, elem)
            index += 1
            size += 1

        index += 1
    # first, do a normal for loop
    # while index < size:
    #   xxxxxxx
    #   index += 1

    # second, do an equality judgment and insert
    # if lst[index] == entry:
    #     lst.insert(index + 1, elem)

    # third, modify size and index
    # cuz insert one element, size plus one, index also plus one to skip this element
    # if lst[index] == entry:
    #     lst.insert(index + 1, elem)
    #     index += 1
    #     size += 1
    return lst
