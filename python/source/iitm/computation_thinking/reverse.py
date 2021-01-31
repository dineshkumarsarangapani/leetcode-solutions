def first(l):
    if len(l) != 0:
        return l[0]


def last(l):
    if len(l) != 0:
        return l[len(l) - 1]


def init(l):
    if len(l) != 0:
        return l[:-1]


def rest(l):
    if len(l) != 0:
        return l[1:]

def reverse(l):
    if len(l) <= 1:
        return l
    a = []
    a.append(last(l))
    a.extend(reverse(rest(init(l))))
    a.append(first(l))
    return a
    #return [last(l)].append(reverse(init(rest(l))))


if __name__ == '__main__':
    print(first([1, 2, 3, 4]))
    print(last([1, 2, 3, 4]))
    print(init([1, 2, 3, 4]))
    print(rest([1, 2, 3, 4]))
    print(reverse([1, 2, 3, 4]))
