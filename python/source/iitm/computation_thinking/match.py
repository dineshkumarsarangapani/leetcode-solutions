def first(l):
    if len(l) != 0:
        return l[0]


def last(l):
    if len(l) != 0:
        return l[len(l) - 1]


def init(l):
    if len(l) != 0:
        return l[:-1]
    else:
        return []


def rest(l):
    if len(l) != 0:
        return l[1:]
    else:
        return []


def match(players):
    if len(players) == 0:
        return []
    else:
        firstLast = [[first(players), last(players)]]
        middle = init(rest(players))
        if len(middle) >0:
            firstLast.append(match(middle))
        return firstLast


if __name__ == '__main__':
    players = [1, 2, 3, 4, 5, 6]
    a = match(players)
    print(a)
